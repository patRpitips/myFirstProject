def greet():
    """Returns the greeting message."""
    return "Hello, World!"

def print_greeting(message):
    """Prints the provided message to the console."""
    print(message)

def main():
    """Main function to run the program."""
    message = greet()  # Get the greeting message
    print_greeting(message)  # Print the greeting

# Entry point of the script
if __name__ == "__main__":
    main()
