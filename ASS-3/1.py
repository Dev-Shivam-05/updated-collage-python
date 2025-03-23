s = """Create a Python program that stores a paragraph using triple quotes and extracts all sentences that contain a specific word.Write a function that extracts and prints the first half and second half of a given string separately.Write a function that takes two strings and concatenates them with a space in between. If the second string is empty, return only the first string"""
print(s)
w=input("Enter the word: ")
s1=s.split(".")
for s1 in s1:
    if w in s1:
        print(s1)