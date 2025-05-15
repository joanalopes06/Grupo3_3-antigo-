"""
@author: António Brito / Carlos Bragança
(2025) objective: class Person
"""
# Class Person - generic version with inheritance
from classes.gclass import Gclass

class Player(Gclass):
<<<<<<< HEAD
=======
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''

>>>>>>> origin/master
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_players_id','_username','_level','_join_date', '_score']
    # Class header title
    header = 'Player'
    # field description for use in, for example, input form
    des = ['Id','Username','Level','Join date', 'Score']
    # Constructor: Called when an object is instantiated
    def __init__(self, players_id, username, level, join_date, score):
        super().__init__()
        # Object attributes
        id = Player.get_id(players_id)
        self._players_id = players_id
        self._username = username
        self._level = level
        self._join_date= join_date
        self._score = score
        # Add the new object to the dictionary of objects
        Player.obj[players_id] = self
        # Add the id to the list of object ids
        Player.lst.append(players_id)
    # id property getter method
    @property
    def players_id(self):
        return self._players_id
    @players_id.setter
    def id(self, players_id):
        self._players_id = players_id
    # property getter method
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username):
        self._username = username
    #property getter method
    @property
    def level(self):
        return self._level
    # property setter method
    @level.setter
    def level(self, level):
        self._level = level
    #property getter method
    @property
    def join_date(self):
        return self._join_date
    #property setter method
    @join_date.setter
    def joindate(self, join_date):
        self._join_date = join_date
    #property getter method
    @property
    def score(self):
        return self._score
    # property setter method
    @score.setter
    def score(self, score):
        self._score = score
    