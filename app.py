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
    
#Création de la table Player
class Player(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.team_id'), nullable=False)

#Création de la table Transfert
class Transfert(db.Model):
    transfert_id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.player_id'), nullable=False)
    team_origine_id = db.Column(db.Integer, db.ForeignKey('team.team_id'), nullable=False)
    new_team_id = db.Column(db.Integer, db.ForeignKey('team.team_id'), nullable=False)

#Retourne toutes les teams 
@app.route('/get_all_teams' , methods=['GET'])
def get_teams():
    AllTeams = Team.query.all()
    teams = [{'id': team.team_id, 'name': team.name} for team in AllTeams]
    return jsonify(teams)

#Créé une team
@app.route('/create_team' , methods=['POST'])
def create_team():
    # DataTeam = request.get_json()
    # DataTeam2 = request.json.get('name')
    
    team = Team(name=request.json.get('name'))
    db.session.add(team)
    db.session.commit()
    return jsonify({'id': team.team_id})

#Retourne tous les joueurs 
@app.route('/get_all_players' , methods=['GET'])
def get_players():
    AllPlayers = Player.query.all()
    Players = [{'id' : player.player_id , 'team_id': player.team_id, 'name': player.name} for player in AllPlayers]
    return jsonify(Players)

#Créé un joueur
@app.route('/create_player' , methods=['POST'])
def create_player():
    AllTeams = Team.query.all()
    for team in AllTeams :
        if request.json.get('team_id') == team.team_id :
            player = Player(name=request.json.get('name') , team_id=request.json.get('team_id'))
        
    
    db.session.add(player)
    db.session.commit()
    return jsonify({'player_id': player.player_id})


@app.route('/transfert_player' , methods=['POST'])
def Transfert_Player_To_Another_Team():
    AllTeams = Team.query.all()
    AllPlayers = Player.query.all()
    
    for idx , player in enumerate(AllPlayers) :
        if request.json.get('player_id') == player.player_id :
            for team in AllTeams : 
                if request.json.get('new_team_id') == team.team_id:
                    tfert = Transfert(player_id=request.json.get('player_id') ,team_origine_id=Player.query.get(idx+1).team_id ,new_team_id=request.json.get('new_team_id'))
        
    
    db.session.add(tfert)
    db.session.commit()
    return jsonify({'tfert_id': tfert.player_id , 'new_team_id' : tfert.new_team_id})

with app.app_context():
    db.create_all()

app.run()
