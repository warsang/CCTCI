#This is not the right approach. An approach that would work is to create
#a piece class which includes four edges
#And to create an edge class with a method fitswith which given a certain edge would
#return True if they fit together
#A bruteforce method to solving the puzzle would be to start by identifying the top left piece
#=> left edge and top edge are None, then testing edge by edge if the edges of other pieces
#fit with it's right edge.
#Then we would complete a row with this process and move on to the next row.
#Once we've gone through all rows, we only need to test one piece to know that a row
#fits with another


class piece(object):

    def __init__(self,top = None,bottom = None,left = None,right = None,location = None):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.location = location
        
    def belongs(self,edge):
        if edge == self.top or edge == self.bottom or edge == self.left or edge ==self.right:
            return True
        else:
            return False

    
def main():

    #Build 3x3 jigsaw:
    0_0 = piece()
    0_1 = piece()
    0_2 = piece()
    1_0 = piece()
    1_1 = piece()
    1_2 = piece()
    2_0 = piece()
    2_1 = piece()
    2_2 = piece()

    0_0.left = 0_1
    0_1.left = 0_2
    1_0.left = 1_1
    1_1.left = 1_2
    2_0.left = 2_1
    2_1.left = 2_2
    
    0_0.bottom = 1_0
    1_0.bottom = 2_0
    0_1.bottom = 1_1
    1_1.bottom = 2_1
    #And so on
    
