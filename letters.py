# First, let's define a list of letters
import random
consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'W', 'Y',
                  'Z']
vowels = ['A', 'E', 'I', 'O', 'U']
number_of_vowels = int(input("How many vowels do you want? [3,4,5]"))
if number_of_vowels > 5 or number_of_vowels < 3:
        print("Number of vowels must be between 3 and 5 inclusive")
        number_of_vowels = int(input("How many vowels do you want? [3,4,5]"))
vow = random.choices(vowels, weights=(15, 21, 13, 13, 5), k=number_of_vowels)
number_of_consonants = 9 - number_of_vowels
cons = random.choices(consonants, weights=(2, 3, 6, 2, 3, 2, 1, 1, 5, 4, 8, 4, 1, 9, 9, 9, 1, 1, 1, 1, 1),
                          k=number_of_consonants)
letters = [ops.lower() for ops in [*vow, *cons]]
print(letters)



user_word =  input("Input word using letters in the list provided")
#Defining a list of words that we want to check
with open('/usr/share/dict/words', 'r') as f:
    words = f.read().split()



# Now, we can iterate through the list of words and check if they can be made from the list of letters
all_possible = []
for word in words:
    remaining_letters = letters[:]
    can_make_word = True

    # Iterate through the letters in the word
    for letter in word:
        # Check if the letter is in the remaining letters list
        if letter in remaining_letters:
            # If it is, remove the letter from the list
            remaining_letters.remove(letter)
        else:
            # If the letter is not in the remaining letters list, we can't make the word
            can_make_word = False
            break


    # Print the result
    if can_make_word:
        all_possible.append(word)
print(all_possible)


score = 0
print(user_word)
if user_word in all_possible:
    score += len(user_word)
    print(f'score is {score}')

# Find the maximum length of the words
max_length = max(len(word) for word in all_possible)
# Use a list comprehension to find the longest words
longest_words = [word for word in all_possible if len(word) == max_length]
# Print the longest words
print(f"The longest words are: {longest_words}")






