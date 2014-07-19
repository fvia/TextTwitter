from user import User
from message import Message
from formater import Formater 
from storage import Storage
from testabletime import TestableTime


class TextTwitter:
	
  def __init__( self):
	  self._storage = Storage()
	  
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
	
    msg = Message( TestableTime.now(), str_message, username )
    self._storage.saveMessage(msg)
    
    return ""
    
    
  def _reads(self,strInput):
    messages = self._storage.getMessages([strInput])
    fmt= Formater()
    return fmt.readFormat(messages)
      
      
  def _follows(self,strInput):
    (username, user_to_follow) = strInput.split( " follows ",2)
     
    user = self._storage.loadCreateUser( username )    
    user.following( user_to_follow )  
    return ""
    
    
  def _wall(self,strInput):
    (username, _ignore) = strInput.split( " wall",2)  
    
    user = self._storage.loadUser( username )
    if not user:
      return ""
    
    users_to_list = user.followed_users()
    users_to_list.append( username )
  
    all_messages = self._storage.getMessages( users_to_list )
    
    formater = Formater()
    return formater.wallFormat( all_messages)  
 

if __name__ == "__main__":
  twcon = TextTwitter()
  print ("> ",end='')
  while(True):
    strInput = input("")
    print( twcon.processInput(strInput), end='' ) 




