from controller import Controller

class Parser:
	
    def __init__( self ):
	    self._controller = Controller()
      
	  
    def processInput( self, strInput ):
      
        if " -> "  in strInput:
            return self._posts( strInput )
            
        elif " follows " in strInput:
            return self._follows( strInput )
      
        elif " wall" in strInput:
            return self._wall( strInput )
      
        else:
            return self._reads( strInput )
        
        
    def _posts( self, strInput ):
        (username,str_message) = strInput.split( " -> ", 2 ) 	
        self._controller.posts(username,str_message)
        return ""
    
    
    def _reads( self, strInput ):
        return self._controller.reads( strInput )	  
      
      
    def _follows( self, strInput ):
        (username, user_to_follow) = strInput.split( " follows ", 2 )    
        self._controller.follows( username, user_to_follow ) 
        return ""
    
    
    def _wall( self, strInput ):
        (username, _ignore) = strInput.split( " wall", 2 )      
        return self._controller.wall( username ) 
 
