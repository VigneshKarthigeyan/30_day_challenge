# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n=int(input())
    phoneNumber={}
    while n!=0:
        lst=list(input().rstrip().split())
        phoneNumber[lst[0]]=int(lst[1])
        n-=1
    lst=[]
    while True:
        try:
            query=input()
            if query!='':
                lst.append(query)
            else:
                break
        except EOFError:
            break
    for query in lst:
        if query in phoneNumber:
            print("%s=%d"%(query,phoneNumber[query]))
        else:
            print("Not found")
