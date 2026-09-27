
from database.db import db

from models.formulario_model import Formulario
from models.user_model import User


class FormularioController:

    @staticmethod
    def create_formulario(data):

        titulo = data.get("titulo")
        descricao = data.get("descricao")
        usuario_id = data.get("usuario_id")

        if not titulo or not usuario_id:
            return {
                "erro": "Título e usuario_id são obrigatórios"
            }, 400

        usuario = User.query.get(usuario_id)

        if not usuario:
            return {
                "erro": "Usuário não encontrado"
            }, 404

        novo_formulario = Formulario(
            titulo=titulo,
            descricao=descricao,
            usuario_id=usuario_id
        )

        db.session.add(novo_formulario)
        db.session.commit()

        return {
            "mensagem": "Formulário criado com sucesso",
            "formulario": novo_formulario.to_dict()
        }, 201
    @staticmethod
    def get_formulario(formulario_id):

        formulario = Formulario.query.get(
            formulario_id
        )

        if not formulario:
            return {
                "erro": "Formulário não encontrado"
            }, 404

        return formulario.to_dict(), 200
    
    @staticmethod
    def update_formulario(formulario_id, data):

        formulario = Formulario.query.get(
            formulario_id
        )

        if not formulario:
            return {
                "erro": "Formulário não encontrado"
            }, 404

        if "titulo" in data:
            formulario.titulo = data["titulo"]

        if "descricao" in data:
            formulario.descricao = data["descricao"]

        if "usuario_id" in data:

            usuario = User.query.get(
                data["usuario_id"]
            )

            if not usuario:
                return {
                    "erro": "Usuário não encontrado"
                }, 404

            formulario.usuario_id = data["usuario_id"]

        db.session.commit()

        return {
            "mensagem": "Formulário atualizado com sucesso",
            "formulario": formulario.to_dict()
        }, 200

    # DELETE - excluir formulário
    @staticmethod
    def delete_formulario(formulario_id):

        formulario = Formulario.query.get(
            formulario_id
        )

        if not formulario:
            return {
                "erro": "Formulário não encontrado"
            }, 404

        db.session.delete(formulario)
        db.session.commit()

        return {
            "mensagem": "Formulário excluído com sucesso"
        }, 200