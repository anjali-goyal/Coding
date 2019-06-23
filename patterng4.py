n=int(input())
for i in range(n//2+1):
    for j in range(i,n//2+1):
        print(" ",end="")
    for j in range(i+1):
        if i==n//2:
            print("*",end="")
        else:
            if j==0 or j==i:
                print("*",end="")
            else:
                print(" ",end="")
    for j in range(0,i):
        if i==n//2:
            print("*",end="")
        else:
            if j==i-1:
                print("*",end="")
            else:
                print(" ",end="")
    print("")
for i in range(n//2):
    for j in range(i+2):
        print(" ",end="")
    for j in range(i,n//2):
        if j==i or j==n//2-1:
            print("*",end="")
        else:
            print(" ",end="")
    for j in range(i+1,n//2):
        if j==n//2-1:
            print("*",end="")
        else:
            print(" ",end="")
    print("")
    
