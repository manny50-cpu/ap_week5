def manipuatingword():
    # Manipulating Words:
    # # Given the string info = "Python is fun. Fun is good. Good is subjective.",
    info= "Python is fun. Fun is good. Good is subjective."
    # # a. Extract the word 'subjective' without knowing its exact position.
    # # b. Extract every third word.
    # # c. Reverse the positions of the words, but keep the characters in each word in the same order.
    reversed_word_positions = info.split()[::-1]
    reversed_word_positions = ' '.join(reversed_word_positions)
    print("Reversed word positions:", reversed_word_positions)