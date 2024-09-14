from flask import Flask
from routes import roulette_bp
from config.config_bd import Config
from models.database_models import db

def create_app():
    app = Flask(__name__)
    app.register_blueprint(roulette_bp)
    app.config.from_object(Config)
    db.init_app(app)
    return app 

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", debug=True)
