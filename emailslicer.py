# Step 1: Get email input from the user
email = input("Enter your email address: ")

# Step 2: Split the email at the '@' symbol
username, domain = email.split('@')

# Step 3: Display the results
print("Username:", username)
print("Domain:", domain)
