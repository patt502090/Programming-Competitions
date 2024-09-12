def solve():
    n, k = map(int, input().split())
    
    # Calculate the total sum of the array
    total_sum = (n * (2 * k + n - 1)) // 2  # Sum of k to k+n-1
    
    min_diff = float('inf')  # Initialize minimum difference
    current_sum = 0  # Running sum for the first i elements
    
    # Iterate through possible values of i
    for i in range(1, n + 1):
        current_sum += (k + i - 1)  # Add the current element (k + (i - 1))
        # Calculate the absolute difference
        diff = abs(2 * current_sum - total_sum)
        # Update the minimum difference
        min_diff = min(min_diff, diff)
    
    print(min_diff)

# Read the number of test cases
for _ in range(int(input())):
    solve()
