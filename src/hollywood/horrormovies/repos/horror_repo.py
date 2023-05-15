__author__ = 'Ravi Prasad'

from src.presistance.database_factory import DatabaseFactory


class Horror_Service_repo:
    def __init__(self):
        self.table_name = 'statistics'
        # self.demo_table = 'demo_statistics'
        self.postgres_database = DatabaseFactory().get_database_connection('POSTGRES')
        pass

    def fetch_all(self):
        statistics_model_list = []
        statistics_model_list_from_db = self.postgres_database.fetch_all(self.table_name)
        for row in statistics_model_list_from_db:
            statistics_model = self.convert_db_row_to_statistics_model(row)
            statistics_model_list.append(statistics_model)
        return statistics_model_list