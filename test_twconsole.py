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
	  
    ut_time.fastenNow( datetime.now())  
    self.twc = TwConsole()
    self.twc.processInput( "Alice -> I love the weather today") 
    self.twc.processInput( "Bob -> Damn! We lost!" ) 
    self.twc.processInput( "Bob -> Good game though." )
 
  def test_reading_alice(self):
    ut_time.fastenNow( ut_time.now() + timedelta(0,5*60))  
    self.assertEqual( 
	self.twc.processInput( "Alice" ), 
        "I love the weather today (5 minutes ago)\n> "  
    )     




