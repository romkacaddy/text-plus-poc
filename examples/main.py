from textplus import Textplus
import threading

def main():
    connection = Textplus()
    connection.send_message("+1numberhere", "some message") #number must be like: 18312345423 (mind the country code)
    
    
main()
