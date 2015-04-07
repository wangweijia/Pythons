def gen1():
    a = 100
    yield a
    a = a * 8
    yield a
    yield 1000
for i in gen1():
    print i

def gen2():
    for i in range(0,4,1):
        yield i

for i in gen2():
    print i
