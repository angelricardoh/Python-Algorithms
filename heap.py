import heapq

# initializing list
li = [5, 7, 9, 1, 3]
  
# using heapify to convert list into heap
heapq.heapify(li)
  
# printing created heap
print ("The created heap is : ",end="")
print (list(li))
  
# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li,4)
  
# printing modified heap
print ("The modified heap after push is : ",end="")
print (list(li))
  
# using heappop() to pop smallest element
print ("The popped and smallest element is : ",end="")
print (heapq.heappop(li))


listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    
heapq.heapify(listForTree)             # for a min heap
heapq._heapify_max(listForTree)        # for a maxheap!!

print(heapq.heappop(listForTree))