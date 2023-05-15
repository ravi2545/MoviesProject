__author__ = "Ravi Prasad"

from src.hollywood.horrormovies.repos.horror_repo import Horror_Service_repo

class StatisticsService:

    def __init__(self):
        self.horror_repo_servives_data = Horror_Service_repo()


    ###############################
    ## Returns all statistics
    ###############################
    def get_all_statistics(self):
        return self.horror_repo_servives_data.fetch_all()

    ####################################
    ## Returns datatype based statistics
    ####################################
    # def get_datatype_statistics(self, dataset_type_uuid):
    #     dataset_type_uuid_data = self.statistics_repository_service.fetch_by_id(dataset_type_uuid)
    #     return dataset_type_uuid_data

    # def get_demo_statistics__consolidateddata(self):
    #     statistics__consolidateddata = self.statistics_repository_service.fetch_demo_consolidateddata_all()
    #     return statistics__consolidateddata