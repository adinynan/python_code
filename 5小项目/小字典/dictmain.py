#!/usr/bin/python

import MySQLdb
import sys
import time

def history(db):
    cursor = db.cursor()
    sql = sql = "select * from history"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        word = row[0]
        time = row[1]
        print "searched word: %s , time: %s"%(word,time)

def dict(db):

    cursor = db.cursor()

    while True:

        s = raw_input('word(out:##):')
        tm = time.localtime()
        t = "%4d-%02d-%02d  %02d:%02d:%02d"%(tm.tm_year,tm.tm_mon,tm.tm_mday,tm.tm_hour,tm.tm_min,tm.tm_sec)
        t = str(t)

        sql = "insert into history values('%s','%s')"%(s,t)
        cursor.execute(sql)
        db.commit()
:
        string = "%s   "%s
        f = open('dict.txt')

        if s == '##':
            break

        try:
            for line in f:
                if string in line and s[0] == line[0] and s[len(s)-1] == line[len(s)-1]:
                    print line
            f.next()
        except:
           pass

def personal(db):
    while True:
        print '''
    ----------------------------------
    ---1:search   2:history  3:quit---
    ----------------------------------
          '''
        i = input('please select:')
        if i not in [1,2,3]:
            print "error!"
            continue
        elif i == 1:
            dict(db)
        elif i ==2:
            history(db)
        else:
            print "Thank you for use!"
            sys.exit()

def register(db):
    cursor = db.cursor()
    while True:
        name = raw_input("input name(str)>>")
        sql = "select * from usrname where name = '%s'"%name
        cursor.execute(sql)
        data = cursor.fetchone()

        if not data:
            break
        else:
            print "sorry existed"

    passwd = input("input  password(str)>>")

    sql = "insert into usrname values('%s',%d)"%(name,passwd)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        print "sorry, failed!"
        db.rollback()

    print "register ok!"

def login(db):
    cursor = db.cursor()
    name = raw_input("name(str):")
    passwd = input("password(int):")

    sql = "select * from usrname where name = '%s' and password = %d"%(name,passwd)
    cursor.execute(sql)
    data = cursor.fetchone()

    if data == None:
        print "sorry,error!"
        return
    else:
        personal(db)

def main():
    db = MySQLdb.connect('localhost','root','1','dictuser')
    while True:
        print '''
        --------------command---------------
        ----1:login   2:register   3:quit---
        ------------------------------------
              '''
        num = input("please select:")

        if num not in [1,2,3]:
            print "input error!"
            sys.stdin.flush()
            continue
        elif num == 1:
            login(db)
        elif num == 2:
            register(db)
        else:
            db.close()
            print "Thank you for use!"
            return

if __name__ == "__main__":
    main()
