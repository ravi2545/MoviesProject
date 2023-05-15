"""data_management_model_serializer.py: Contains classes and methods to convert object to JSON"""
__author__      = "Ravi Prasad"


from json import JSONEncoder, dumps
from uuid import UUID
from datetime import datetime
import decimal

#
# Custom JSON Serializer for models
#
class CustomJSONSerializer(JSONEncoder):

    # Overload method default
    def default(self, obj):
        
        # UUIDs, 
        if isinstance(obj, UUID):
            return str(obj)

        # datetimes
        if isinstance(obj, datetime):
            return obj.isoformat()

        if isinstance(obj, decimal.Decimal):
            return str(obj)
        # Otherwise, default to super
        #return JSONEncoder.default(self, obj)
        #return super(DatasetTypeModelSerializer, self).default(obj)
        return obj.__dict__

