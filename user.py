class User:
	
  def __init__(self,name):
    self._name =  name
    self._follows = []
  
      
  def following( self,  user_to_follow ):	   
    self._follows.append(user_to_follow)    
         
    
  def followed_users(self):
	  return list(self._follows)
