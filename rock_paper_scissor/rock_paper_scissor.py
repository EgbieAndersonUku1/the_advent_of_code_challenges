import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



def determine_rps_result(player_1:str, player2:str, rules:dict) -> dict:
    """
    Determines the result of a Rock-Paper-Scissors round between Player 1 and an player2,
    calculates the score, and returns the outcome.

    The function maps the choices of both players from letter representations 
    ('R', 'P', 'S') to the corresponding RPS choices and then calculates the 
    score based on the game outcome.

    Args:
        player_1 (str): The choice of Player 1 ('A', 'B', 'C', 'X', 'Y' or 'Z' ).
        player2 (str): The choice of the player2 ('A', 'B', 'C', 'X', 'Y' or 'Z' ).
        rules (dict) : The rules for each game

    Returns:
        dict: The result of the game. A draw returns 3, a win returns 6, and a loss returns 0.
        The dictionary contains both players and their scores e.g {"player1": <score>, "opponent": <score>}
    """
    player_1  = map_letter_to_rps(player_1)
    player2   = map_letter_to_rps(player2)
    return calculate_rps_score(player_1, player2, rules)


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
   

def calculate_rps_score(player1_choice:str, player2_choice:str, game_settings:dict):
    """
     Calculates scores based on the outcome of Rock-Paper-Scissors
        
    Args:
        player1_choice (str): Player 1 choice.
        player2_choice (str): Player 2 choice
        game_settings (dict): The game settings for the game, differnt games have differnt rules
        
    """
      
    DRAW  = game_settings.get("DRAW")
    WIN   = game_settings.get("WIN")
    LOSS  = game_settings.get("LOSS")
    
    result      = get_winner(player1_choice, player2_choice)
    result_dict = {}
    
    if result == "draw":
        result_dict["player1"]    = DRAW + game_settings.get(player1_choice)
        result_dict["opponent"]   = DRAW + game_settings.get(player2_choice)
    elif result == "player1":
        result_dict["player1"]    = WIN  + game_settings.get(player1_choice)
        result_dict["opponent"]   = LOSS + game_settings.get(player2_choice)
    else:
        result_dict["opponent"]   = WIN  + game_settings.get(player2_choice)
        result_dict["player1"]    = LOSS + game_settings.get(player1_choice)
    
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

    
def get_opposite_hand(hand, is_winner=True):
    """
    Returns the opposite hand based on whether the provided hand is a winner or a loser.

    This function accepts a hand and checks if it's a winning or losing hand. If it's a
    winning hand (is_winner=True), the function returns the corresponding losing hand. 
    If it's a losing hand (is_winner=False), it returns the corresponding winning hand.

    Args:
        hand (str): The hand to look up. Expected values are "A", "B", or "C".
        is_winner (bool): A flag indicating whether the provided hand is a winner. 
                          If True (default), returns the losing hand. If False, 
                          returns the winning hand.

    Returns:
        str: The corresponding hand based on the provided hand and the is_winner flag.

    Raises:
        ValueError: If the provided hand is invalid or not one of "A", "B", or "C".

    Example:
        
        >>> get_opposite_hand("A", is_winner=True)
        'B'
        >>> get_opposite_hand("A", is_winner=False)
        'C'
    """
    winning_to_losing = {
        "A": "B",
        "B": "Z",
        "C": "A"
    }

    losing_to_winning = {
        "A": "C",
        "B": "A",
        "C": "B"
    }

    try:
        hand = hand.strip().upper()
        if is_winner:
            return winning_to_losing[hand]
        return losing_to_winning[hand]
    except KeyError:
        raise ValueError(f"Invalid hand provided: {hand}")


def cheat_to_win_or_lose(player1_hand, player2_hand):
    """
    Manipulates the outcome of the game based on player 1's cheating strategy (win, draw, or lose).

    Args:
        player1_hand (str): The desired outcome for player 1, where "Z" forces a win, 
                            "Y" forces a draw, and "X" forces a loss.
        player2_hand (str): The hand played by player 2.

    Returns:
        tuple: A tuple containing player 1's manipulated hand and player 2's hand.

    The function behaves as follows:
    - If player1_hand is "Z" (win), it returns the winning hand for player 1 based on player 2's hand.
    - If player1_hand is "Y" (draw), it returns player 2's hand for both players to force a draw.
    - If player1_hand is "X" (loss), it returns a losing hand for player 1 based on player 2's hand.
    """
    DRAW = "Y"
    LOSS = "X"
    WIN  = "Z"

    HAND_SET = {
        WIN: get_opposite_hand(player2_hand),
        DRAW: player2_hand,
        LOSS: get_opposite_hand(player2_hand, is_winner=False)
    }
    
    try:
        return HAND_SET[player1_hand], player2_hand
    except KeyError:
        raise ValueError(f"The player hand combination is invalid: Player 1 {player1_hand} and Player 2 {player2_hand}")


def play_game(game_settings, play_dishonest_game=False):
    """Reads the input file and calculates the total score for player1."""
    
    text_file     = "problem_input.txt"
    total         = 0
   
    with open(text_file) as f:
        for line in f:
            if line.strip():  
                
                opponent_hand, player_1_hand = line.strip().split(" ")
                
                if play_dishonest_game:
                    player_1_hand, opponent_hand = cheat_to_win_or_lose(player1_hand=player_1_hand, player2_hand=opponent_hand)
                  
                result_dict  = determine_rps_result(player_1=player_1_hand, player2=opponent_hand, rules=game_settings)
                total += result_dict["player1"]
    return total
            
        

if __name__ == "__main__":
    game_settings = {"R": 1, "P": 2, "S": 3, "DRAW": 3, "WIN" : 6, "LOSS": 0}
    
    print(f"Game 1 -> RPS -> Total score: {play_game(game_settings=game_settings)}")
    print(f"Game 2 -> RPS with player 1 cheating -> Total score : {play_game(game_settings=game_settings, play_dishonest_game=True)}")
   



