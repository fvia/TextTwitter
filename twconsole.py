from user import User
from message import Message


class TwConsole:
  def __init__( self):
	  self._users = dict()	
	
  def processInput( self , strInput  ):
    returnValue = ""  
    if " -> "  in strInput:
      returnValue = self.posting( strInput )
    else:
      returnValue = self.reading( strInput )	  
    return returnValue+"> "
    
  def posting(self,strInput):
    (username,str_message) = strInput.split( " -> ",2)  
    if username not in self._users:
      self._users[username] = User(username)
	
    msg = Message( str_message )
    self._users[username].posting( msg )
    
    return ""
    
  def reading(self,strInput):
    if strInput in self._users:
      return self._users[strInput].reading()
    else:		
      return ""  
  def following(self,strInput):
    print("following")
    return ""
  def wall(self,strInput):
    print("wall")
    return ""


if __name__ == "__main__":
  twcon = TwConsole()
  print ("> ",end='')
  while(True):
    strInput = input("")
    print( twcon.processInput(strInput), end='' ) 




