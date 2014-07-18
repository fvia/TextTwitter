import unittest
import datetime
from time_utils import ut_time
from texttwitter import TextTwitter


class TextTwitterTimedTest( unittest.TestCase ):
	
  def __init__(self, *args, **kwargs):
    unittest.TestCase.__init__(self, *args, **kwargs)
    self._testTime = datetime.datetime.now()
    self._textTwitter = TextTwitter()
    
    
  def timedInput( self, strMessage, deltaMinutes=None,deltaSeconds=None  ):
    ut_time.fastenNow( self._testTime,deltaMinutes,deltaSeconds )
    return self._textTwitter.processInput( strMessage ) 



