import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



def determine_rps_result(player_1:str, player2:str) -> dict:
    """
    Determines the result of a Rock-Paper-Scissors round between Player 1 and an player2,
    calculates the score, and returns the outcome.

    The function maps the choices of both players from letter representations 
    ('R', 'P', 'S') to the corresponding RPS choices and then calculates the 
    score based on the game outcome.

    Args:
        player_1 (str): The choice of Player 1 ('R', 'P', or 'S').
        player2 (str): The choice of the player2 ('R', 'P', or 'S').

    Returns:
        dict: The result of the game. A draw returns 3, a win returns 6, and a loss returns 0.
        The dictionary contains both players and their scores e.g {"player1": <score>, "opponent": <score>}
    """
    player_1  = map_letter_to_rps(player_1)
    player2   = map_letter_to_rps(player2)
    return calculate_rps_score(player_1, player2)


def map_letter_to_rps(letter):
    """
    Maps a set of given letters (A, B, C, X, Y or Z) to the first letter of the words (R)ock, (P)aper and (S)cissor game cyclically.
    
    Mapping:
        A = R, B = P, C = S, X = R, Y = P, Z = S
    
    Args:
        letter (str): The letter for the mapping.
    
    Raises:
        Raises a ValueError if the letter entered are not `A, B, C, X, Y or Z`
        
    Returns:
        Returns the mapping of the letter to RPS game.
    
    Example usage:
    
    >>> map_letter_to_rps("A")
    >>> "R"
    
    >>> map_letter_to_rps("W")
    >>> Raises ValueError("The letter `W` is invalid. Letters must be ['A', 'B', 'C', 'X', 'Y', 'Z']")
    """
    
    game = { "A": "R", "B": "P", "C": "S", "X": "R", "Y": "P", "Z": "S" }
    
    try:
        return game[letter.strip().upper()]
    except KeyError:
        raise ValueError(f"The letter `{letter}` is invalid. Letters must be ['A', 'B', 'C', 'X', 'Y', 'Z'] ")
   

def calculate_rps_score(player1_choice:str, player2_choice:str):
    """
     Calculates scores based on the outcome of Rock-Paper-Scissors
        
    Args:
        player1_choice (str): Player 1 choice.
        player2_choice (str): Player 2 choice
        
    """
    game_choice_value = {"R" : 1,  "P" : 2, "S" : 3}
    
    DRAW  = 3
    WIN   = 6
    LOSS  = 0
    
    result      = get_winner(player1_choice, player2_choice)
    result_dict = {}
    
    if result == "draw":
        result_dict["player1"]    = DRAW + game_choice_value.get(player1_choice)
        result_dict["opponent"]   = DRAW + game_choice_value.get(player2_choice)
    elif result == "player1":
        result_dict["player1"]    = WIN  + game_choice_value.get(player1_choice)
        result_dict["opponent"]   = LOSS + game_choice_value.get(player2_choice)
    else:
        result_dict["opponent"]   = WIN  + game_choice_value.get(player2_choice)
        result_dict["player1"]    = LOSS + game_choice_value.get(player1_choice)
    
    return result_dict


def get_winner(player1:str, player2:str) -> dict:
    """Determines the winner of Rock-Paper-Scissors."""
    
    game_outcomes = {
        "RR": "draw", "PP": "draw", "SS": "draw",
        "PR": "player1", "RS": "player1", "SP": "player1",
        "RP": "opponent", "SR": "opponent", "PS": "opponent",
    }
    
    try:
         return game_outcomes[f"{player1}{player2}"]
    except KeyError:
        raise KeyError(f"The choice for player 1 or player 2 is invalid. Player 1: <{player1}>, Player 2: <{player2}>")

    
def play_game():
    """Reads the input file and calculates the total score for player1."""
    
    text_file = "problem_input.txt"
    total     = 0
    
    with open(text_file) as f:
        for line in f:
            if line.strip():  
                opponent, player_1 = line.strip().split(" ")
                result_dict        = determine_rps_result(player_1=player_1, player2=opponent)
                total += result_dict["player1"]
    return total
            
      
if __name__ == "__main__":
    print(play_game())


