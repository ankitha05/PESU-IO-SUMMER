values = input("Input numbers of the list : ")
list1 = values.split(",")
list = []
for i in list1:
	list.append(int(i))
def binarySearch (list, l, r, x): 
    if r >= l: 
  
        mid = l + (r - l)/2
  
        if list[mid] == x: 
            return mid 
        elif list[mid] > x: 
            return binarySearch(list, l, mid-1, x)  
        else: 
            return binarySearch(list, mid+1, r, x) 
  
    else: 
        return -1

x=input("Enter the element to be searched")
result = binarySearch(list, 0, len(list)-1, x) 
  
if result != -1: 
    print("Element is present at index %d",result) 
else: 
    print("Element is not present in array")


