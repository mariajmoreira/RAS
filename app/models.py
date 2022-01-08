from . import db
from flask_login import UserMixin
from enum import IntEnum,auto

class Result(IntEnum):
    WIN = auto()
    DRAW = auto()
    DEFEAT = auto()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(120))
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    balance = db.Column(db.Float)

    def __init__(self, email, password, first_name, last_name):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0.0

class Football_team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    country = db.Column(db.String(60))

    def __init__(self, name, country):
        self.name = name
        self.country = country

class Tennis_player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    country = db.Column(db.String(60))

    def __init__(self, name, country):
        self.name = name
        self.country = country

class Odd(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    win = db.Column(db.Float)
    draw = db.Column(db.Float, nullable=True)
    defeat = db.Column(db.Float)

class Football_game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True))
    team1 = db.Column(db.Integer,db.ForeignKey(Football_team.id))
    team2 = db.Column(db.Integer,db.ForeignKey(Football_team.id))
    odd = db.Column(db.Integer, db.ForeignKey(Odd.id))
    result = db.Column(db.Integer, nullable=True)


    def __init__(self, date, team1, team2, odd, winner=None):
        self.date = date
        self.team1 = team1
        self.team2 = team2
        self.odd = odd
        if winner:
            self.winer = winner

class Tennis_game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True))
    player1 = db.Column(db.Integer,db.ForeignKey(Tennis_player.id))
    player2 = db.Column(db.Integer,db.ForeignKey(Tennis_player.id))
    odd = db.Column(db.Integer, db.ForeignKey(Odd.id))
    result = db.Column(db.Integer, nullable=True)


    def __init__(self, date, player1, player2, odd, winner=None):
        self.date = date
        self.player1 = player1
        self.player2 = player2
        self.odd = odd
        if winner:
            self.winer = winner

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(300))
    user_id = db.Column(db.Integer,db.ForeignKey(User.id))

    def __init__(self,message,user_id):
        self.message = message
        self.user_id = user_id

class Bet_Tennis_game(db.Model):
    Tennis_game_id = db.Column(db.Integer, db.ForeignKey(Tennis_game.id), primary_key=True)
    Betted = db.Column(db.Integer)

    def __init__(self, Tennis_game, Betted):
        self.Tennis_game_id = Tennis_game
        self.Betted = Betted

class Bet_Football_game(db.Model):
    Football_game_id = db.Column(db.Integer, db.ForeignKey(Football_game.id), primary_key=True)
    Betted = db.Column(db.Integer)

    def __init__(self, Football_game, Betted):
        self.Football_game_id = Football_game
        self.Betted = Betted

class CombinedBet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float)
    user_id = db.Column(db.Integer,db.ForeignKey(User.id))
    date = db.Column(db.DateTime(timezone=True))

    def __init__(self, value, user_id, date):
        self.value = value
        self.user_id = user_id
        self.date = date

class SimpleBet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float)
    user_id = db.Column(db.Integer,db.ForeignKey(User.id))
    date = db.Column(db.DateTime(timezone=True))
    football_game_id = db.Column(db.Integer,db.ForeignKey(Football_game.id))
    tennis_game_id = db.Column(db.Integer,db.ForeignKey(Tennis_game.id))
    betted = db.Column(db.Integer)

    def __init__(self, value, user_id, date, football_game_id, tennis_game_id, betted):
        self.value = value
        self.user_id = user_id
        self.date = date
        self.football_game_id = football_game_id
        self.tennis_game_id = tennis_game_id
        self.betted = betted

