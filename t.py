#!/usr/bin/env python


import subprocess
from threading import Thread
from Queue import Queue

num_threads = 3
ips = ['127.0.0.1', '10.103.13.156','10.103.13.145']
q = Queue()


def pingme(i, queue):

    while True:
        ip = queue.get()
        print 'Thread %s pinging %s ' % (i, ip)
        ret = subprocess.call('ping -c 1 %s' % ip, shell=True, stdout=open('c;/'), stderr=subprocess.STDOUT)
        if ret == 0:
            print '%s is alive!' % ip
        else:
            print '%s is down...' % ip

# start threads
for i in xrange(num_threads):
    t = Thread(target=pingme, args=(i, q))
    t.setDaemon(True)
    t.start()

for ip in ips:
    q.put(ip)

print 'main thread waiting...'
q.join()
print 'Done..'

if __name__ == '__main__':
    pass