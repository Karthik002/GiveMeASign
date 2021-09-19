from pymongo import MongoClient
from observable import Observable

class MongoDriver(Observable):
    def __init__(self):
        super().__init__()
        conn_string = 'mongodb+srv://admin:Vm#LKgG2_C9Cks$@cluster0.n4srd.mongodb.net/test'
        other_conn_string = 'mongodb+srv://admin:Vm%23LKgG2_C9Cks%24@cluster0.n4srd.mongodb.net/test'
        self.client = MongoClient(conn_string)
        self.db = self.client['htn_project_db']
        self.survey_data_collection = self.db['survey_data']
    
    def getSurvey(self, surveyName, surveyPassword):
        survey_dict = self.survey_data_collection.find_one({'name': surveyName, 'password': surveyPassword})
        survey_dict.pop('_id')
        return survey_dict