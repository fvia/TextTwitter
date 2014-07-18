
from texttwittertimedtest import TextTwitterTimedTest


class testPosting( TextTwitterTimedTest ):

  def test_post_must_return_prompt(self):
	  
    self.assertEqual( 
		self.timedInput( "Alice -> I love the weather today"   ), 
        "> "  
    )     
    self.assertEqual( 
		self.timedInput( "Bob -> Damn! We lost!" ), 
        "> "  
    )     
    self.assertEqual( 
	    self.timedInput( "Bob -> Good game though." ), 
        "> "  
    )     


