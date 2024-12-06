def remove_vowels(stri):
    vow = "aeiou"
    temp = ""
    for i in range(len(stri)):
        if stri[i].lower() in vow:
            temp = stri.replace(stri[i], "")
    return temp

def remove_vowels_reverse(stri):
    stri = remove_vowels(stri)
    temp = ""
    for i in range(len(stri)):
        temp = f"{temp}{stri[-i-1]}"
    return temp

print(remove_vowels_reverse(input("gimme a word: ")))