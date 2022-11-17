def AvgSubarraysOfSizeKBrute(arr,k):
  #slice the array for each size of k.
  #findeach average and then add it to the result subarray
  res = []
  for i in range(len(arr)-k+1):
    avg = sum(arr[i:i+k])/k
    res.append(avg)
  return res

print(AvgSubarraysOfSizeKBrute([1, 3, 2, 6, -1, 4, 1, 8, 2],5))

def AvgSubarraysOfSizeKSliding(arr,k):
  start = 0
  end = 0
  res = []
  windowSum=0
  for i in range(len(arr)):
    windowSum+=arr[i]
    end+=1
    if(end>=k):
      res.append(windowSum/k)
      windowSum-=arr[start]
      start+=1
  return res    

AvgSubarraysOfSizeKSliding([1, 3, 2, 6, -1, 4, 1, 8, 2],5)


