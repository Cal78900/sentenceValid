# function to check if a sentence is valid based on specified rules
def is_valid_sentence(sentence):
    # Rule 1: String starts with a capital letter.
    if not sentence[0].isupper():
        return False

    # Rule 2: String has an even number of quotation marks.
    if sentence.count('"') % 2 != 0:
        return False

    # Rule 3: String ends with one of the specified sentence termination characters.
    if not sentence.endswith(('.', '?', '!')):
        return False

    # Rule 4: String has no period characters other than the last character.
    if '.' in sentence[:-1]:
        return False

    # Rule 5: Numbers below 13 are spelled out.
    words = sentence.split()
    for word in words:
        # Check if the word is a spelled-out number below 13
        spelled_out_numbers = ["one", "two", "three", "four", "five", "six", "seven",
                               "eight", "nine", "ten", "eleven",
                               "twelve"]

        # Remove punctuation from the word for comparison
        cleaned_word = ''.join(char for char in word if char.isalnum())

        # Check if the cleaned word is a spelled-out number below 13
        if cleaned_word.lower() in spelled_out_numbers:
            return False

        # Check if the word is a digit and less than 13
        if cleaned_word.isdigit() and int(cleaned_word) < 13:
            return False

    # All rules passed, the sentence is valid.
    return True


# Print rules for validation
print('Rules for validation:\n'
      'String starts with a capital letter.\n'
      'String has an even number of quotation marks.\n'
      'String ends with one of the following sentence termination characters: "." , "?", "!"\n'
      'String has no period characters other than the last character.\n'
      'Numbers below 13 are spelled out (”one”, “two”, "three”, etc…).\n')

# Get input from the user
user_input = input("Enter a sentence: ")

# Check if the input is a valid sentence
result = is_valid_sentence(user_input)

# Display the result
if result:
    print("This is a valid sentence.")
else:
    print("This is not a valid sentence.")
