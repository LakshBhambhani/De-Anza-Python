# Vowel/Consonant check

vowel = ['a', 'e', 'i', 'o', 'u']

input = str(input("Enter an alphabet to check if it's a vowel or a consonant"))
if(vowel.__contains__(input)):
    print("It's a vowel")
else:
    print("It's a consonant")