def kth_greatest_number(arr, k):
    # Sort the array in descending order
    arr.sort(reverse=True)

    # Check if k is within the valid range
    if 1 <= k <= len(arr):
        return arr[k - 1]
    else:
        return None

arr=[]
n=int(input("enter the number "))
for i in range(n):
    a=int(input("enter the elements"))
    arr.append(a)
k = int(input("Enter the value of k: "))

result = kth_greatest_number(arr, k)

if result is not None:
    print(f"The {k}th greatest number in the array is: {result}")
else:
    print("Invalid value of k.")
