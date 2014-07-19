from user import User


class Storage:

    def __init__(self):
        self._messages = []
        self._users = dict()
        
    def saveMessage( self, message ):
        if message.user not in self._users:
            self._users[message.user]= User( message.user) 
		
        self._messages.append( message)
        
		
    def getMessages( self, usernames ):
        """ returns all messages from all users in usernames
        """
        return [msg  for msg in self._messages if msg.user in usernames ]
        
        
    def loadUser( self, username ):
        """ returns a User or None if not found
        """
        if username in self._users:
            return self._users[username]
			
        return None 	
        	 
             
    def loadCreateUser( self, username ):
        """ returns a User if not found it will be created
        """
        if username not in self._users:
            self._users[username]= User(username)
        
        return self._users[username]
        

