from flask import Flask ,request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError


app = Flask(__name__)
#Config de SQLAlchymy 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost/TP'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#ça c'est pour créer une table Team
class Team(db.Model):
    team_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60) , nullable=False)
    

class Player(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.team_id'), nullable=False)

#Retourne toutes les teams 
@app.route('/get_all_teams' , methods=['GET'])
def get_teams():
    AllTeams = Team.query.all()
    return jsonify([{'id': team.id, 'name': team.name} for team in AllTeams])

#Créé une team
@app.route('/create_team' , methods=['POST'])
def create_team():
    # DataTeam = request.get_json()
    # DataTeam2 = request.json.get('name')
    
    team = Team(name=request.json.get('name'))
    db.session.add(team)
    db.session.commit()
    return jsonify({'id': team.team_id})


with app.app_context():
    db.create_all()

app.run()
