from flask import Blueprint,request, Response


horror_lists = Blueprint('horror', __name__)


@horror_lists.route('', methods=['GET'])
def get_horror_movies():
    return 'List'