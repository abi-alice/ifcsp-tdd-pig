def pig_latin(text):
    vowels = "aeiou"
    lower_text = text.lower()
    words = lower_text.split()
    result = []

    for word in words:
        if word[0] in vowels:
            pig_word = word + "yay"
        else:
            first_vowel = 0
            for i, char in enumerate(word):
                if char in vowels:
                    first_vowel = i
                    break
            pig_word = word[first_vowel:] + word[:first_vowel] + "ay"
        
        result.append(pig_word)
    return " ".join(result)