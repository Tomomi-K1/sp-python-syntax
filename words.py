def print_upper_words(string_list, must_start_with):
    """
    prints out the words that starts with "must_start_with"letters in string_list in uppercase
    
    for example:
        print_upper_words(['apple', 'banana'], "b") => BANANA

    -string_list is list of string
    -must_start_with is a set of letters
    
    """
    for string in string_list:
        for letter in must_start_with:
            if letter == string[0]:
                print(string.upper())
