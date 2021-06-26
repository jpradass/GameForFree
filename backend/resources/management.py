from backend.models.games import Game
# from models.games import Game
from typing import Dict
from ..version import version
import requests
# from version import version

gamerpower_endpoint = 'https://www.gamerpower.com/api/giveaways?platform=pc'

def health() -> Dict[str, str]:
    return {'Status': 'OK'}

def server_version() -> Dict[str, str]:
    return {'Version': f'v{version}'}

def refresh() -> bool:
    games = requests.get(gamerpower_endpoint).json()
    if not games:
        return False

    try:
        for game in games:
            Game(**game).saveto_db()
        
        return True
    except Exception as e:
        print(e.__str__())
        return False