from message import Message
from user import User
from storage import Storage
from formater import Formater
from testabletime import TestableTime

class Controller:
 
    def __init__(self):
        self._storage = Storage()
        self._formater = Formater()

           
    def follows( self, username, username_to_follow ):
        user = self._storage.loadCreateUser( username )    
        user.following( username_to_follow )  
        
        
    def posts( self, username, str_message ):
        msg = Message( TestableTime.now(), str_message, username )
        self._storage.saveMessage(msg)

        
    def reads( self, username ):
        messages = self._storage.getMessages([username])
        return self._formater.readFormat(messages)

        
    def wall( self, username ):
        user = self._storage.loadUser( username )
        if not user:
            return ""
    
        users_to_list = user.followed_users()
        users_to_list.append( username )
  
        all_messages = self._storage.getMessages( users_to_list )

        return self._formater.wallFormat( all_messages)  
