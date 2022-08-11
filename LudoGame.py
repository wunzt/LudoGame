# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 8/10/2022
# Description: Allows the user to play a text-based, simplified version of the game Ludo. User passes a list of players,
#              and a list of turns. The program decides which token moves based on a specific algorithm and moves the
#               tokens. The program tracks the players' playing status and returns a list of the spaces occupied by all
#               tokens at the end of execution.


class Player:
    """Creates player objects for class LudoGame, holding information regarding the player’s position, game status,
    start and end spaces (by calling get_player_spaces in GameBoard), token locations, token step counts, and whether
    their tokens are stacked. LudoGame calls each get method when determining token movements, executing token
    movements, and determining which players are Finished."""

    def __init__(self, player_pos):
        """Initiates a player object that holds values for the player at the passed position (A, B, C, or D),
        the location of token ‘p’ and token ‘q’ at ‘H’, the player’s current status (not playing, playing, finished),
        the start and end space for the player (calling get_player_spaces in GameBoard class), the step count from
        token ‘p’ and token ‘q’ at -1, and the Boolean value for whether the tokens are stacked to False."""
        self._player_pos = player_pos
        self._status = "Not Playing"
        self._token_p_step_count = -1
        self._token_q_step_count = -1
        self._token_stacked = False

    def get_pos(self):
        """Returns the board position of the player object."""
        return self._player_pos

    def update_status(self, status):
        """Updates the current playing status of the player."""
        self._status = status

    def get_status(self):
        """Returns the playing status of the player."""
        return self._status

    def get_completed(self):
        """Returns True if the player’s current state is Finished. Otherwise, returns False."""
        if self._status == "Finished":
            return True
        else:
            return False

    def update_token_p_step_count(self, roll):
        """Adds the roll to update the token's step count."""
        self._token_p_step_count += roll

    def set_token_p_step_count(self, space):
        """Sets the step count for token p to the passed space."""
        self._token_p_step_count = space

    def get_token_p_step_count(self):
        """Returns the step count for token p."""
        return self._token_p_step_count

    def update_token_q_step_count(self, roll):
        """Adds the roll to update the token's step count."""
        self._token_q_step_count += roll

    def set_token_q_step_count(self, space):
        """Sets the step count for token q to the passed space."""
        self._token_q_step_count = space

    def get_token_q_step_count(self):
        """Returns the step count for token q."""
        return self._token_q_step_count

    def get_space_name(self, step_count):
        """Takes the step count of a token and returns the name of the space the token is currently on."""

        player_a_spaces = ['R', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                           24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45,
                           46, 47, 48, 49, 50, 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'E', 'H']
        player_b_spaces = ['R', 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
                           35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
                           1, 2, 3, 4, 5, 6, 7, 8, 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'E', 'H']
        player_c_spaces = ['R', 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
                           49, 50,  51, 52, 53, 54, 55, 56, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                           18, 19, 20, 21, 22, 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'E', 'H']
        player_d_spaces = ['R', 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                           11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
                           34, 35, 36, 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'E', 'H']

        if self._player_pos == 'A':
            return str(player_a_spaces[step_count])

        if self._player_pos == 'B':
            return str(player_b_spaces[step_count])

        if self._player_pos == 'C':
            return str(player_c_spaces[step_count])

        if self._player_pos == 'D':
            return str(player_d_spaces[step_count])

    def update_token_stacked(self, boolean_value):
        """Updates whether the player's tokens are stacked or not via the passed boolean."""
        self._token_stacked = boolean_value

    def get_token_stacked(self):
        """Returns True if player’s tokens are stacked. Otherwise, returns False."""
        return self._token_stacked


