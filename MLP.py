from Player_mlp import Player_mlp
import numpy as np
import copy

class MLP_p(Player_mlp):

	def think(self,board,availables):
		if len(availables) == 0:
			return 0,0,0
		if len(availables) == 1:
			x, y = availables[0]
			return x,y , self.stone
		_value = []
		for available in availables:
			copy_board = copy.deepcopy(board)
			x, y = available
			copy_board.put(x,y,self.stone)
			_value.append(MLP().train(self.get_future_vector(copy_board),self.W1,self.W2))
		x, y = availables[_value.index(max(_value))]
		return x, y, self.stone
		
	def getGameResult(self,board,opponent_player=None):
		pass

	# 6 x 6 boad  future vector
	# def get_future_vector(self,board):
	# 	f1, f2 = board.corner(self.stone)
	# 	f3, f4 = board.around_corner(self.stone)
	# 	f5 = board.difference_stone(self.stone)
	# 	f6 = board.blank_count()
	# 	return np.array([f1,f2,f3,f4,f5,f6])

	# 4 x 4 boad future vector
	# def get_future_vector(self,board):
	# 	f1, f2 = board.corner(self.stone)
	# 	f3 = board.difference_stone(self.stone)
	# 	f4 = board.blank_count()
	# 	f5 = board.center_stone(self.stone)
	# 	return np.array([f1,f2,f3,f4,f5])

	def get_future_vector(self,board):
		f1, f2 = board.corner(self.stone)
		f3 = board.difference_stone(self.stone)
		f4 = board.blank_count()
		f5, f6 = board.around_corner(self.stone)
		f7, f8 = board.outside_stone(self.stone)
		f9 = board.center_around(self.stone)
		return np.array([f1,f2,f3,f4,f5,f6,f7,f8,f9])
		
class MLP():
    def sigmoid(self, x):
        y = 1 / (1 + np.exp(-x))
        return y

    def train(self, vector, w1, w2):
        layer_z1 = np.dot(vector, w1)
        layer_a1 = self.sigmoid(layer_z1)
        layer_z2 = np.dot(layer_a1, w2)
        return layer_z2