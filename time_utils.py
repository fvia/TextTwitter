
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
	  plural = "s" if elapsed_time.seconds > 1 else ""
	  return "%d second%s ago" % ( elapsed_time.seconds , plural)
	else:
	  minutes =  elapsed_time.seconds // 60 
	  plural = "s" if minutes > 1 else ""
	  return "%d minute%s ago" % ( minutes , plural)
    
