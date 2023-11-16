def find_target_indices(arr, target):
    start_index = None
    last_index = None

    for i in range(0,len(arr)):
        if target == arr[i]:
            if start_index is None:
                start_index = i 
            last_index = i 

    if start_index is not None:
        print(f"Target {target} found at indices: {start_index} to {last_index}")
    else:
        print(f"Target {target} not found in the array")

# Input the array elements
arr = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    a = int(input("Enter the array element: "))
    arr.append(a)

# Input the target
target = int(input("Enter the target: "))

# Call the function to find the target indices in the array
find_target_indices(arr, target)
