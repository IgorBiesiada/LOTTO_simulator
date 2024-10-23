from random import randint

# Initialize the list to store the random Lotto numbers
LOTTO = []

# Generate 6 unique random Lotto numbers between 1 and 49
while len(LOTTO) < 6:
    lotto_numbers = randint(1, 49)
    if lotto_numbers not in LOTTO:  # Avoid duplicate numbers
        LOTTO.append(lotto_numbers)

# List to store player's chosen numbers
player_numbers = []

# Allow the player to input 6 valid numbers between 1 and 49
while len(player_numbers) < 6:
    try:
        player_choice = int(input('Enter your number:'))

        # Check if the number is within the valid range
        if player_choice < 1 or player_choice > 49:
            print('Number must be between 1 and 49')
        # Ensure the player doesn't enter duplicate numbers
        elif player_choice in player_numbers:
            print('You already put this number')
        else:
            player_numbers.append(player_choice)  # Add the valid number
    except ValueError:
        # Handle invalid input that cannot be converted to an integer
        print('Please enter a valid number!')


# Function to check how many Lotto numbers the player guessed correctly
def check_lotto(LOTTO, player_numbers):
    # Find the common numbers between Lotto and player's choices using set intersection
    guessed_numbers = len(set(LOTTO) & set(player_numbers))

    # If the player guessed more than 2 numbers, it's a win; otherwise, it's a loss
    if guessed_numbers > 2:
        print(f'Congratulations! You guessed {guessed_numbers} numbers!')
    else:
        print(f'Sorry, you guessed only {guessed_numbers} numbers.')


# Call the function to check and print the result
check_lotto(LOTTO, player_numbers)