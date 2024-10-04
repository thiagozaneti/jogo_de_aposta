from flask import Blueprint, request, jsonify
from models.models import User, Betting_House
from models.database_models import Usuario, db

user_bp = Blueprint('user', __name__)

@user_bp.route("/register", methods=["POST"])
def register_cadastro():
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

    # Cria um novo usuário (id será gerado automaticamente pelo PostgreSQL)
    new_user = Usuario(username=username, email=email, senha=senha)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"mensagem": "usuário adicionado com sucesso"}), 201

@user_bp.route("/recarregar", methods=["POST"])
def recarregar_saldo():
    data = request.get_json()
    username = data.get("username")
    saldo = data.get("saldo")
    try:
        saldo_add = float(saldo)
    except (ValueError, TypeError):
        return jsonify({"erro": "Valor de saldo inválido"}), 400

    usuario_existente = Usuario.query.filter_by(username=username).first()
    if usuario_existente:
        # Atualiza o saldo diretamente no objeto existente
        usuario_existente.saldo += saldo_add
        db.session.commit()
        
        return jsonify({"message": "Saldo recarregado", "saldo": usuario_existente.saldo}), 200
    else:
        return jsonify({"erro": "Usuário não encontrado"}), 404
    
@user_bp.route("/usuarios", methods=["GET"])
def get_users():
    users = Usuario.query.all()
    users_dict = [user.to_dict() for user in users]
    return jsonify(users_dict)
