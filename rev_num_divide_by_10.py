def reverse_number():
    # Get input from the user
    number = int(input("Please enter a number: "))
    
    # Reverse the number
    reversed_number = 0
    
    while number > 0:
        # Get the last digit of the number
        digit = number % 10
        # Add the digit to the reversed number
        reversed_number = reversed_number * 10 + digit
        # Remove the last digit from the number
        number = number // 10
    
    # Display the reversed number
    print(f"The reversed number is: {reversed_number}")

# Call the function to run the program
reverse_number()