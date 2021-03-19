from typing import Dict
from game_engine import TicTacToeGame, TicTacToeGameInfo, TicTacToeTurn


class TicTacToeApp:
    def __init__(self):
        """пока не знаю, мб что-то ещё тут будет :)
        в обоих случаях айдишник - ключ, значение - угадайте, что)"""
        self._games: Dict[str, TicTacToeGame] = {}

    def start_game(self, first_player_id: str, second_player_id: str) -> TicTacToeGameInfo:
        new_game = str(len(self._games) + 1)
        
        self._games[new_game] = TicTacToeGame(
            game_id = str(len(self._games) + 1),
            first_player_id=first_player_id,
            second_player_id=second_player_id)

        return self._games[new_game].get_game_info()

        # ttt_game => add to dict => tttgi
        
    def get_game_by_id(self, game_id: str) -> TicTacToeGameInfo:
        return self._games[game_id].get_game_info()   #probably right

    def do_turn(self, turn: TicTacToeTurn, game_id: str) -> TicTacToeGameInfo:
        return self._games[game_id].do_turn(turn)
