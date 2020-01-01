#Write your code here
class Calculator:
    def power(self,a,b):
        if a==abs(a) and b==abs(b):
            res=1
            for _ in range(b):
                res*=a
            return res
        return "n and p should be non-negative"

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)