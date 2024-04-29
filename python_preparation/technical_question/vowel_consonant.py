def vowel_or_consonant(letter):
    vowel = "aeiouAEIOU"

    if letter in vowel:
        return "vowel"
    elif letter.isalpha():
        return "consonant"
    else:
        return "invalid"

letter = input("Enter a letter of alphabet : ")

if len(letter)==1:
    result = vowel_or_consonant(letter)
    print(f"the letter '{letter}' is a {result}.")
else:
    print("Enter a single letter.")
