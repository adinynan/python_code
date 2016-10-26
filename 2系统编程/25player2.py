
#!/usr/bin/python

from time import ctime,sleep
import threading

def music(func):
    print('I was listening to music %s .%s'%(func,ctime()))
    sleep(2)

def move(func):
    print('I was at the movie %s! %s'%(func,ctime()))
    sleep(5)

def player(name):
    r = name.split('.')[1]
    if r == 'mp3':
        music(name)
    elif r == 'mp4':
        move(name)
    else:
        print('error')

l = ['baby.mp3','Avatar.mp4']

threads = []
files = range(len(l))

for i in files:
    t = threading.Thread(target = player,args = (l[i],))
    threads.append(t)

if __name__ == '__main__':
    for t in files:
        t.threads[i].start()
    for i in files:
        t.threads[i].join()

    print("all over %s"%ctime())
