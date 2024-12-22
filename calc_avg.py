def Calculate_avg():
    numbers = [] # List to store the numbers entered by the user.
    while True:
        try:
            # Get user input for a number. If the input is '-1', break the loop.
            num = float(input("Enter a number (or '-1' to quit): "))
            if num == -1:
                break
            numbers.append(num) # Add the number to the list.
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nProcess interrupted. Exiting program.")
            break
    if numbers:
        avg = sum(numbers) / len(numbers) # Calculate the average.

        print(f"The average is: {avg}")
    else:
        print("No numbers were entered.")
# Call the function to calculate the average.
Calculate_avg()           