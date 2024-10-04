from flask import Blueprint, request, jsonify
from services.roullete_logic import Roleta
from models.models import User, Betting_House
from models.database_models import Usuario, db

user_bp = Blueprint('roulette', __name__)
 
@user_bp.route("/user/register", methods=["POST"])
def register_cadastro():
    """
    End-point para cadastrar um novo usuário.

    Parâmetros:
        username (string): nome de usuário.
        email (string): endereço de e-mail.
        senha (string): senha do usuário.

    Retorna:
        JSON com status 201 e mensagem de sucesso se o cadastro for realizado com sucesso.
        JSON com status 400 e mensagem de erro se os parâmetros forem inválidos.
        JSON com status 409 e mensagem de erro se o usuário já existir.
    """
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    senha = data.get("senha")

    # Verifica se todos os parâmetros foram passados
    if not username or not email or not senha:
        return jsonify({"erro": "parâmetros não passados"}), 400

    # Verifica se o usuário já existe
    usuario_existente = Usuario.query.filter_by(email=email).first()
    if usuario_existente:
        return jsonify({"erro": "usuário já existente"}), 409

    # Cria um novo usuário
    new_user = Usuario(id = 5, username=username, email=email, senha=senha, saldo = 0.0)
    db.session.add(new_user)
    db.session.commit()
    
    # Retorna mensagem de sucesso
    return jsonify({"mensagem": "usuário adicionado com sucesso"}), 201


# @user_bp("/user/recarregar/", methods=["POST"])
# def recarregar_saldo():
#     data = request.get_json()
#     username = data.get("username")
#     saldo = data.get("saldo")

#     usuario_existente = Usuario.query.filter_by(username=username).first()
#     if usuario_existente:
#         add_saldo = Usuario(username=username, saldo=saldo)
#         User.add_saldo(saldo)

#         db.session.add(add_saldo)
#         db.session.commit()
#         return jsonify({"message": "Saldo recarregado","saldo": User.saldo})
#     else:
#         return jsonify({"erro": "Usuário nao encontrado"}), 404
    
