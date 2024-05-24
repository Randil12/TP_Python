from flask import Flask ,request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
app = Flask(__name__)

@app.route('/get_all_teams' , methods=['GET'])
def test():
    return 'Hello, World!'


@app.route('/create_team' , methods=['POST'])
def test2():
    return request.get_json()
app.run()