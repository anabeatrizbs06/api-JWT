from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from controllers.user_controller import UserController


user_routes = Blueprint(
    "user_routes",
    __name__
)

@user_routes.route(
    "/users",
    methods=["POST"]
)
def criar_usuario():

    dados = request.get_json()

    if not dados:
        return jsonify({
            "erro": "Nenhum dado foi enviado"
        }), 400

    resultado, status = UserController.register_user(dados)

    return jsonify(resultado), status

@user_routes.route(
    "/users/login",
    methods=["POST"]
)
def login():

    dados = request.get_json()

    if not dados:
        return jsonify({
            "erro": "Nenhum dado foi enviado"
        }), 400

    resultado, status = UserController.login_user(dados)

    return jsonify(resultado), status

@user_routes.route(
    "/users/<int:id>",
    methods=["GET"]
)
@jwt_required()
def buscar_usuario(id):

    resultado, status = UserController.get_user(id)

    return jsonify(resultado), status

@user_routes.route(
    "/users/<int:id>",
    methods=["PUT"]
)
@jwt_required()
def atualizar_usuario(id):

    dados = request.get_json()

    if not dados:
        return jsonify({
            "erro": "Nenhum dado foi enviado"
        }), 400

    resultado, status = UserController.update_user(
        id,
        dados
    )

    return jsonify(resultado), status

@user_routes.route(
    "/users/<int:id>",
    methods=["DELETE"]
)
@jwt_required()
def excluir_usuario(id):

    resultado, status = UserController.delete_user(id)

    return jsonify(resultado), status