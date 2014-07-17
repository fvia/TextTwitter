from user import User
from message import Message


class TextTwitter:
  def __init__( self):
	  self._users = dict()	
	
	
  def processInput( self , strInput  ):
    returnValue = ""  
    if " -> "  in strInput:
      returnValue = self._posts( strInput )
      
    elif " follows " in strInput:
      returnValue = self._follows( strInput )
       
    elif " wall" in strInput:
      returnValue = self._wall( strInput )
      		  
    else:
      returnValue = self._reads( strInput )
        
    return returnValue+"> "
    
    
  def _posts(self,strInput):
    (username,str_message) = strInput.split( " -> ",2) 
    
    if username not in self._users:
      self._users[username] = User(username)
	
    msg = Message( str_message )
    self._users[username].posting( msg )
    
    return ""
    
    
  def _reads(self,strInput):
    if strInput in self._users:
      return self._users[strInput].reading()
    else:		
      return ""  
      
      
  def _follows(self,strInput):
    (username, user_to_follow) = strInput.split( " follows ",2)
        
    if username not in self._users:
      self._users[username] = User(username)
      
    self._users[username].following( user_to_follow )  
    return ""
    
    
  def _wall(self,strInput):
    (username, _ignore) = strInput.split( " wall",2)  
    if username not in self._users:
      return ""
    
    users_to_list = self._users[username].followed_users()
    users_to_list.append( username )
    
    all_messages = []
    for u in users_to_list:
      all_messages += self._users[u].messagesToMix()	     
    
    all_messages = sorted( all_messages, reverse = True) 
    
    returnStr = ""
    for ( ignore, text ) in all_messages: 
      returnStr += text +"\n"
      
    return returnStr 


if __name__ == "__main__":
  twcon = TextTwitter()
  print ("> ",end='')
  while(True):
    strInput = input("")
    print( twcon.processInput(strInput), end='' ) 




