import flask
import flask_cors
from flask import jsonify
from flask import request

import auxiliar_functions
from database.mongo import Mongo


def create_app():
    app = flask.Flask(__name__)
    return app


app = create_app()

flask_cors.CORS(app)

@app.route('/api/login', methods=['GET', 'POST'])
def api_login():
    if request.method == 'GET':
        return jsonify({"user": "your_user", "psw": "password"})

    elif request.method == 'POST':
        post_data = request.json
        try:
            print(post_data['user'])
            print(post_data['psw'])
            return jsonify({"message": "printed"})
        except:
            return jsonify({"message": "error in request"})


@app.route('/api/cadastrar', methods=['GET', 'POST'])
def api_cadastrar():
    if request.method == 'GET':
        return jsonify({"user": "your_user", "psw": "password"})

    elif request.method == 'POST':
        post_data = request.json

        if auxiliar_functions.verify_user_dict(post_data):
            db = Mongo("admin", "project")

            db.insert_one(post_data)

            return jsonify({"message": "Cadastrado"})

        else:
            return jsonify({"message": "error in request"})

@app.route('/api/updatecad', methods=['GET', 'POST'])
def api_update_cadastro():
    if request.method == 'GET':
        return jsonify({"user": "your_user"})

    elif request.method == 'POST':
        post_data = request.json

        if auxiliar_functions.verify_user_only(post_data):
            db = Mongo("admin", "project")

            db.update({"user":post_data['user']},{"psw":"54321"})

            return jsonify({"message": "Cadastro atualizado"})

        else:
            return jsonify({"message": "error in request"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False, port=5005)
