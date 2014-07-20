from parser import Parser


class TextTwitter:
    def __init__( self ):
	    self._parser = Parser()	
    
    def run( self ):
        while( True ):
            strInput = input( "> " )
            print( self._parser.processInput(strInput), end = '' ) 
    	

if __name__ == "__main__":
    texttwitter = TextTwitter()
    texttwitter.run() 
    





