from textplus import Textplus

def main():
    
    connection = Textplus()
    connection.send_message("yournumber", "test") #number must be like: 18312345423 (mind the country code)
    
    
main()