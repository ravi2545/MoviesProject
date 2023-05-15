__author__ = 'Ravi Prasad'

from src.presistance.database_factory import DatabaseFactory
from src.hollywood.horrormovies.model.statistics_model import StatisticsModel

class Horror_Service_repo:
    def __init__(self):
        self.table_name = 'algorithm'
        # self.demo_table = 'demo_statistics'
        self.postgres_database = DatabaseFactory().get_database_connection('POSTGRES')
        pass

    def fetch_all(self):
        statistics_model_list = []
        statistics_model_list_from_db = self.postgres_database.fetch_all(self.table_name)
        for row in statistics_model_list_from_db:
            # statistics_model = self.convert_db_row_to_statistics_model(row)
            statistics_model_list.append(row)
        return statistics_model_list
    
    ############################################################
    ## Convert DB row to Statistics model
    ############################################################
    def convert_db_row_to_statistics_model(self, row):
        statistics_model = StatisticsModel()
        statistics_model.set_statistics_uuid(row[0])
        statistics_model.set_statistics_name(row[1])
        statistics_model.set_statistics_value(row[2])
        statistics_model.set_statistics_icon(row[3])
        statistics_model.set_statistics_priority(row[4])
        return statistics_model