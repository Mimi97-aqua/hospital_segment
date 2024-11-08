from flask import Blueprint

index_route = Blueprint('index', __name__)

@index_route.route('/', methods=['GET', 'LONI'])
def index():
    return "Welcome to the Hospital Segment"
