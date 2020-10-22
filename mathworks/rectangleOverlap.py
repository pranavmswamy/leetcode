class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # sort x coord for rec1 and rec2
        # sort y coord for rec1 and rec2
        # if both intersect, then the rectangles overlap.
        
        rec1_x = sorted([rec1[0], rec1[2]])
        rec1_y = sorted([rec1[1], rec1[3]])
        
        rec2_x = sorted([rec2[0], rec2[2]])
        rec2_y = sorted([rec2[1], rec2[3]])
        
        # base cases - check if it is a line and not a rect. then return false
        if rec1_x[1] - rec1_x[0] == 0:
            return False
        if rec1_y[1] - rec1_y[0] == 0:
            return False
        if rec2_x[1] - rec2_x[0] == 0:
            return False
        if rec2_y[1] - rec2_y[0] == 0:
            return False
            
        
        # choose first rect and second_rect according to sorted order of x and y; in order to compare (see which rect comes first in the cartesian plane).
        first_x = second_x = None
        
        if rec1_x[0] < rec2_x[0]:
            first_x = rec1_x
            second_x = rec2_x
        else:
            first_x = rec2_x
            second_x = rec1_x
        
        first_y = second_y = None
        
        if rec1_y[0] < rec2_y[0]:
            first_y = rec1_y
            second_y = rec2_y
        else:
            first_y = rec2_y
            second_y = rec1_y
        
        
        # they overlap iff both x and y coords overlap.
        if first_x[1] > second_x[0] and first_y[1] > second_y[0]:
            return True
        
        return False



# better soln
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        # edge cases - when its a line
        if rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3]:
            return False
        
        
        # We can compare like this because we know that 0th coord is < 2nd coord and 1st coord is less than 3rd coord
        
        # left = rec1 is to the left of rec2?
        left = rec1[2] <= rec2[0]
        
        # right = rec1 is to the right of rec2?
        right = rec1[0] >= rec2[2]
        
        # top = rec1 above rec2?
        top = rec2[3] <= rec1[1]
        
        # below = rec1 below rec2?
        below = rec2[1] >= rec1[3]
        
        # if any of the above conditions are true, then the rectangles dont overlap.
        
        return not (left or right or top or below)
