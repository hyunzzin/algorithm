import math
def solution(brown, yellow):
    iter = math.floor(yellow**(1/2))
    for w in range(1,iter+1):
        square = 0
        h = yellow / w
        if h.is_integer():
            square = 2*w + 2*h + 4
        if square == brown:
            if w >= h:
                return [w+2,h+2]
            else:
                return [h+2,w+2]
