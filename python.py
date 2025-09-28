# Step 1: Select number of rows
n = 5  

# Step 2 & 3: Generate pyramid pattern using loops
for i in range(1, n+1):
    # Print spaces
    print(" " * (n-i), end="")  
    
    # Print increasing numbers
    for j in range(1, i+1):
        print(j, end="")
    
    # Print decreasing numbers
    for j in range(i-1, 0, -1):
        print(j, end="")
    
    print()  # Move to next line

# Step 4: Verify the correctness of pattern
