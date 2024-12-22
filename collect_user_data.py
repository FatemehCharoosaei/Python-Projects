import re

def is_valid_email(email):
    """
    Validates the email using a regex pattern.
    Returns True if the email is valid, otherwise False.
    """
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_pattern, email) is not None

def collect_user_data():
    # Dictionary to store user data
    user_data = {}

    print("Enter user details. Type 'done' when finished.")
    
    while True:
        # Get name, surname, and email from the user
        name = input("Enter first name (or 'done' to stop): ")
        if name.lower() == 'done':
            break
        surname = input("Enter last name: ")
        
        # Loop to validate the email input
        while True:
            email = input("Enter email address: ")
            if is_valid_email(email):
                break
            else:
                print("Invalid email format. Please enter a valid email.")

        # Store data in the dictionary with "name surname" as the key
        full_name = f"{name} {surname}"
        user_data[full_name] = email

    # Process and display user information
    for full_name, email in user_data.items():
        # Split the email into username and domain
        username, domain = email.split('@')
        print(f"{full_name} has username: '{username}' and domain: '{domain}'")

# Run the program
collect_user_data()