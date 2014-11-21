__author__ = 'Madeleine'


class Foo():
    notagoodidea = "What am I now?"

x = Foo()
x.notagoodidea = "Who knows."
y = Foo()
print(Foo.notagoodidea)
print(x.notagoodidea)
x.notagoodidea = "I'm lost"
print(x.notagoodidea)