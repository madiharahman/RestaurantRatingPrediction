import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self,name,online_order,book_table,rate,votes,location,rest_type,cost2plates,category,grouped_cuisines):
        self.name = name
        self.online_order = online_order
        self.book_table = book_table
        self.rate = rate
        self.votes = votes
        self.location = location
        self.rest_type = rest_type
        self.cost2plates = cost2plates
        self.category = category
        self.grouped_cuisines = grouped_cuisines

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                "name": [self.name],
                "online_order": [self.online_order],
                "book_table": [self.book_table],
                "rate": [self.rate],
                "votes": [self.votes],
                "location": [self.location],
                "rest_type": [self.rest_type],
                "cost2plates": [self.cost2plates],
                "category": [self.category],
                "grouped_cuisines": [self.grouped_cuisines]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)  