import random




class Card:
    """This class is responsible for the random number generater of the cards
    
    attributes:
    new_card(int): outputs a random number
    """
    
    def __init__(self):
        self.card=0
        
        
        
    def new_card(self):
        self.card=random.randint(1,13)
        return self.card