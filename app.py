from flask import Flask

from flask_jwt_extended import JWTManager

from database.db import db

from routes.user_routes import user_routes
from routes.formulario_routes import formulario_routes


app = Flask(__name__)

app.config.from_pyfile("config.py")


db.init_app(app)

jwt = JWTManager(app)


with app.app_context():
    db.create_all()

app.register_blueprint(user_routes)

app.register_blueprint(formulario_routes)


if __name__ == "__main__":
    app.run(debug=True)