# Analitical (and also normal) geometry library for python
# The name was just for convenience.
class Point():
  """2d point on decartian plane"""
  
  def __init__(self , x=0 , y=0):
    self.x_coord = x
    self.y_coord = y
  
  def get_x(self):
    return self.x_coord
  
  def get_y(self):
    return self.y_coord
    
  
