import unittest

from datetime import datetime, timedelta
from time_utils import ut_time

from twconsole import TwConsole


class testPosting( unittest.TestCase ):

  def test_post_must_return_prompt(self):
    twc = TwConsole()
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
    self.twc = TwConsole()

  def test_reading_alice(self):
    ut_time.fastenNow( datetime.now())  
    self.twc.processInput( "Alice -> I love the weather today") 
      
    ut_time.fastenNow( ut_time.now() + timedelta(0,5*60))  
    self.assertEqual( 
	self.twc.processInput( "Alice" ), 
"""I love the weather today (5 minutes ago)
> """  
    )     

  def test_reading_bob(self):
    time_read_bob =  datetime.now() 
    
    ut_time.fastenNow( time_read_bob - timedelta(0,2*60))  
    self.twc.processInput( "Bob -> Damn! We lost!" ) 
    
    ut_time.fastenNow( time_read_bob - timedelta(0,1*60))
    self.twc.processInput( "Bob -> Good game though." )
   
    ut_time.fastenNow(time_read_bob)  
    self.assertEqual( 
		self.twc.processInput( "Bob" ), 
"""Good game though. (1 minute ago)
Damn! We lost! (2 minutes ago)
> """  
    )     

class testFollowing(unittest.TestCase):
  def setUp(self ):  
    self.twc = TwConsole()
    self.time_test =  datetime.now()
    
    ut_time.fastenNow( self.time_test - timedelta(0,2*60))  
    self.twc.processInput( "Bob -> Damn! We lost!" ) 
    
    ut_time.fastenNow( self.time_test - timedelta(0,1*60))
    self.twc.processInput( "Bob -> Good game though." )
    
    ut_time.fastenNow( self.time_test - timedelta(0,5*60))  
    self.twc.processInput( "Alice -> I love the weather today" ) 
	
    ut_time.fastenNow( self.time_test - timedelta(0,2))  
    self.twc.processInput( "Charlie -> I'm in New York today! Anyone want to have a coffee?" )
    self.twc.processInput( "Charlie follows Alice")
    
    
	
  def test_follow_Alice( self):
    ut_time.fastenNow(self.time_test) 	  
    self.assertEqual( 
      self.twc.processInput( "Charlie wall" ), 
"""Charlie - I'm in New York today! Anyone want to have a coffee? (2 seconds ago)
Alice - I love the weather today (5 minutes ago)
> """
    )     

  def test_follow_Bob( self):
    self.twc.processInput( "Charlie follows Bob")  
    ut_time.fastenNow(self.time_test) 	  
    self.assertEqual( 
      self.twc.processInput( "Charlie wall" ), 
"""Charlie - I'm in New York today! Anyone want to have a coffee? (2 seconds ago)
Bob - Good game though. (1 minute ago)
Bob - Damn! We lost! (2 minutes ago)
Alice - I love the weather today (5 minutes ago)
> """
    )     



		

