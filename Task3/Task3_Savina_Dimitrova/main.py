import logging
import psycopg2

class SingletonClass:
  """"Singleton class""""
  _instance = None

  def __new__(cls):
    """"Create instance and check if there are other instances already connected""""
    if cls._instance is None:
      print('Creating the object')
      cls._instance = super(SingletonClass, cls).__new__(cls)
    return cls._instance
  
  
  #still in progress
