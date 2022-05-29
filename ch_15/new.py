def FirstKelements(arr,size,k):

    our_list = []
    for i in range(k):
        our_list.append(arr[i])
     
    for i in range(k, size):
        our_list.sort()
         
      
        if (our_list[0] > arr[i]):
            continue
             
      
        else:
            our_list.pop(0)
            our_list.append(arr[i])
             
 
    for i in our_list:
        print(i, end = " ")
 

arr=[11, 3, 2, 1, 15, 5, 4,45, 88, 96, 50, 45]
size = len(arr)
 

k=3
FirstKelements(arr, size, k)
 
# This code is contributed by avanitrachhadiya2155