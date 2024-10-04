from flask import Flask
from routes.roulette_routes import roulette_bp
from routes.user_routes import user_bp
from config.config_bd import Config
from models.database_models import db

def create_app():
    """
    Fun o que cria uma aplica o Flask e registra as blueprint.
    
    Retorna:
        Uma instancia da classe Flask.
    """
    app = Flask(__name__)
    app.register_blueprint(roulette_bp,url_prefix="/roleta", name= "roulette")
    app.register_blueprint(user_bp, url_prefix="/user", name="user")
    app.config.from_object(Config)
    db.init_app(app)
    return app 

if __name__ == "__main__":
    app = create_app()
    # with app.app_context:
    #     print("Mostrando todas as rotas")
    #     for rule in app.url_map.iter_rules():
    #         print(f"Endpoint: {rule.endpoint}, Route: {rule}")
    app.run(host="0.0.0.0", debug=True, port=8000)

