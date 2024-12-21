import random

def get_greetings():
    """Returns a list of greetings."""
    return [
        "Hello, World!",
        "Hi there, Raspberry Pi enthusiast!",
        "Greetings, Earthling!",
        "Hey! Welcome to the tutorial.",
        "Hello from Python on Raspberry Pi!"
    ]

def choose_greeting(greetings):
    """Selects and returns a random greeting from the list."""
    return random.choice(greetings)

def print_greeting(message):
    """Prints the provided message to the console."""
    print(message)

def main():
    """Main function to run the program."""
    greetings = get_greetings()  # Get the list of greetings
    message = choose_greeting(greetings)  # Pick a random greeting
    print_greeting(message)  # Print the chosen greeting

# Entry point of the script
if __name__ == "__main__":
    main()

