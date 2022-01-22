from Classes.Deck import Deck

limit = 1000
easy_mode = 1
hard_mode =  1.5

class Game_Master:
    """This class is responsible for organizing the game HiLo
    
    attributes:
    card: the class responsible for getting the random card number
    get_input: gets necessary information from the user for the game
    do_score: calculates the score for the game and decides how many points the player should receive
    display: outputs results into the terminal.
    is_playing: checks if the game is currently active
    """
    
    def __init__(self):
        """This is a contructor for the Game_Master instance
        """
        self.deck = Deck()
        self.is_playing=False
        self.score=0
        self.total_score=0
        self.first_card = 0
        self.next_card = 0
        self.guess = ""
        self.round = 0
        
    def start(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self.player_points = 300
        self.is_playing = True
        while self.is_playing and self.player_points > 0 and self.player_points < limit:
            self.get_inputs()
            self.do_logic()
            self.do_display()

        
            
    def get_inputs(self):
        """displays first card, then recieves input for if the next card is higher or lower
        """
        

        self.first_card = self.deck.draw()
        print (f'\nThe card is:{self.first_card}')

        self.guess = input(f'High or Low? (h/l)' ).lower()
        while self.guess != "h" and self.guess != "l":
            print("Invalid selection, please try again.")
            self.guess = input(f'High or Low? (h/l)' ).lower()
        self.next_card = self.deck.draw()

        print(f'The next card was: {self.next_card}')

        if self.round > 0:
            choice = input("Would you like to play again: (y/n) ")
            while choice != "y" and choice != "n":
                print("Invalid selection, please try again.")
                choice = input("Would you like to play again: (y/n) ")
            if choice == "n":
                self.is_playing = False
                return

        
        
    def do_logic(self):
        """generates the score system and keeps track of it
        """

        if self.guess == 'l':
            if self.next_card <= self.first_card:
               self.player_points += 100
            else:
               self.player_points -= 75    
        elif self.guess == 'h':
            if self.next_card >= self.first_card:
               self.player_points += 100
            else:
               self.player_points -= 75
        if self.player_points < 75:
            self.is_playing = False
      
    def do_display(self):
        """outputs the results and, if the score is not 0, requests to play again.
        """
        print(f"Your score is: {self.player_points}")

        if self.round >= limit:
            print("\nYou got 1000 points! You win!!")
            print(f"Your final score is: {self.player_points}")
            

        if self.is_playing == False:
            print("\nGame over!")
            print(f"Your final score was {self.player_points}")