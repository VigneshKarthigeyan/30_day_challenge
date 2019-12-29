class Difference:
    maximumDifference=0
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        lst=self.__elements
        for i in range(0,len(lst)):
            for j in range(i+1,len(lst)):
                dif=abs(lst[i]-lst[j])
                if self.maximumDifference<dif:
                    self.maximumDifference = dif

	# Add your code here


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)