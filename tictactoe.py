#import game

class TicTacToe :
	def __init__(self):
		self.board=[[None for j in range(3)] for i in range(3)]
		self.players=[]
	def addPlayer(self,player):
		self.players += [player]
	def begin(self):
		if len(self.players) is not 0:
			self.currentplayer = 0
	def score(self):
		out = {}
		for player in self.players :
			out[player]=self.scoreboard(player)
		return out
	def scoreboard(self,player):
		num = 0
		for x in range(3):
			for y in range(3):
				num += self.scorecell(player,(x,y))
		return num
	def scorecell(self,player,pos):
		num = 0
		for dx in range( 2 if pos[0] == 0 else 1):
			for dy in range( 2 if pos[1] == 0 else 1):
				if dx !=0 and dy!=0 :
					num += 1
					for n in range(3):
						if self.board[pos[0]+n*dx][pos[1]+n*dy] != player :
							num -= 1
							break
		return num
	def isfinished(self):
		if len(self.players) == 0 :
			return True
		scores = self.score()
		for key in scores:
			if scores[key]!=0 :
				return True
		return False
	def validate(self,player,move):
		if player not in self.players :
			return False
		if self.players.index(player)!=self.currentplayer :
			return False
		if not isinstance(move,dict):
			return False
		if "x" not in move or "y" not in move :
			return False
		indexrange = range(3)
		if move["x"] not in indexrange or move["y"] not in indexrange :
			return False
		if self.board[move["x"]][move["y"]] is not None :
			return False
		return True
	def execute(self,player,move):
		self.board[move["x"]][move["y"]] = player
		self.currentplayer = (self.currentplayer+1)%len(self.players)
		return True
	def getstate(self,player):
		return self.board