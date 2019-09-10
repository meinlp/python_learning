# надо каким-то хуем превратить Don't panic! в on tap

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
#--------------------------
for i in range(4):
    plist.pop()
plist.remove("\'")
plist.pop(0)
plist.extend([plist.pop(), plist.pop()])
plist.insert(3, plist.pop(2))
#--------------------------
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
