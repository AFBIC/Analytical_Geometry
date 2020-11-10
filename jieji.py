# Analitical (and also normal) geometry library for python
# (c) Zaiyou Xue, 2020
# The name was just for convenience.
import matplotlib
import math
import sympy
from matplotlib import pyplot as plt

"""
Type traits helper funcs with C++-like names
"""
def Is_integral(arg):
	return True if type(arg) == int else False

def Is_arithmetic(arg):
	flag = (type(arg) == int or type(arg) == float)
	return flag

def swap(arguno , argdos):
    """helper function to swap the value of two variables"""
    temp = arguno
    arguno = argdos
    argdos = temp

def with_symbol(a):
	assert(Is_arithmetic(a))
	if(a == 0):
		return "0"
	elif(a < 0):
		return f"-{a}"
	else:
		return f"+{a}"
		

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
    
    def __init__(self , x , y):
        self.x = x
	    self.y = y
    
    def __add__(self , other):
	    return Math_Vector ( self.x + other.x , self.y + other.y )
	
	def __neg__(self):
		return Math_Vector (-self.x , -self.y)
	
	def __pos__(self):
		return self
	
	def __sub__(self , other):
		return -self + other
	
	def __mul__(self , other):
		if (Is_arithmetic(other)):
			return Math_Vector ( self.x * other , self.y * other )

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
		xsymb = sympy.Symbol("x")
		ysymb = sympy.Symbol("y")
		expr = (xsymb + self.center.x_coord) ** 2 + (ysymb + self.center.y_coord) ** 2 - self.radius ** 2
		return expr
    
	def __str__(self):
		return self.Expr()

def create_line (puntoa , puntob):
	return Line(puntoa , puntob)

def main():
	pass

if __name__ == '__main__':
	main()

