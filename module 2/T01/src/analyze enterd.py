n=int(input())

even_count = 0
odd_count = 0
zero_count = 0
total = 0
for i in range(n):
    num=int(input())
    total+=num
    if num==0:
        zero_count+=1
    elif num>=0:
        even_count+=1
    else:
        odd_count+=1

print("Positive Count:",even_count)  
print("Negative Count:",odd_count)
print("Zero Count:",zero_count)
print("Total:",total)      

