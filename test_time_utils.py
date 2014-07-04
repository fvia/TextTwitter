import unittest
from datetime import datetime

from time_utils import timeAgo

class testUtils( unittest.TestCase ):
	def test_timeAgo(self):
		self.assertEqual(  
		     timeAgo(  datetime(2014,7,4,12,0,0) ,  datetime(2014,7,4,12,0,1)   ),
		     "1 second ago"
		) 
		self.assertEqual(  
		     timeAgo(  datetime(2014,7,4,12,0,0) ,  datetime(2014,7,4,12,0,12)   ),
		     "12 seconds ago"
		) 
		self.assertEqual(  
		     timeAgo(  datetime(2014,7,4,12,0,0) ,  datetime(2014,7,4,12,1,12)   ),
		     "1 minute ago"
		) 
		self.assertEqual(  
		     timeAgo(  datetime(2014,7,4,12,0,0) ,  datetime(2014,7,4,12,4,0)   ),
		     "4 minutes ago"
		) 









