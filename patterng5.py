n=int(input())
for i in range(n//2+1):
    if i==n//2:
        for j in range(n):
            print("*",end="")
    else:
        for j in range(i,n//2):
            print(" ",end="")
        for j in range(i+1):
            if i==0:
                print("*",end="")
            else:
                print(" ",end="")
        for j in range(i):
            if j==i-1:
                print("*",end="")
            else:
                print(" ",end="")
    print("")
for i in range(n//2):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n//2):
        if i==n//2-1:
            print("*",end="")
        else:
            print(" ",end="")
    for j in range(i+1,n//2):
        if j==n//2-1:
            print("*",end="")
        else:
            print(" ",end="")
    print("")
