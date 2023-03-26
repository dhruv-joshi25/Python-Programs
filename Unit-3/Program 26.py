# Open a file for writing
with open('names.txt', 'w') as f:
    # Read names from the keyboard until the user enters an empty string
    while True:
        name = input('Enter a name (or press enter to quit): ')
        if name == '':
            break
        # Write each name to the file, followed by a newline character
        f.write(name + '\n')