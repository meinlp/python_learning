formatter = "%s %s %s %s"

print (formatter % (1, 2, 3, 4))
print (formatter % ("раз", "два", "три", "четыре"))
print (formatter % (True, False, False, True))
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter % (
        "Спят в конюшне кони,",
        "начал пес дремать,",
        "только мальчик Джонни",
        "не ложится спать!"
))
