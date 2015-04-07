with open("new.txt","w") as f:
    print f.closed
    f.write("hello word")
print f.closed
