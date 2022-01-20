from Classes.Card import Card


class Game_Master:
    """This class is responsible for organizing the game HiLo
    
    attributes:
    card-the class responsible for getting the random card number
    get_input:gets neccesary information from the user for the game
    do_score:calculates the score for the game and decides how many points the player should receive
    display:outputes results into the terminal.
    is_playing: checks if the game is currently active
    """
    
    def __init__(self):
        """This is a contructor for the Game_Master instance
        """
        self.card=Card()
        self.is_playing=False
        self.score=0
        self.total_score=0
        
        
    def start(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_logic()
            self.do_display()
            
    def get_inputs(self):
        """displays first card, then recieves input for if the next card is higher or lower
        """
        first_card = Card.new_card()
        print (f'The card is:{first_card}')

        guess = input(f'High or Low? (h/l)').lower()

        next_card = Card.new_card()

        print(f'The next card was: {next_card}')

        if guess == 'l':
            if next_card <= first_card:
               points = self.player_points + 100
               print(f'Your score is: {points}')
            else:
               points = self.player_points - 75
               print(f'Your score is: {points}')

                
        elif guess == 'h':
            if next_card >= first_card:
               points = self.player_points + 100
               print(f'Your score is: {points}')

                
            else:
               points = self.player_points - 75
               print(f'Your score is: {points}')

                

        
    def do_logic(self):
        """generates the score system and keeps track of it
        """
        self.player_points = 300

        
    def do_display(self):
        """outputs the results and, if the score is not 0, requests to play again.
        """