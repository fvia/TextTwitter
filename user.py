class User:
	
  def __init__(self,name):
    self._name =  name
    self._follows = []
    self._messages = []
  
  def posting( self,  message ): 
    self._messages.append( message)
    
  def reading( self ): 
    strReturn = ""    	  
    for m in self._messages:   
      strReturn += m.timedText()+"\n"
    return strReturn  
