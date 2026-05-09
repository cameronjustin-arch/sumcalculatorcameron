# Ask the user to input a positive integer
user_num = int(input("Enter a positive integer: "))

# Initialize the sum at 0 to hold the running total
total_sum = 0

# Initialize a counter starting at 0
current_num = 0

# Use a while loop to iterate until the counter exceeds the user's number
while current_num <= user_num:
    # Add the current number to our running total
    total_sum += current_num
    
    # Increment the counter by 1 to move to the next integer
    current_num += 1

# Display the final calculated sum
print(f"The sum of the numbers from 0 to {user_num} is: {total_sum}")
