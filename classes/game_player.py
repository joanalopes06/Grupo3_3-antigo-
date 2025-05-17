"""
@author: António Brito / Carlos Bragança
(2025) objective: class Person
"""
# Class Person - generic version with inheritance
from classes.gclass import Gclass

class Game_player(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''


    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_id','_players_id','_games_id']
    # Class header title
    header = 'Game Player'
    # field description for use in, for example, input form
    des = ['Id','Id Game','Id Player']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, players_id, games_id):
        super().__init__()
        # Object attributes
        id = Game_player.get_id(id)
        self._id = id
        self._games_id=games_id
        self._players_id=players_id
        
        Game_player.obj[id] = self
        # Add the id to the list of object ids
        Game_player.lst.append(id)
    # id property getter method
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id
   
    @property
    def games_id(self):
        return self._games_id
    @games_id.setter
    def id_game(self, games_id):
        self._games_id = games_id
        
    @property
    def players_id(self):
        return self._players_id
    @players_id.setter
    def id_player(self, players_id):
        self._players_id = players_id
    