
class TwCon:
  def write( self , strInput  ):
    returnValue = ""  
    if " -> "  in strInput:
      returnValue = self.posting( strInput )
    else:
      returnValue = self.reading( strInput )	  
    return returnValue+"> "
    
  def posting(self,strInput):
    print("posting")
    return ""
  def reading(self,strInput):
    print("reading")	
    return ""  
  def following(self,strInput):
    print("following")
    return ""
  def wall(self,strInput):
    print("wall")
    return ""


if __name__ == "__main__":
  twcon = TwCon()
  print ("> ",end='')
  while(True):
    strInput = input("")
    print( twcon.write(strInput), end='' ) 




