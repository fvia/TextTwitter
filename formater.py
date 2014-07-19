import time_utils

class Formater:
	
  def timedText(self,message):
      return "%s (%s)" % (  message.text, time_utils.timeAgo( message.when, time_utils.ut_time.now() )  )	
	
	
  def wallFormat( self , messages ):
    """ Sort the messages by time, and builds the return string
    
	messages is a List of Message	
    """
    
    sorted_messages = sorted( messages, key = lambda  m: m.when , reverse = True) 
    
    returnStr = ""
    for msg in sorted_messages: 
      returnStr += msg.user + " - " + self.timedText(msg) +"\n"
      
    return returnStr 


  def readFormat( self , messages ):
    """ builds the return string
    
    messages is a sorted List of Messages	
    """
    
    strReturn = ""    	  
    for msg in messages:   
      strReturn += self.timedText(msg)+"\n"
    return strReturn  


 