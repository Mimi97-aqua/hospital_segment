from .index import index_route
from .participants import participants_routes
from .prescriptions import prescriptions_route


def register_routes(app):
    app.register_blueprint(index_route)
    app.register_blueprint(participants_routes, url_prefix='/participant')
    app.register_blueprint(prescriptions_route)
