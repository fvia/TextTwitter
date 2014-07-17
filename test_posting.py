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


