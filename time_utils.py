import datetime

   

class ut_time:
  """
  as datetime does not allow monkey patching 
  ( related to optimized, c writed classes )
  I wrote this class for not using a Inject library
  """
  __fastenNow = None
  
  @staticmethod 
  def now():
    if ut_time.__fastenNow:
      return ut_time.__fastenNow
    else:	
      return datetime.datetime.now()
  
  
  @staticmethod  
  def fastenNow(  fixedDatetime, deltaMinutes=None,deltaSeconds=None):
    if deltaMinutes:
      fixedDatetime+=datetime.timedelta(0,deltaMinutes*60)
      
    if deltaSeconds:
      fixedDatetime+=datetime.timedelta(0,deltaSeconds)
      
    ut_time.__fastenNow = fixedDatetime   
    		
    		
	

	
	
	
