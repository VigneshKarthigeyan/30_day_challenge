# Enter your code here. Read input from STDIN. Print output to STDOUT
def isPrime(n):
    if n==1:
        return 0
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0 and i!=n:
            return 0
    return 1
if __name__=="__main__":
    n=int(input())
    while n>0:
        if isPrime(int(input())):
            print("Prime")
        else:
            print("Not prime")
        n-=1
