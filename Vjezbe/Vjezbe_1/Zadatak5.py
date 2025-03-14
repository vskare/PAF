import matplotlib.pyplot as plt
def jednadzba_pravca(x1,y1,x2,y2):
    k = (y2-y1)/(x2-x1)
    l = y1 - k*x1
    print("y = {}x + {}".format(k,l))
jednadzba_pravca(1,2,3,4)