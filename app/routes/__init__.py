from .participants import participants_routes


def register_routes(app):
    app.register_blueprint(participants_routes, url_prefix='/participants')