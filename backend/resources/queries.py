from typing import Dict
from ariadne.utils import convert_kwargs_to_snake_case
from ..models.games import Game
# from models.games import Game

def resolve_games(obj, info) -> Dict[str, any]:
    try:
        games = [game.to_dict() for game in Game.find_all()]
        payload = {
            "success": True,
            "games": games
        }
    except Exception as e:
        payload = {
            "success": False,
            "errors": [str(e)]
        }
    return payload

@convert_kwargs_to_snake_case
def resolve_game(obj, info, game_id) -> Dict[str, any]:
    try:
        game = Game.findby_id(game_id)
        payload = {
            "success": True,
            "game": game.to_dict()
        }

    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"game itme matching id {game_id} not found"]
        }

    return payload