class User:
	
  def __init__(self,name):
    self._name =  name
    self._follows = []
    self._messages = []
  
  def posting( self,  message ): 
    self._messages.insert(0, message)
    
  def following( self,  user_to_follow ): 
    self._follows.append(user_to_follow)    
    
  def reading( self ): 
    strReturn = ""    	  
    for m in self._messages:   
      strReturn += m.timedText()+"\n"
    return strReturn  
  
  def messagesToMix(self):
    cooked_msgs = []	   
    for m in self._messages:   
      ( time, str_text ) = m.msgToMix()
      cooked_msgs.append(  ( time, self._name + " - " + str_text )   )       
    return cooked_msgs	  
    
  def followed_users(self):
	  return list(self._follows)
