import joblib
import json
import numpy as np
import pandas as pd

CATEGORIAL_COLUMNS = ['host_response_time',
                      'host_is_superhost',
                      'host_identity_verified',
                      'is_location_exact',
                      'property_type',
                      'room_type',
                      'bed_type',
                      'cancellation_policy'
                      ]
USED_CATEGORIAL_FEATURES = [0, 1, 3, 6, 9, 16, 18, 22, 25, 30,
                            31, 32, 33, 48, 53, 54, 55, 65, 66,
                            ]
NUMERIC_FEATURES = ['accommodates',
           'bedrooms',
           'cleaning_fee',
           'guests_included',
           'minimum_nights',
           'neighbourhood_cleansed',
           ]

class Regressor(object):
    def __init__(self):
        with open("distr_dict.json", "r") as read_file:
            self.distr_dict = json.load(read_file)
        self.model = joblib.load("model_dump.pkl")
        self.enc = joblib.load("enc_dump.pkl")

    def predict_price(self, query_dict):
        cat_features = [query_dict[i] for i in CATEGORIAL_COLUMNS]
        cat_features = np.array(cat_features).reshape(1, - 1)
        cat_features = self.enc.transform(cat_features)
        cat_features = cat_features[:, USED_CATEGORIAL_FEATURES]
        query_dict['neighbourhood_cleansed'] = self.distr_dict[query_dict['neighbourhood_cleansed']]
        num_features = [query_dict[i] for i in NUMERIC_FEATURES]
        query_vec = np.array(num_features + list(*cat_features))
        query_vec = query_vec.reshape(1, -1)
        #res = 0
        #for estim in self.model:
        #    res += estim.predict(query_vec)
        #res = res / len(self.model)
        res = self.model.predict(query_vec)
        return round(res[0], 2)
