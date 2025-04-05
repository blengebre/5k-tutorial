if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    le=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k!=n:
                   le.append([i,j,k]) 
                else:
                    continue
    print(le)
    
