from regressor import Regressor
from codecs import open
import time
from flask import Flask, render_template, request
app = Flask(__name__)

print("Load regressor")
regr = Regressor()
print("Regressor is successfully loaded")


@app.route("/renting-apartments", methods = ["POST", "GET"])
def index_page(text = "",
               prediction_message = ""):
    if request.method == "POST":
        query_dict = {}
        query_dict['host_response_time'] = request.form['host_response_time']
        query_dict['host_is_superhost'] = request.form['host_is_superhost']
        query_dict['host_identity_verified'] = request.form['host_identity_verified']
        query_dict['is_location_exact'] = request.form['is_location_exact']
        query_dict['property_type'] = request.form['property_type']
        query_dict['room_type'] = request.form['room_type']
        query_dict['bed_type'] = request.form['bed_type']
        query_dict['cancellation_policy'] = request.form['cancellation_policy']
        query_dict['accommodates'] = request.form['accommodates']
        query_dict['bedrooms'] = request.form['bedrooms']
        query_dict['cleaning_fee'] = request.form['cleaning_fee']
        query_dict['guests_included'] = request.form['guests_included']
        query_dict['minimum_nights'] = request.form['minimum_nights']
        query_dict['neighbourhood_cleansed'] = request.form['neighbourhood_cleansed']

        prediction_message = regr.predict_price(query_dict)


    return render_template('simple_page.html', text = text, prediction_message = prediction_message)


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000, debug = True)
