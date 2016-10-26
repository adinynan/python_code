#!/usr/bin/python
#coding=utf-8

# 日期格式2016-1-1

f_leap = 0
days = 0
DayMon = {'mon1':31,'mon2':28,'mon3':31,'mon4':30,'mon5':31,'mon6':30,'mon7':31,'mon8':31,'mon9':30,'mon10':31,'mon11':30,'mon12':31}

data = raw_input("Enter as 2016-1-1>>")

data = data.split('-')

year = int(data[0])
mon = int(data[1])
day = int(data[2])

print "%d-%d-%d"%(year,mon,day)

if year < 0 or mon < 1 or mon > 12 or day < 1 or day > 31:
    print "Invalid data"
    exit()

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    f_leap = 1
    if mon == 2 and day > 29:
        print "Invalid data"
        exit()
elif mon == 2 and day > 28:
    print "Invalid data"
    exit()

if mon == 4 or mon == 6 or mon == 9 or mon == 11:
    if day > 30:
        print "Invalid data"
        exit()

for i in range(1,mon):
#    l = ['mon',str(i)]
#    s = ''.join(l)
    s = 'mon' + str(i)
    days += DayMon[s]

if mon > 2:
    days += f_leap

days += day

print "days = ",days

