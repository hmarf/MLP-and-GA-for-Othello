import numpy as np

class Player_mlp:

    def __init__(self, stone, name, w):#_input, _hidden, _output):
        self.stone = stone
        self.name = name
        self.w1, self.w2 = w[:162], w[162:]

    def split_list(self,l,n):
        a = len(l)
        return [l[i:i+n] for i in range(0,a,n)]
        
    def play(self, board):
        self.W1 = np.array(self.split_list(self.w1,18))
        self.W2 = np.array(self.split_list(self.w2,1))
        availables = board.availables(self.stone)
        return self.think(board, availables)
    
    def get_w(self):
        return W1, W2
