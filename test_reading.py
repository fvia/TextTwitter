
from texttwittertimedtest import TextTwitterTimedTest


class testReading(TextTwitterTimedTest):
	  
  def test_reading_alice(self):
    self.timedInput( "Alice -> I love the weather today",-5)

    self.assertEqual( 
      self.timedInput( "Alice" ,0), 
      "I love the weather today (5 minutes ago)\n"
     )
	  
 
  def test_reading_bob(self):
    self.timedInput( "Bob -> Damn! We lost!", -2 ) 
    self.timedInput( "Bob -> Good game though.", -1 ) 
   
    self.assertEqual( 
		self.timedInput( "Bob"), 
	    "Good game though. (1 minute ago)\n"
	    "Damn! We lost! (2 minutes ago)\n"
    )     

