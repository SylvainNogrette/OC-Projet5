words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]
vowels = ["a","e", "i", "o", "u", "y"]
result = []
for word in words:
    number_of_vowels_in_word = len([x for x in word if x in vowels])
    result.append((word, number_of_vowels_in_word))
print(result)

