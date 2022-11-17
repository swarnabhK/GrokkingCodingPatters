def max_array_size_k(arr,k):
  windowSum,windowStart = 0,0
  max_sum = 0
  max_array_start,max_array_end= 0,0
  for end in range(len(arr)):
    windowSum+=arr[end]
    if(end>=k-1):
      if windowSum>max_sum:
        max_sum = windowSum
        max_array_start = windowStart
        max_array_end = end
      windowSum-=arr[windowStart]
      windowStart+=1
  return max_sum,max_array_start,max_array_end


arr = [2, 1, 5, 1, 3, 2]
max_sum,max_array_start,max_array_end = max_array_size_k(arr,3)

print("Maximum sum array is: ",arr[max_array_start:max_array_end+1], ", sum is : ",max_sum)