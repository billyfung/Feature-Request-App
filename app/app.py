import logging 

from flask import Flask
from config import DefaultConfig
from flask_sqlalchemy import SQLAlchemy

INSTANCE_FOLDER_PATH = '/opt/app/private'

def create_app(config=None, app_name=None):
    if app_name is None:
        app_name = DefaultConfig.PROJECT

    app = Flask(app_name, 
        instance_path=INSTANCE_FOLDER_PATH,
        instance_relative_config=True
    )
    # configure_app(app, config)
    # configure_db(app)
    # configure_blueprints(app)
    # configure_hook(app)
    # configure_logging(app)
    # configure_error_handlers(app)

    return app


def configure_app(app, config=None):
    app.config.from_object(DefaultConfig)

    app.config.from_pyfile('production.cfg', silent=True)

    if config:
        app.config.from_object(config)


def configure_extensions(app):
    db = SQLAlchemy()
    db.init_app(app)


def configure_blueprints(app):
    from api import api
    from frontend.views import frontend

    for bp in [api, frontend]:
        app.register_blueprint(bp)


def configure_hook(app):
    app.register_error_handler(
        ApiException, lambda err: err.to_result())


def configure_error_handlers(app):
    @app.errorhandler(404)
    def page_not_found(error):
        app.logger.error(error)
        return render_template("errors/404.html", error=error), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        app.logger.error(error)
        return render_template("errors/500.html", error=error), 500

    @app.errorhandler(Exception)
    def unhandled_exception(error):
        app.logger.exception(error)
        return render_template("errors/500.html", error=error), 500


# TODO SMTP logging?
def configure_logging(app):
    if app.debug or app.testing:
        # Skip debug and test mode. Just check standard output.
        return

    # In production mode, add log handler to sys.stderr.
    app.logger.setLevel(logging.INFO)

    log = logging.StreamHandler()
    log.setLevel(logging.INFO)
    log.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')
    )
    app.logger.addHandler(log)