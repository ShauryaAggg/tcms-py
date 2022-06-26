from sanic import Sanic
from app.listeners import listeners
from app.routes import bp_group


if __name__ == "__main__":

    # register combined blueprint group here. these blueprints are defined in the routes directory and has to be
    # collected in init file otherwise route will end up with 404 error.

    app = Sanic(__name__)
    app._listeners = listeners
    app.blueprint(bp_group)
    app.run()
