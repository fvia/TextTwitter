class User:
	
  def __init__(self,name):
    self._name =  name
    self._follows = []
    self._messages = []
  
  
  def posting( self,  message ): 
    self._messages.insert(0, message)
    
    
  def following( self,  user_to_follow ): 
    self._follows.append(user_to_follow)    

    
  def messages( self ):
    return list( self._messages)	  
         
    
  def followed_users(self):
	  return list(self._follows)
