import time_utils


class Message:
	
  def __init__( self , text):
    self._text = text
    self._when = time_utils.ut_time.now()
        
  def timedText(self):
    return "%s (%s)" % (  self._text, time_utils.timeAgo( self._when, time_utils.ut_time.now() )  )	
		 
