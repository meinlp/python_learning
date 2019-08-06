#-*- coding: utf-8 -*-
x = u'Существует %d типов людей' % 10
binary = "Python"
do_not = u"нет"
y = u"Те, кто понимает %r, и те, кто - %s." % (binary, do_not)

print (x)
print (y)

print (u"Я сказал: %s." % x)
print (u"А еще я сказал: '%s'." % y)

hilarious = False
joke_evaluation = u"Разве это не смешно?! %r"

print (joke_evaluation % hilarious)

w = u"Это часть строки слева..."
e = u"Это часть строки справа."

print (w + e + e)
