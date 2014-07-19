import datetime
   

class TestableTime:
  """ A time class for testing 
  """
  __fastenNow = None
  
  @staticmethod 
  def now():
    if TestableTime.__fastenNow:
      return TestableTime.__fastenNow
    else:	
      return datetime.datetime.now()
  
  
  @staticmethod  
  def fastenNow(  fixedDatetime, deltaMinutes=None,deltaSeconds=None):
    if deltaMinutes:
      fixedDatetime+=datetime.timedelta(0,deltaMinutes*60)
      
    if deltaSeconds:
      fixedDatetime+=datetime.timedelta(0,deltaSeconds)
      
    TestableTime.__fastenNow = fixedDatetime   
    		
    		
	

	
	
	
