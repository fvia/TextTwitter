from testabletime import TestableTime

from timeago import timeAgo 

class Formater:
	
  def timedText(self,message):
      return "%s (%s)" % (  message.text, timeAgo( message.when, TestableTime.now() )  )	
	
	
  def wallFormat( self , messages ):
    """ Sort the messages by time, and builds the return string for the wall command
    
	messages is a List of Message	
    """
    
    sorted_messages = sorted( messages, key = lambda  m: m.when , reverse = True) 
    
    returnStr = ""
    for msg in sorted_messages: 
      returnStr += msg.user + " - " + self.timedText(msg) +"\n"
      
    return returnStr 


  def readFormat( self , messages ):
    """ Sort the messages by time and builds the return string for the read command
    
    messages is List of Messages	
    """
    sorted_messages = sorted( messages, key = lambda  m: m.when , reverse = True) 
    
    strReturn = ""    	  
    for msg in sorted_messages:   
      strReturn += self.timedText(msg)+"\n"
      
    return strReturn  


 
