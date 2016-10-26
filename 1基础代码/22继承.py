#!/usr/bin/python


class Calculator():
    name = "luosifu"

    age = 88

class Talker():
    name = "liyong"

    sex = 'man'

class TalkCalculator(Calculator,Talker):
    pass


A = TalkCalculator()

print A.name
print A.sex
