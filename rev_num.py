number = input("Enter a three-digit number: ")

# Check if the input is a three-digit number and contains only digits. If not, print an error message. 
if len(number) == 3 and number.isdigit():
    # Reverse the number to get the reversed number
    reversed_number = number[::-1]
    
    # Calculate the result by multiplying the reversed number by 2 and converting it to an integer. 
    result = int(reversed_number) * 2
    
    # Print the result
    print("The result is:", result)
else:
    print("Please enter a valid three-digit")