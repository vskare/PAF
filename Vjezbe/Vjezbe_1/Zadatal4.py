def jednadzba_pravca(x1,y1,x2,y2):
    k = (y2-y1)/(x2-x1)
    l = y1 - k*x1
    print("y = {}x + {}".format(k,l))
x1 = float(input("Unesite x koordinatu prve tocke: "))
y1 = float(input("Unesite y koordinatu prve tocke: "))
x2 = float(input("Unesite x koordinatu druge tocke: "))
y2 = float(input("Unesite y koordinatu druge tocke: "))
jednadzba_pravca(x1,y1,x2,y2)