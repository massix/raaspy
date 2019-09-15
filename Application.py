import logging

from connexion import FlaskApp
from flask_injector import FlaskInjector
from injector import Binder
from os import getenv
from waitress import serve


def get_logger():
    return logging.getLogger(__name__)


class Application(object):
    def __init__(self, port: int):
        logging.basicConfig(level=logging.INFO)
        self._port = port
        self._app = FlaskApp(__name__, port=self._port, specification_dir='swagger/')
        self._app.add_api('raaspy.yaml')
        FlaskInjector(app=self._app.app, modules=[self.configure])

    @classmethod
    def configure(cls, binder: Binder):
        return binder

    @property
    def app(self):
        return self._app


if __name__ == "__main__":
    a = Application(8080)
    serve(a.app) if getenv('environment', 'dev') == 'prod' else a.app.run()
