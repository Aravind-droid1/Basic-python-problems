#bubble sort algorithm
class solution(object):
    def bubble_sort(self,a):
        n=len(a)
        for i in range(n-1):
            for j in range(n-i-1):
                #here if the number next to is higher they would switch places
                if a[j]>a[j+1]:
                    a[j],a[j+1]=a[j+1],a[j]

        print(a)

a1=[2,5,6,3,1,4]
a2=[2,4,5,6,3,1]
obj=solution()
obj.bubble_sort(a1)
obj.bubble_sort(a2)