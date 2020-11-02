# Analitical (and also normal) geometry library for python
# The name was just for convenience.
import matplotlib
import math
from matplotlib import pyplot as plt

def swap(arguno , argdos):
  temp = arguno
  arguno = argdos
  argdos = temp



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
    return (self.x_coord == other.x_coord and self.y_coord == other.y_coord)
  
  def __ne__(self , other):
    return not (self == other)
  
  def distance(self , other):
    """gets distance between 2 points self and other"""
    
    return math.sqrt(((self.x_coord - other.x_coord)**2) + ((self.y_coord - other.y_coord)**2))
  
  def move(self , x=0 , y=0):
    """moves point x units up and y units down"""
    
    self.x_coord = self.x_coord + x
    self.y_coord = self.y_coord + y
  
  def plot(self):
    """This should be able to produce sth on a canvas but I don't know if it will work"""
    plt.scatter(self.x_coord,self.y_coord)

class Line_Segment():
  """2d line segement defined by 2 points"""
  
  def __init__(self , alpha , beta):
    """Initializers should be points."""
    if (alpha == beta):
      raise ValueError("The two points must be different.")
    self.p1 = alpha
    self.p2 = beta
    
  def __eq__(self , otro):
    return self.p1 == otro.p1 and self.p2 == otro.p2
  
  def __ne__(self , otro):
    return not (self == otro)
  
  def slope(self):
    if (self.p1.x_coord == self.p2.x_coord):
      return float("inf")
    else:
     return (self.p1.get_y() - self.p2.get_y()) / (self.p1.get_x() - self.p2.get_x())
  
  def is_parallel(self , otro):
    """sees if self and otro are parallel lines"""
    return self.slope() == otro.slope()
  
  def lenth(self):
    """returns lenth of line"""
    return self.p1.distance(self.p2)
  
  def plot(self):
    x = [self.p1.x_coord , self.p2.x_coord]
    y = [self.p2.y_coord , self.p2.y_coord]
    plt.plot(x,y)

class Math_Vector():
  """2d math vector"""
  
  def __init__(self , radian , mag):
  	"""radian represents the angle in the polar plane;
  	   mag is the magnitude"""
  	
class Circle():
  """a circle defined by the center and radius"""
  
  def __init__(self , center , radius):
    self.center = center
    self.radius = radius
  
  def __eq__(self , otro):
    """
    note: this only checks if the two are equal in normal geometry terms.
    It does not checkif the centers are on the same point.
    If you wnat checking against the center, use All_Equal.
    """
    return self.radius == otro.radius
  
  def __ne__(self , otro):
    return not self == otro
  
  def All_Equal(self , otro):
    return self == otro and self.center == otro.center
  
  def Expr(self):
    absx = math.abs(self.center.x_coord)
    absy = math.abs(self.center.y_coord)
    if (self.center.x_coord == 0):
      if (self.center.y_coord == 0):
        return ("x ** 2 + y ** 2 = " + str(self.radius) + " ** 2")
      elif (self.center.y_coord > 0):
        return ("x ** 2 + (y - " + str(absy) + ") ** 2 = " + str(self.radius) + " ** 2")
      else: 
        return ("x ** 2 + (y + " + str(absy) + ") ** 2 = " + str(self.radius) + " ** 2")
    elif (self.center.x_coord > 0):
      if (self.center.y_coord == 0):
        return ("(x - " + str(absx) + ") ** 2 + y ** 2 = " + str(self.radius) + " ** 2")
      elif (self.center.y_coord > 0):
        return ("(x - " + str(absx) + "(y - " + str(absy) + ") ** 2 = " + str(self.radius) + " ** 2")
      elif (self.center.y_coord < 0):
        return ("(x - " + str(absx) + "(y + " + str(absy) + ") ** 2 = " + str(self.radius) + " ** 2")
    elif (self.center.x_coord < 0):
      if (self.center.y_coord == 0):
        return ("(x + " + str(absx) + ") ** 2 + y ** 2 = " + str(self.radius) + " ** 2")
      elif (self.center.y_coord > 0):
        return ("(x + " + str(absx) + "(y - " + str(absy) + ") ** 2 = " + str(self.radius) + " ** 2")
      elif (self.center.y_coord < 0):
        return ("(x + " + str(absx) + "(y + " + str(absy) + ") ** 2 = " + str(self.radius) + " ** 2")
  
  def __str__(self):
    return self.Expr()

def create_line (puntoa , puntob):
  return Line(puntoa , puntob)

