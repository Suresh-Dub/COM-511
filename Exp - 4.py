#Linear search  
 list = [1,2,3,4,5,6,7,8,9] 
 length = len(list) 
 x = int(input("Enter the target element for linear search:")) 
  
 for i in range(length + 1): 
     if(x==i): 
         print("Linear Search: The element is found at index",i) 
         break 
     elif(i==length): 
         print('The element is not found')  
  
  
 #Binary Search 
  
 my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
 x = int(input("Enter the target element for binary search: ")) 
  
 low = 0 
 high = len(my_list) - 1 
  
 found = False  # Initialize a variable to keep track of whether the element was found or not 
  
 while low <= high: 
     mid = (low + high) // 2 
     if x == my_list[mid]: 
         print("Binary Search: The element is found at index", mid) 
         found = True 
         break 
     elif x < my_list[mid]: 
         high = mid - 1 
     else: 
         low = mid + 1 
  
 if not found: 
     print('Binary Search: The element is not found')
