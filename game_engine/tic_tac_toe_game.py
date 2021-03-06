from copy import deepcopy
from typing import Callable, List, Optional
from game_engine import TicTacToeTurn, TicTacToeGameInfo, AbstractTicTacToeGame

class TicTacToeGame(AbstractTicTacToeGame):
    def __init__(self, game_id: str, first_player_id: str, second_player_id: str, 
        strategy: Optional[Callable[[TicTacToeGameInfo], TicTacToeTurn]] = None) -> None:
        self.__game_id = game_id
        self.__first_player_id = first_player_id
        self.__second_player_id = second_player_id
        self.__winner_id = ""
        self.__strategy = strategy
        self.__turns: List[TicTacToeTurn] = []


    def current_player_id(self) -> str:
        if self.__turns == []:
            return self.__first_player_id
        if self.__turns[-1].player_id == self.__first_player_id:
            return self.__second_player_id
        return self.__first_player_id

    def is_turn_correct(self, turn: TicTacToeTurn) -> bool:
        if  self.__winner_id != "":
            return False
        if not (0 <= turn.x_coordinate <= 2) and not (0 <= turn.y_coordinate <= 2):
            return False
        if self.current_player_id() != turn.player_id:
            return False

        field = self.get_game_info().field

        if field[turn.x_coordinate][turn.y_coordinate] != " ":
            return False

        return True

    def do_turn(self, turn: TicTacToeTurn) -> TicTacToeGameInfo:
        if not self.is_turn_correct(turn):
            return self.get_game_info()
        self.__turns.append(deepcopy(turn))
        self.set_winner_id()
        return self.get_game_info()

    def set_winner_id(self) -> None:
        field = self.get_game_info().field
        #draw = True
        for i in range(3):
            row1 = ""
            row2 = ""
            for j in range(3):
                row1 += field[i][j]
                row2 += field[j][i]
            if row1 == "XXX" or row2 == "XXX":
                self.__winner_id = self.__first_player_id
                return
            if row1 == "OOO" or row2 == "OOO":
                self.__winner_id = self.__second_player_id
                return

        row1 = ""
        row2 = ""
        for i in range(3):
            row1 += field[i][i]
            row2 += field[i][2 - i]
            if row1 == "XXX" or row2 == "XXX":
                self.__winner_id = self.__first_player_id
                return
            if row1 == "OOO" or row2 == "OOO":
                self.__winner_id = self.__second_player_id
                return
        
        #if draw:
         #   self.__winner_id = "draw"
          #  return

        if not " " in field[1] and not " " in field[2] and not " " in field[3]:
            self.__winner_id = "draw"
            return
        
        return

       

    def get_game_info(self) -> TicTacToeGameInfo:
        result = TicTacToeGameInfo(
            game_id=self.__game_id,
            field=[
                [" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]
            ],
            sequence_of_turns=deepcopy(self.__turns),
            first_player_id=self.__first_player_id,
            second_player_id=self.__second_player_id,
            winner_id=self.__winner_id
        )
        for turn in self.__turns:
            if turn.player_id == self.__first_player_id:
                ch = "X"
            else:
                ch = "O"
            result.field[turn.x_coordinate][turn.y_coordinate] = ch
        return result