string = "ABCDEFG"
for c in range(len(string),0,-1):
    print(" "*(len(string)-c)+" ".join(string[:c]))
