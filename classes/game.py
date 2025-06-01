"""
@author: António Brito / Carlos Bragança
(2025) objective: class Person
"""
# Class Person - generic version with inheritance
from classes.gclass import Gclass

class Game(Gclass):

    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''

    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_id','_genre','_title', '_release_date','_tournaments_id']
    # Class header title
    header = 'Game'
    # field description for use in, for example, input form
    des = ['Id','Genre','Title', 'Release Date','Id Tournament']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, genre, title, release_date, tournaments_id):
        super().__init__()
        # Object attributes
        id = Game.get_id(id)
        self._id= id
        self._genre = genre
        self._title = title
        self._release_date = release_date
        self._tournaments_id = tournaments_id
        # Add the new object to the dictionary of objects
      
        Game.obj[id] = self
        # Add the id to the list of object ids
        Game.lst.append(id)
    # id property getter method
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id
    # property getter method
    @property
    def genre(self):
        return self._genre
    @genre.setter
    def genre(self, genre):
        self._genre = genre
    #property getter method
    @property
    def title(self):
        return self._title
    # property setter method
    @title.setter
    def title(self, title):
        self._title = title
    #property getter method
    
    #property getter method
    @property
    def releasedate(self):
        return self._release_date
    # property setter method
    @releasedate.setter
    def releasedate(self, release_date):
        self._release_date = release_date
    @property
    def tournaments_id(self):
        return self._tournaments_id
    @tournaments_id.setter
    def tournaments_id(self, tournaments_id):
        self._tournaments_id = tournaments_id
