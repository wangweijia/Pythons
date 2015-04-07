ta = [1,2,3]
tb = [9,8,7]

zipped = zip(ta,tb)
print(zipped)


na,nb = zip(*zipped)
print(na,nb)

