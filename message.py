from datetime import datetime


class Message:
	__init__( self , text ):
		self._text = text
        self._when = datetime.now() 
        
    timedText(self):
		elapsed_time = datetime.now() - self._when
		if elapsed_time.seconds < 60:
			strTime = "(%d seconds ago)"
		returnValue = self._text
		
		
		
		#returnValue = returnValue +
		return 	
		 
