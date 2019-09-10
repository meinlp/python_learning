# надо каким-то хуем превратить Don't panic! в on tap

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
#--------------------------
black_list=[ "D", "\'", "i", "!", "c" ]
white_list=['t', 'p', 'a']
templist=[]
i=1
while i<3:
    for letter in plist:
        if letter in black_list:
            plist.remove(letter)
    i=i+1
plist.pop()
for letter in plist:
    if letter in white_list:
        templist.extend(letter)
        plist.remove(letter)
for letter in templist:
    plist.insert(i, letter)
    i=i+2
#--------------------------
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
