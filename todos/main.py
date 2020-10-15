import os

import jwt
from flask import request, Flask
from jwt import InvalidSignatureError

import db
from todo import Todo

app = Flask(__name__)
app.config['TESTING'] = True
app.config['DEVELOPMENT'] = False
app.config['DEBUG'] = True

key = os.environ['SECRET']


def create_todo(description: str):
    todo = Todo(description)
    db.session.add(todo)
    db.session.commit()


@app.route('/todo', methods=['POST'])
def todo():
    authorization = request.headers['Authorization']

    try:
        decoded = jwt.decode(authorization, key, verify=True)
    except InvalidSignatureError:
        return '401'

    if not decoded['authorized']:
        return '401'

    data = request.json
    create_todo(data['todo'])

    return '201'


if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)
    app.run(port=9090, debug=True, host="0.0.0.0")
