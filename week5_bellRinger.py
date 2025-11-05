# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.
# phrase1="abracadabra"
# print(phrase1[4])
# # b. Retrieve the second to last character. 
# print(phrase1[-2])
# # c. Find the first occurrence of the letter 'c'.
# #  letter_to_find = "c"
# print(phrase1.find(letter_to_find))
#  # Advanced Slicing:
#  # Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
#  phrase2= "abcdefghijklmnopqrstuvwxyz"
# # a. Extract the letters 'hij'.
#  print(phrase2[7:10])
#  # b. Extract every second letter starting from 'a' to 'm'.
# phrase3="abcdefghijklm"
# print(phrase3[::2])

# substring=phrase2[:13]
# result=substring[::2]
# print (result)
# # c. Reverse the entire string using slicing.
# reversedphrase2 = phrase2[::-1] #the third part of the [::] 
# print(reversedphrase2)
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"

# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
info= "Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
# b. Extract every third word.
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
reversed_word_positions = info.split()[::-1]
reversed_word_positions = ' '.join(reversed_word_positions)
print("Reversed word positions:", reversed_word_positions)

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
text = "MAY THE FORCE BE WITH YOU."
lowercase_text = text.lower()
print("Lowercase:", lowercase_text)
# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
otto = ["Make", "haste", "slowly."]
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.
motto_str = ' '.join(motto_str)
print("Single string:", motto_str)
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".
split_motto = motto_str.split('a')
print("Split at 'a':", split_motto)

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.
phrase5= "Supercalifragilisticexpialidocious"
lettercount= "i"
count