# TP_Python
TP python avancée


Pour lancer le programme veuillez suivre les étapes suivantes : 

# Etape 1 : 


git clone https://github.com/Randil12/TP_Python.git

# Etape 2 : 

Installé docker si ce n'est pas déjà fait sinon allez dans le dossier , ouvrez un terminal et lancer la commande suivante : 

docker compose up 

Dans un autre terminal dans le même dossier installer les dépendances suivantes : 
    - flask : pip install flask 
    - flask_sqlalchemy : pip install flask_sqlalchemy
    - psycopg2 : pip install psycopg2

# Etape 3 : 

Lancer le app.py

python app.py ou python3 app.py

# Etape 4 : 

Utiliser postman 

Mettez l'url suivante : http://127.0.0.1:5000/

A la suite de l'url pour utiliser les fonctionnalités =>

# get_all_teams

Donc l'url est : http://127.0.0.1:5000/get_all_teams va permettre de récupérer toutes les équipes

# create_team

Url : http://127.0.0.1:5000/create_team vous allez pouvoir créer votre équipe 

Exemple : 

{
    "name" : "Barcelone"
}

# get_all_teams

url  : http://127.0.0.1:5000/get_all_players va permettre de récupérer tous les joueurs

# create_player 

url : http://127.0.0.1:5000/create_player vous allez pouvoir créer votre joueur 

Exemple : 

{
    "team_id" : 1
    "name" : "Benzema"
}

Attention si la team_id n'existe pas et qu'il vous renvoie une error 500 c'est normal. Il faut mettre un team_id qui existe 

# transfert_player

Ne fonctionne pas pour l'instant , en travaux
















