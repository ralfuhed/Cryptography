""" Crypto.py
    Implements a simple cypher
    Author: Rashed Al Fuhed
    Date: March 19, 2021"""

# Create two list of variables that are encoded into one another
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key =   "XPMGTDHLYONZBWEARKJUFSCIQV"

# Create a main function and define
def main():
  # Initialize keepGoing as true
  keepGoing = True
  # Start with the while loop
  while keepGoing:
    # Create a variable for menu function
    response = menu()
    # Create an if statement and state what to do if true
    if response == "1":
      # Create a user input and store into variable
      plain = input("text to be encoded: ")
      # Print out the encrypted text
      print(encode(plain))
    # Create an additional if statement
    elif response == "2":
      # Create a user input and store into variable
      coded = input("code to be decyphered: ")
      # Print out the decrypted text
      print (decode(coded))
    # Create one last if statement and state what to do if true
    elif response == "0":
      # Output a response
      print ("Thanks for doing secret spy stuff with me.")
      # Initialize keepGoing as false to stop the endless loop if this true
      keepGoing = False
    # Create an else statement and state what to do if all of the above is false
    else:
      # Output a response
      print ("I don't know what you want to do...")

# My starter code.

# Create a menu function and define it
def menu():
    # Output the options
    print("""
    SECRET DECODER MENU

0) Quit
1) Encode
2) Decode
""")
    # Get a response from the user (0-2)
    response = input("What is your choice? ")
    # Return to that response
    return response
    # Pass the function
    pass

# Create an encode function and which will restore the input in the variable "plain"
def encode(plain):
    # Make an empty string called output
    output = ""
    # Convert plain to all upper case
    plain = plain.upper()
    # For each character in plain
    for currentChar in plain:
        # Make an if condition and make it equals to -1, which means if there is any special character, ignore it
        if alpha.find(currentChar) == -1:
            continue
        # Find the location of that character in alpha and store it in a variable called position
        position = alpha.find(currentChar)
        # Find the character at that position in key and store it in a variable called newChar
        newChar = key[position]
        # Append newChar to output
        output += newChar
    # Return to output
    return output
    # Pass the function
    pass

# Create a decode function and which will restore the input in the variable "coded"
def decode(coded):
    # Make an empty string called output
    output = ""
    # convert coded to all upper case
    coded = coded.upper()
    # For each character in coded
    for currentChar in coded:
        # Make an if condition and make it equals to -1, which means if there is any special character, ignore it
        if key.find(currentChar) == -1:
            continue
        # Find the location of that character in key and store it in a variable called position
        position = key.find(currentChar)
        # Find the character at that position in alpha and store it in a variable called newChar
        newChar = alpha[position]
        # Append newChar to output
        output += newChar
    # return to output
    return output
    # Pass the function
    pass

if __name__ == "__main__":
    main()
