# Program to count the frequency of a user-entered word in a text file.

word = input("Enter the word to search: ")

file = open("sample.txt", "r")

content = file.read()

file.close()

words = content.split()

count = 0

for w in words:
    if w == word:
        count += 1

print("Frequency:", count)