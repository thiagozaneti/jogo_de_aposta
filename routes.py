from flask import Blueprint, request, jsonify
from services.roullete_logic import Roleta
from models.models import User, Betting_House
from models.database_models import Usuario, db


roulette_bp = Blueprint('roulette', __name__)
 

@roulette_bp.route("/roleta/play/<usuario>", methods=["POST"])
def play_roulette(usuario):
    user_data = request.get_json()
    if not user_data or 'rodadas' not in user_data:
        return jsonify({"error": "Dados inválidos ou incompletos"}), 400

    user_db = Usuario.query.filter_by(username = usuario).first()       
    if not user_db:
        return jsonify({"error": "Usuário não encontrado"}), 404
    
    if user_db.saldo <= 0 :
        return jsonify({"error": "Saldo insuficiente para jogar a roleta"}), 400

    casa = Betting_House(saldo=1000)
    user = User(user_db_instance=user_db, rodadas=user_data['rodadas'], betting_house=casa)
    roleta = Roleta(usuario=user, casa=casa)
    roleta.rolar_roleta(rodadas=user.rodadas)

    return jsonify({
        "rodadas": user.rodadas,
        "saldo_final": user.saldo,
        "ganhos": user.ganhos,
        "derrotas": user.derrotas
    })



@roulette_bp.route("/roleta/register", methods=["POST"])
def register_cadastro():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    senha = data.get("senha")

    if not username or not email or not senha:
        return jsonify({"erro": "parâmetros não passados"}), 400

    usuario_existente = Usuario.query.filter_by(email=email).first()
    if usuario_existente:
        return jsonify({"erro": "usuário já existente"}), 409

    new_user = Usuario(id = 3, username=username, email=email, senha=senha, saldo = 0.0)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"mensagem": "usuário adicionado com sucesso"}), 201

# @app.route("/test") def test_route(): response = app.test_client().post('/roleta/register/cadastro', json={ "username": "testuser", "email": "test@example.com", "senha": "password" }) return response.data