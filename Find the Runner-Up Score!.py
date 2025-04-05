if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    li=[]
    
    for i in arr:
        if i in li:
            continue
        else:
            li.append(i)
    li.sort()
    print(li[len(li)-2])
    
