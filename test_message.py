
import unittest
import time_utils

from message import Message

from datetime import datetime, timedelta




class testMessage( unittest.TestCase ):
  def test_Message_now(self):
    
    msg = Message("Hi Boy!" )
    self.assertEqual( msg.timedText(), "Hi Boy! (0 seconds ago)"  )

  def test_Message_10_minutes_later(self):
    
    time_utils.ut_time.fastenNow( datetime.now())
    msg = Message("Hi Peter!")
    
    time_utils.ut_time.fastenNow( time_utils.ut_time.now()+timedelta(0,10*60))
    self.assertEqual( msg.timedText(), "Hi Peter! (10 minutes ago)"  )
		

