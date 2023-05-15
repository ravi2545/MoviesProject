__author__      = "Pravin.Kumar"

#
#
#
class StatisticsModel:

    def __init__(self) -> None:
        self.statistics_uuid = ""
        self.statistics_name = ""
        self.statistics_value = ""
        self.statistics_icon = ""
        self.statistics_priority = ""

    ## Setter
    def set_statistics_uuid(self, statistics_uuid):
        self.statistics_uuid = statistics_uuid
    def set_statistics_name(self, statistics_name):
        self.statistics_name = statistics_name
    def set_statistics_value(self, statistics_value):
        self.statistics_value = statistics_value
    def set_statistics_icon(self, statistics_icon):
        self.statistics_icon = statistics_icon
    def set_statistics_priority(self, statistics_priority):
        self.statistics_priority = statistics_priority

    ## Getter

    def get_statistics_uuid(self):
        return self.statistics_uuid
    def get_statistics_name(self):
        return self.statistics_name
    def get_statistics_value(self):
        return self.statistics_value
    def get_statistics_icon(self):
        return self.statistics_icon
    def get_statistics_priority(self):
        return self.statistics_priority


class DemoConsolidateddataStatisticsModel:

    def __init__(self) -> None:
        self.statistics_name = ""
        self.statistics_value = ""
        self.statistics_icon = ""
        self.statistics_priority = ""
    
    ## Setter
    def set_statistics_name(self, statistics_name):
        self.statistics_name = statistics_name
    def set_statistics_value(self, statistics_value):
        self.statistics_value = statistics_value
    def set_statistics_icon(self, statistics_icon):
        self.statistics_icon = statistics_icon
    def set_statistics_priority(self, statistics_priority):
        self.statistics_priority = statistics_priority
