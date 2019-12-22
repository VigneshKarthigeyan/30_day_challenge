# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    T=int(input())
    lst=[]
    if T>=1 and T<=10:
        for i in range(0,T):
            S=input()
            lst.append(S)
    for i in range(0,lst.__len__()):
        S = lst[i]
        if S.__len__() >= 2 and S.__len__() <= 10000:
            arr1 = []
            arr2 = []
            for i in range(0, S.__len__()):
                if i % 2 == 0:
                    arr1.append(S[i])
                else:
                    arr2.append(S[i])
            for i in range(0, arr1.__len__()):
                print(arr1[i], end='')
                if i == arr1.__len__() - 1:
                    print(end=" ")
            for i in arr2:
                print(i, end='')
            print()

