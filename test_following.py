
from texttwittertimedtest import TextTwitterTimedTest


class testFollowing(TextTwitterTimedTest):

  def setUp(self ):  
    self.timedInput( "Bob -> Damn! We lost!",-2)
    self.timedInput( "Bob -> Good game though.",-1)
    self.timedInput( "Alice -> I love the weather today",-5)
    self.timedInput( "Charlie -> I'm in New York today! Anyone want to have a coffee?",deltaSeconds= -2)
    self.timedInput( "Charlie follows Alice",deltaSeconds= -2)
    
	
  def test_follow_Alice( self):  
    self.assertEqual( 
      self.timedInput( "Charlie wall" ), 
      "Charlie - I'm in New York today! Anyone want to have a coffee? (2 seconds ago)\n"
      "Alice - I love the weather today (5 minutes ago)\n"
      "> "
    )     


  def test_follow_Bob( self):
    self.timedInput( "Charlie follows Bob")  
    self.assertEqual( 
      self.timedInput( "Charlie wall" ), 
      "Charlie - I'm in New York today! Anyone want to have a coffee? (2 seconds ago)\n"
      "Bob - Good game though. (1 minute ago)\n"
      "Bob - Damn! We lost! (2 minutes ago)\n"
      "Alice - I love the weather today (5 minutes ago)\n"
      "> "
    )     