class LudoGame:
    """Creates a game of Ludo with four possible players positions. The play_game method moves the game forward by
    taking a list of turns, running an algorithm to determine which token should move, and moving the token. After
    each move, it will check if any players have Finished and return a list of current token positions. It relies on
    GameBoard for information regarding special case spaces tokens might land on and Player for information regarding
    the game’s players and their tokens."""

    def __init__(self):
        """Initiates a game object with a list of player objects."""
        self._player_object_list = []

    def set_player_by_position(self, player_pos):
        """Creates a player object at the passed position and adds it to the player object list."""
        temp_player = Player(player_pos)
        self._player_object_list.append(temp_player)

    def get_player_by_position(self, player_pos):
        """Takes the position of a player and returns the player object at that position."""
        for i in self._player_object_list:
            if player_pos == i.get_pos():
                return i

    def move_token(self, player, token, roll):
        """Takes the player as an object, the token name, and the player’s current roll and moves the given token
        forward a number of spaces equal to the roll, unless the token’s location is ‘H’, in which case it moves to
        ‘R’. If the player’s tokens are stacked, both will be moved. Updates the token’s step count by adding the
        amount of the roll. If this takes the token beyond ‘E’, the remaining steps are subtracted from the step
        count. If the step count is not ‘H’ or ‘E’ and equal to another token from the same player, the stacked value
        is set to True (the tokens are stacked). If it is equal to a token of another player, that token (or both if
        stacked) are returned to that player’s ‘H’ space. Any token returned this way will have its stacked value set
        to False."""

        token_p = player.get_token_p_step_count
        token_q = player.get_token_q_step_count

        move_token_p = player.update_token_p_step_count
        move_token_q = player.update_token_q_step_count

        if token == 'none':
            return

        if player.get_token_stacked() is True:
            move_token_p(roll)
            move_token_q(roll)

        elif token == 'p':
            if token_p() == -1:
                move_token_p(1)

            elif token_p() + roll > 57:
                extra = roll - (57 - token_p())
                space_index = 57 - extra
                player.set_token_p_step_count(space_index)

            else:
                move_token_p(roll)

            if token_p() not in [-1, 0, 57]:
                for i in self._player_object_list:
                    if i is player:
                        if i.get_space_name(i.get_token_q_step_count()) == player.get_space_name(token_p()):
                            player.update_token_stacked(True)
                    else:
                        if i.get_space_name(i.get_token_p_step_count()) == player.get_space_name(token_p()):
                            i.set_token_p_step_count(-1)
                            i.update_token_stacked(False)
                        if i.get_space_name(i.get_token_q_step_count()) == player.get_space_name(token_p()):
                            i.set_token_q_step_count(-1)
                            i.update_token_stacked(False)

        else:
            if token_q() == -1:
                move_token_q(1)

            elif token_q() + roll > 57:
                extra = roll - (57 - token_q())
                space_index = 57 - extra
                player.set_token_q_step_count(space_index)

            else:
                move_token_q(roll)

            if token_q() not in [-1, 0, 57]:
                for i in self._player_object_list:
                    if i is player:
                        if i.get_space_name(i.get_token_p_step_count()) == player.get_space_name(token_q()):
                            player.update_token_stacked(True)
                    else:
                        if i.get_space_name(i.get_token_q_step_count()) == player.get_space_name(token_q()):
                            i.set_token_p_step_count(-1)
                            i.update_token_stacked(False)
                        if i.get_space_name(i.get_token_p_step_count()) == player.get_space_name(token_q()):
                            i.set_token_q_step_count(-1)
                            i.update_token_stacked(False)

    def token_algorithm(self, player, roll):
        """Takes the player as an object and the player’s current roll to determine which token should be moved
        (always in the order of ‘p’, then ‘q’ when the tokens meet the same conditions). If the roll is 6, a token
        will move out from ‘H’ to ‘R’ if possible. If both are out of ‘H’, the algorithm treats it the same as 1-5.
        On a 1-5, if either token can move to ‘E’ exactly, it does. Next, if either token can move to a space occupied
        by an opposing token, it will. If both can, the token further from ‘E’ moves. If no conditions have been met,
        the token further from ‘E’ moves."""

        token_p = player.get_token_p_step_count
        token_q = player.get_token_q_step_count

        if roll == 6:
            if token_p() == -1:
                return 'p'
            if token_q() == -1:
                return 'q'

        if token_p() == -1 and token_q() == -1:
            return 'none'

        if token_p() == 57 - roll:
            return 'p'
        if token_q() == 57 - roll:
            return 'q'

        for i in self._player_object_list:
            if i is not player:
                if player.get_token_p_step_count() + roll == i.get_token_p_step_count():
                    return 'p'
                if player.get_token_q_step_count() + roll == i.get_token_q_step_count():
                    return 'q'

        if token_p() != -1 and token_q() == -1:
            return 'p'

        if token_p() < token_q():
            return 'p'

        return 'q'

    def play_game(self, player_list, turns_list):
        """Takes list of players, setting players’ statuses to Playing, and a list of turns and moves the players’
        tokens according to the rolls given in the turns list and the decision algorithm, calling the move_token
        and token_algorithm methods. Then, checks after each move if any player has both tokens on ‘E’. If so, updates
        that player’s status to Finished. Finally, returns a list of strings representing the current spaces occupied
        by the tokens of each player after each turn."""

        end_spaces_list = []

        for i in player_list:
            self.set_player_by_position(i)

        for i in self._player_object_list:
            i.update_status("Playing")

        for i in turns_list:
            temp_player = self.get_player_by_position(i[0])

            token = self.token_algorithm(temp_player, i[1])

            if token != 'none':
                self.move_token(temp_player, token, i[1])

            for pos in self._player_object_list:
                if pos.get_token_p_step_count() == 57:
                    if pos.get_token_q_step_count() == 57:
                        pos.update_status("Finished")

        for i in self._player_object_list:
            token_p = i.get_space_name(i.get_token_p_step_count())
            token_q = i.get_space_name(i.get_token_q_step_count())

            end_spaces_list.append(token_p)
            end_spaces_list.append(token_q)

        return end_spaces_list
