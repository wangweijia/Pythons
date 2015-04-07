x1 = [1,3,5]
y1 = [9,12,13]
L = [ (x**2,y) for (x,y) in zip(x1,y1) if y > 10]

for i in L:
    print i
