from controller import Controller


class TextTwitter:
	
  def __init__( self):
	  self._controller = Controller()
	  
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
	
    self._controller.posts(username,str_message)
    return ""
    
    
  def _reads(self,strInput):
    return self._controller.reads( strInput )	  
      
      
  def _follows(self,strInput):
    (username, user_to_follow) = strInput.split( " follows ",2)
    
    self._controller.follows( username, user_to_follow ) 
    return ""
    
    
  def _wall(self,strInput):
    (username, _ignore) = strInput.split( " wall",2)  
    
    return self._controller.wall( username ) 
 

if __name__ == "__main__":
  twcon = TextTwitter()
  print ("> ",end='')
  while(True):
    strInput = input("")
    print( twcon.processInput(strInput), end='' ) 




