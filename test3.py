from itertools import product

def solution(n, m, x_axis, y_axis):
    dims = dict()
    dots = list(product(x_axis+[n],y_axis+[m]))

    for x,y in dots:
        dims[(x,y)] = x * y
        if len(dims) > 1:
            for k,v in dims.items():
                if (x > k[0] and y >= k[1]) or (x >= k[0] and y > k[1]) :
                    dims[(x,y)] -= v

    return max(dims.values())