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








if __name__ == "__main__":
  unittest.main()



