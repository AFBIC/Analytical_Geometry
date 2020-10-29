# Analitical (and also normal) geometry library for python
# The name was just for convenience.
import matplotlib
import math
from matplotlib import pyplot as plt


class Point():
  """2d point on decartian plane"""
  
  def __init__(self , x=0 , y=0):
    self.x_coord = x
    self.y_coord = y
  
  def get_x(self):
    return self.x_coord
  
  def get_y(self):
    return self.y_coord
    
  def __eq__(self , other):
    return (self.x_coord == other.x_coord && self.y_coord == other.y_coord)
  
  def __ne__(self , other):
    return !(self == other)
  
  def distance(self , other):
    """gets distance between 2 points self and other"""
    
    return math.sqrt(((self.x_coord - other.x_coord)**2) + ((self.y_coord - other.y_coord)**2))
  
  def move(self , x , y):
    """moves point x units up and y units down"""
    
    self.x_coord = self.x_coord + x
    self.y_coord = self.y_coord + y
