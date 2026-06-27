# Problem 1: Given an array of integers, print all the elements of the array.
arr=[10,20,30,40,50]
for num in arr:
    print(num)

# Problem 2: Given an array of integers, find and print the sum of all elements.
arr=[10,20,30,40,50]
total_sum=0
for num in arr:
    total_sum+=num
print(total_sum)

# Problem 3: Given an array of integers, find and print the largest element.
arr=[10,20,30,40,50]
largest_num=arr[0]
for num in arr:
    if num>largest_num:
        largest_num=num
print(largest_num)

# Problem 4: Given an array of integers, find and print the smallest element
arr=[10,20,30,40,50]
smallest_num=arr[0]
for num in arr:
    if num<smallest_num:
        smallest_num=num
print(smallest_num)

# Problem 5: Given an array of integers, count how many even numbers are
# present.
arr=[10,11,17,20,23,30,40,50,3]
even_count=0
for num in arr:
    if num%2==0:
        even_count+=1
print(even_count)

# Problem 6: Given an array of integers, print only the odd numbers.
arr=[10,11,17,20,23,30,40,50,3]
for num in arr:
    if num%2!=0:
        print(num)

# Problem 7: Given an array of integers, count how many elements are greater
# than 10.
arr=[10,11,17,20,23,30,40,50,3]
greater_elements_count=0
for num in arr:
    if num>10:
        greater_elements_count+=1
print(greater_elements_count)

# Problem 8: Given an array of integers, create a new array containing the square
# of each element and print it.
arr=[10,11,17,20,23,30,40,50,3]
sqr_arr=[]
for num in arr:
    sqr_arr.append(num**2)
print(sqr_arr)

# Problem 9: Given an array of integers, print the elements in reverse order.
arr=[10,11,17,20,23,30,40,50,3]
reve_arr=[]
for num in arr[::-1]:
    reve_arr.append(num)
print(reve_arr)

# Problem 10: Given an array of integers, find the average of all elements.
arr=[10,11,17,20,23,30,40,50,3]
total_sum=0
for num in arr:
    total_sum+=num
    average=total_sum/len(arr)
print(average)


