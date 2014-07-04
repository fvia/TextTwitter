import unittest

from twcon import TwCon


class testPosting( unittest.TestCase ):

  def test_post_must_return_prompt(self):
    twc = TwCon()
    self.assertEqual( 
	twc.write( "Alice -> I love the weather today"   ), 
        "> "  
    )     
    self.assertEqual( 
	twc.write( "Bob -> Damn! We lost!" ), 
        "> "  
    )     
    self.assertEqual( 
	twc.write( "Bob -> Good game though." ), 
        "> "  
    )     

class testReading(unittest.TestCase):

  def setUp(self ):  
    self.twc = TwCon()
    self.twc.write( "Alice -> I love the weather today") 
    self.twc.write( "Bob -> Damn! We lost!" ) 
    self.twc.write( "Bob -> Good game though." )
 
  def test_reading_alice(self):
    self.assertEqual( 
	self.twc.write( "Alice" ), 
        "I love the weather today (5 minutes ago)"  
    )     





if __name__ == "__main__":
  unittest.main()



