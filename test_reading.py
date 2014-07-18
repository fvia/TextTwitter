import unittest
from datetime import datetime

from time_utils import ut_time
from texttwitter import TextTwitter


class testReading(unittest.TestCase):
   
  def setUp(self ):  
    self.ttw = TextTwitter()
    self.testTime = datetime.now()
    
  def timedAction( self, strMessage, elapsedTime  ):
    ut_time.fastenNow( self.testTime,deltaMinutes= elapsedTime)
    return self.ttw.processInput( strMessage ) 
  
	  
  def test_reading_alice(self):
    self.timedAction( "Alice -> I love the weather today",-5)

    self.assertEqual( 
      self.timedAction( "Alice" ,0), 
      "I love the weather today (5 minutes ago)\n"
      "> " 
     )
	  
 
  def test_reading_bob(self):
    self.timedAction( "Bob -> Damn! We lost!", -2 ) 
    self.timedAction( "Bob -> Good game though.", -1 ) 
   
    self.assertEqual( 
		self.timedAction( "Bob",0 ), 
	    "Good game though. (1 minute ago)\n"
	    "Damn! We lost! (2 minutes ago)\n"
        "> "  
    )     

