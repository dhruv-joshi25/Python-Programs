import random

# Define dictionaries for each character set
lower = list('abcdefghijklmnopqrstuvwxyz')
upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
digits = list('0123456789')
special = list('!@#$%^&*()')

# Define a function to generate a random password
def generate_password(length):
    # Make sure the length is at least 4
    if length < 4:
        raise ValueError('Password length must be at least 4')

    # Initialize the password as an empty list
    password = []

    # Choose at least one character from each set
    password.append(random.choice(lower))
    password.append(random.choice(upper))
    password.append(random.choice(digits))
    password.append(random.choice(special))

    # Fill the rest of the password with random characters
    for i in range(length - 4):
        # Choose a random character set
        charset = random.choice([lower, upper, digits, special])
        # Choose a random character from the set
        password.append(random.choice(charset))

    # Shuffle the password to make it more random
    random.shuffle(password)

    # Convert the password to a string and return it
    return ''.join(password)

# Get the desired length of the password from the user
length = int(input('Enter the desired length of the password: '))

# Generate the password and print it
password = generate_password(length)
print('Your random password is:', password)
