import datetime

def timeAgo( time0,time1 ):
	"""
	return diff time formated as:
	  1 second ago 
	  5 seconds ago
	  1 minute ago
	  68 minutes ago
	"""
	elapsed_time = time1 - time0
	if elapsed_time.seconds < 60:
	  plural = "s" if elapsed_time.seconds != 1 else ""
	  return "%d second%s ago" % ( elapsed_time.seconds , plural)
	  
	else:
	  minutes =  elapsed_time.seconds // 60 
	  plural = "s" if minutes != 1 else ""
	  return "%d minute%s ago" % ( minutes , plural)
    

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
    		
    		
	

	
	
	
