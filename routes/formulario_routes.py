from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from controllers.formulario_controller import FormularioController


formulario_routes = Blueprint(
    "formulario_routes",
    __name__
)

@formulario_routes.route(
    "/formularios",
    methods=["POST"]
)
@jwt_required()
def criar_formulario():

    dados = request.get_json()

    if not dados:
        return jsonify({
            "erro": "Nenhum dado foi enviado"
        }), 400

    resultado, status = FormularioController.create_formulario(
        dados
    )

    return jsonify(resultado), status

@formulario_routes.route(
    "/formularios/<int:id>",
    methods=["GET"]
)
@jwt_required()
def buscar_formulario(id):

    resultado, status = FormularioController.get_formulario(
        id
    )

    return jsonify(resultado), status

@formulario_routes.route(
    "/formularios/<int:id>",
    methods=["PUT"]
)
@jwt_required()
def atualizar_formulario(id):

    dados = request.get_json()

    if not dados:
        return jsonify({
            "erro": "Nenhum dado foi enviado"
        }), 400

    resultado, status = FormularioController.update_formulario(
        id,
        dados
    )

    return jsonify(resultado), status

@formulario_routes.route(
    "/formularios/<int:id>",
    methods=["DELETE"]
)
@jwt_required()
def excluir_formulario(id):

    resultado, status = FormularioController.delete_formulario(
        id
    )

    return jsonify(resultado), status