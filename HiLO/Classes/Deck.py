import random, os, time




class Deck:
    """This class is responsible for the random number generater of the cards
    
    attributes:
    new_card(int): outputs a random number
    """
    
    def __init__(self):
        pass
        
        
        
    def draw(self):
        #self.card=random.randint(1,13)
        return random.randint(1,13)
    def shuffle(self):
        station = ("<---------> \n"
         +" \        \ \n"
         +"\ \        \ \n"
         +" \ \        \ \n"
         +"\ \ \        \ \n"
         +" \ \  <________>\n"
         +"  \ \  <_________>\n"
         +"   \ \  <_________>\n")

        shuffle = ("<---------> \n"
                +" \        \ \n"
                +"\ \        \ \n"
                +" \ \        \ \n"
                +"\ \ \        \ \n"
                +" \ \  <________>\n"
                +" \ \  <________>\n"
                +"             \        \ \n"
                +"            \ \        \ \n"
                +"             \ \        \ \n"
                +"            \ \ \        \ \n"
                +"             \ \  <________>\n"
                +"              \ \  <_________>\n"
                +"               \ \  <_________>\n")

        wait_time = .25

        for i in range(random.randint(7,13)):
            print(shuffle)
            time.sleep(wait_time)
            os.system("clear")
            print(station)
            time.sleep(wait_time)
            os.system("clear")