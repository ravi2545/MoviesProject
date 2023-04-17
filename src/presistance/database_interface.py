import abc

class DatabaseInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, table_name, input_list):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def fetch_all(self, table_name):
        """Load in the data set"""
        raise NotImplementedError
    
    @abc.abstractmethod
    def fetch_by_id(self, table_name, id):
        """Load in the data set"""
        raise NotImplementedError
    
    @abc.abstractmethod
    def update(self, table_name, input_list, id):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def delete_by_id(self, table_name, id):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def delete_by_column_name_and_value_dict(self, table_name, column_name_and_value_dict):
        """Load in the data set"""
        raise NotImplementedError