
import unittest
from datetime import datetime

from message import Message
from time_utils import ut_time


class testMessage( unittest.TestCase ):
  def test_Message_now(self):
    
    initial_time =  datetime.now()
    ut_time.fastenNow( initial_time ) 
    
    msg = Message("Hi Boy!" )
    self.assertEqual( msg.timedText(), "Hi Boy! (0 seconds ago)"  )

  def test_Message_10_minutes_later(self):
    
    initial_time =  datetime.now()
    ut_time.fastenNow( initial_time)
    msg = Message("Hi Peter!")
    
    ut_time.fastenNow( initial_time, deltaMinutes=10)
    self.assertEqual( msg.timedText(), "Hi Peter! (10 minutes ago)"  )
		

