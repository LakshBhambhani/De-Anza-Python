word = input("Enter a word to check if it's palindrome")

half = len(word)/2

if word == word[::-1]:
    print("It's a plaindrome")
else:
    print("It's not a palindrome")