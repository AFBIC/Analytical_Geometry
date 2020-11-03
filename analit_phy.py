# analitical physics
import jieji

class Force():
  """
  A force.
  Note that the force is stray. It does not do anything to any object.
  It only has a direction and magnitude, and can be binded to an obj.
  """
  def __init__(self,vector):
    """
    _vector is a vactor, which has a direction and magnitude
    """
    self._vector = vector
    
  def increase(self,increase_by)
    self.vector.magnitude += increase_by
  


class Mass_Point():
  
  def __init__(self,mass,x=0,y=0,z=0):
    self.x=x
    self.y=y
    self.z=z
    self.mass=mass
  
  def Apply_Force(self,Force):
    pass
