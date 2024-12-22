def process_numbers():
    # List to store all numbers entered by the user
    all_numbers = []
    
    # Ask the user to enter at least five numbers
    print("Please enter at least five numbers. Enter 'done' to stop:")
    
    while True:
        user_input = input("Enter a number: ")
        
        # Stop input collection if the user types 'done'
        if user_input.lower() == 'done':
            if len(all_numbers) < 5:
                print("You need to enter at least 5 numbers.")
                continue
            break
        
        try:
            # Convert input to an integer and add to the list
            number = int(user_input)
            all_numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Get the last five numbers entered
    last_five = all_numbers[-5:]
    print(f"The last five numbers entered are: {last_five}")
    
    # Calculate the sum of the last five numbers
    total_sum = sum(last_five)
    
    # Calculate the average of the last five numbers
    average = total_sum / len(last_five)
    
    # Reverse each of the last five numbers
    reversed_numbers = [int(str(num)[::-1]) for num in last_five]
    
    # Display the results
    print(f"Sum of the last five numbers: {total_sum}")
    print(f"Average of the last five numbers: {average}")
    print(f"Reversed forms of the last five numbers: {reversed_numbers}")
    
    # Count even and odd numbers in the entire list
    even_count = len([num for num in all_numbers if num % 2 == 0])
    odd_count = len([num for num in all_numbers if num % 2 != 0])
    
    # Display the counts
    print(f"Total even numbers entered: {even_count}")
    print(f"Total odd numbers entered: {odd_count}")

# Run the program
process_numbers()