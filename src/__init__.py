from flask import Flask
from .routes import AuthRoutes, CompaniesRoutes, ImagenRoutes, CloudinaryRoutes

app = Flask(__name__)

def init_app(config):
    # Configuration
    app.config.from_object(config)

    # Register Blueprints
    app.register_blueprint(AuthRoutes.main, url_prefix='/auth')
    app.register_blueprint(CompaniesRoutes.main, url_prefix='/companies')
    app.register_blueprint(ImagenRoutes.main, url_prefix='/upload')
    app.register_blueprint(CloudinaryRoutes.cloudinary_blueprint, url_prefix='/cloudinary')
    

    return app
