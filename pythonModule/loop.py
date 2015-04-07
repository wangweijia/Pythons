print 'range'

s = 'abcdefghijk'
for i in range(0,len(s),1):
    print s[i]

print 'enumerate'

for (index,char) in enumerate(s):
    print index,char

print 'zip'
ta = [1,2,3]
tb = [4,5,6]
tc = [7,8,9]
for (a,b,c) in zip(ta,tb,tc):
    print 'a:',a,'b:',b,'c:',c
