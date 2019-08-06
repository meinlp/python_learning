vovels = "a, i, o, e, y, u"

word = input("Print word to scan for vovels: ")
found = []
for letter in word:
    if letter in vovels:
        if letter not in found:
            found.append(letter)
print("Vovels in this word: ", found)
