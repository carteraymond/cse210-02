import random




class Card:
    """This class is responsible for the random number generater of the cards
    
    attributes:
    new_card(int): outputs a random number
    """
    
    def __init__(self):
        self.new_card=0
        
        
        
    def new_card(self):
        self.new_card=random.randint(1,13)