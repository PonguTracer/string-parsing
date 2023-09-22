def extract_words(input_string):
    # Split the input string by a comma and remove any leading/trailing spaces
    words = [word.strip() for word in input_string.split(",")]
    return words

while True:
    user_input = input("Enter input string:\n")
    
    if user_input == 'q':
        break
    
    if ',' not in user_input:
        print("Error: No comma in string.\n")
    else:
        words = extract_words(user_input)
        if len(words) != 2:
            print("Error: Invalid input format. Please enter two words separated by a comma.\n")
        else:
            print(f"First word: {words[0]}")
            print(f"Second word: {words[1]}\n")
