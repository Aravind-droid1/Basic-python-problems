#selection sort for a series of numbers
class solution(object):
    def selection_sort(self,a):
        n=len(a)
        for i in range(n-1):
            #min saves the index number alone not the actual value of that index number
            min=i
            for j in range(i+1,n):
                if a[j]<a[min]:
                    min=j
            #it interchanges the numbers of that index
            a[min],a[i]=a[i],a[min]
        print(a)

a1=[2,5,7,3,1,4,6]
a2=[3,5,7,1,4,6,2]
obj=solution()
obj.selection_sort(a1)
obj.selection_sort(a2)