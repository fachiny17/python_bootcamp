import math

def paint_calc(height, width, cover):
    num_of_can = (height*width)/cover
    round_up_can = math.ceil(num_of_can)
    print(f"You'll need {round_up_can} of paints.")
    
test_h = int(input())
test_w = int(input())
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage) 