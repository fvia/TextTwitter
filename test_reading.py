import unittest
from datetime import datetime

from time_utils import ut_time
from texttwitter import TextTwitter


class testReading(unittest.TestCase):

  def setUp(self ):  
    self.twc = TextTwitter()

  def test_reading_alice(self):
    time_read_alice =  datetime.now() 
    ut_time.fastenNow( time_read_alice,deltaMinutes= -5)  
    self.twc.processInput( "Alice -> I love the weather today") 
      
    ut_time.fastenNow( time_read_alice )  
    self.assertEqual( 
	  self.twc.processInput( "Alice" ), 
"""\
I love the weather today (5 minutes ago)
> """  
    )     

  def test_reading_bob(self):
    time_read_bob =  datetime.now() 
    
    ut_time.fastenNow( time_read_bob , deltaMinutes=-2)
    self.twc.processInput( "Bob -> Damn! We lost!" ) 
    
    ut_time.fastenNow( time_read_bob , deltaMinutes=-1)
    self.twc.processInput( "Bob -> Good game though." )
   
    ut_time.fastenNow(time_read_bob)  
    self.assertEqual( 
		self.twc.processInput( "Bob" ), 
"""\
Good game though. (1 minute ago)
Damn! We lost! (2 minutes ago)
> """  
    )     

