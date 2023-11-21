# reverse every kth row in a matrix

test_list=[[2,6,7],
           [3,4,5],
           [11,5,71],
           [90,7,1],
           [99,1,11],
           [78,12,13]]
print("The original list is: " + str(test_list))
k=int(input("Enter the row value want to reverse:"))
res=[]
for idx,ele in enumerate(test_list):
    if(idx+1)%k==0:
        res.append(list(reversed(ele)))
    else:
        res.append(ele)
print("After reversing every kth row: "+ str(res))
