from mlgames.player import Player

class HumanPlayer(Player):
	def name(self):
		return "Human Player"

	def play(self, board, piece):
		result = input("What would you like to do?\n").strip()
		return board.parse_move(result)

	def new_game(self, result):
		pass

	def new_batch(self, dir):
		pass

	def save(self, dir):
		pass