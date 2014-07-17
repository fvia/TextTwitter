import unittest
from datetime import datetime

from time_utils import ut_time
from texttwitter import TextTwitter


class testPosting( unittest.TestCase ):

  def test_post_must_return_prompt(self):
    twc = TextTwitter()
    self.assertEqual( 
		twc.processInput( "Alice -> I love the weather today"   ), 
        "> "  
    )     
    self.assertEqual( 
		twc.processInput( "Bob -> Damn! We lost!" ), 
        "> "  
    )     
    self.assertEqual( 
	twc.processInput( "Bob -> Good game though." ), 
        "> "  
    )     


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

class testFollowing(unittest.TestCase):
  def setUp(self ):  
    self.twc = TextTwitter()
    self.time_test =  datetime.now()
    
    ut_time.fastenNow( self.time_test ,deltaMinutes = -2)  
    self.twc.processInput( "Bob -> Damn! We lost!" ) 
    
    ut_time.fastenNow( self.time_test , deltaMinutes = -1)
    self.twc.processInput( "Bob -> Good game though." )
    
    ut_time.fastenNow( self.time_test , deltaMinutes= -5)  
    self.twc.processInput( "Alice -> I love the weather today" ) 
	
    ut_time.fastenNow( self.time_test , deltaSeconds= -2)  
    self.twc.processInput( "Charlie -> I'm in New York today! Anyone want to have a coffee?" )
    self.twc.processInput( "Charlie follows Alice")
    
	
  def test_follow_Alice( self):
    ut_time.fastenNow(self.time_test) 	  
    self.assertEqual( 
      self.twc.processInput( "Charlie wall" ), 
"""\
Charlie - I'm in New York today! Anyone want to have a coffee? (2 seconds ago)
Alice - I love the weather today (5 minutes ago)
> """
    )     


  def test_follow_Bob( self):
    self.twc.processInput( "Charlie follows Bob")  
    ut_time.fastenNow(self.time_test) 	  
    self.assertEqual( 
      self.twc.processInput( "Charlie wall" ), 
"""\
Charlie - I'm in New York today! Anyone want to have a coffee? (2 seconds ago)
Bob - Good game though. (1 minute ago)
Bob - Damn! We lost! (2 minutes ago)
Alice - I love the weather today (5 minutes ago)
> """
    )     
