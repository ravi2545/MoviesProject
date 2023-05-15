from flask import Blueprint,request, Response
import json
from src.hollywood.horrormovies.services.horror_services import StatisticsService
from src.util.custom_serializers import CustomJSONSerializer

horror_lists = Blueprint('horror', __name__)


@horror_lists.route('', methods=['GET'])
def get_horror_movies():
    try:
        horror_statistics = StatisticsService()
        data = horror_statistics.get_all_statistics()
        print(data)
        resp = json.dumps(data, indent=1, cls=CustomJSONSerializer)
        return Response(resp, status=200)
    except Exception as e:
        return Response(str(e))
    # return 'list'