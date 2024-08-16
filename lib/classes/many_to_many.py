class Game:
    def __init__(self, title):
        if not isinstance(title, str) or len(title) == 0:
            ValueError("Title must be a non-empty string")
        self._title = title
        self._results = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and len(new_title) > 0:
            self._title = new_title
        else:
            ValueError("Title must be a non-empty string")

    def results(self):
        return self._results

    def add_result(self, result):
        if isinstance(result, Result) and result.game == self:
            self._results.append(result)

    def players(self):
        return list(set(result.player for result in self._results))

    def average_score(self, player):
        player_results = [result.score for result in self._results if result.player == player]
        if player_results:
            return sum(player_results) / len(player_results)
        return 0


class Player:
    def __init__(self, username):
        if not isinstance(username, str) or not (2 <= len(username) <= 16):
            ValueError("Username must be a string between 2 and 16 characters")
        self._username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str) and 2 <= len(new_username) <= 16:
            self._username = new_username
        else:
            print("Warning: Username must be a string between 2 and 16 characters. Username not changed.")

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list(set(result.game for result in self.results()))

    def played_game(self, game):
        return any(result.game == game for result in self.results())

    def num_times_played(self, game):
        return len([result for result in self.results() if result.game == game])


class Result:
    all = []

    def __init__(self, player, game, score):
        if not isinstance(player, Player):
            ValueError("Player must be of type Player")
        if not isinstance(game, Game):
            ValueError("Game must be of type Game")
        if not isinstance(score, int) or not (1 <= score <= 5000):
            ValueError("Score must be an integer between 1 and 5000")

        self._player = player
        self._game = game
        if not hasattr(self, '_score'):
            self._score = score

        game.add_result(self)
        Result.all.append(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        AttributeError("Score cannot be changed once set.")

    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game
