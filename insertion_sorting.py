class solution():
    def sort(self,a):
        l=len(a)
        for i in range(1,len(a)):
            insert_index=i
            current_value=a[i]
            for j in range(i-1,-1,-1):
                if a[j] > current_value:
                    a[j+1]=a[j]
                    insert_index=j
                else:
                    break
            a[insert_index]=current_value
        print(a)

obj=solution()
obj.sort(a=[5,4,2,3,6,1])
obj.sort(a=[6,7,3,4,2,9,1])
obj.sort(a=[8,3,4,1,5,2,6])