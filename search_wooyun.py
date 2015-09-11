#coding=utf-8
import re,sys,urllib,urllib2
import threading, time, sys, os
from Queue import Queue
import optparse

class checkweb(threading.Thread):
    
    def __init__(self, queue):

	threading.Thread.__init__(self)
	self.queue = queue
	self.uurl()
	self.found_count = 0


    def uurl(self):

	global regex
        reg1 = '(\d+\-\d+\"\>.*?('
        reg2 = ').*?\<\/a\>)'
	self.reg = reg1 + regex + reg2

    def run(self):

	global list,i,con

	while True: 

		if self.queue.qsize() == 0 and self.found_count > 30000: 
			break

  		if i>5:

			print "\nerror over 5 times\n"	
			sys.exit()

		#print self.queue.qsize(),threading.currentThread().getName()

		sub_getque = self.queue.get(timeout = 1.0)

		if sub_getque == 'quit': break
		
		con.acquire()

   		try:
           		f = urllib2.urlopen(sub_getque, timeout=2)
           		self.line = re.compile(self.reg).findall(f.read())
           		

        	except Exception, e:
           		pass

    		if self.line==None:

    			i+=1
			continue

		con.release()

    		for n in range(len(self.line)):

			con.acquire()
    			content = self.line[n][0]
			keyword = self.line[n][1]

    			for l in range(len(list)):

    				strinfo = re.compile(list[l])
   				content = strinfo.sub(' ',content)
    				cchar = content.split(' ')
    				url = 'http://wooyun.org/bugs/wooyun-'+cchar[0]

    			print "\nKEY: %s, ID: %s, URL: %s, TITLE: %s"%(keyword,cchar[0],url,cchar[1])
			self.found_count += 1
			con.release()
	


class distool(threading.Thread):

	def __init__(self):

		threading.Thread.__init__(self)

	def	run(self):

		global queue

		while True:

			if queue.qsize() < 2:
				break

			for pp in range(9):
				strs = '>'
				strs=strs*pp
				sys.stdout.write(strs)
				sys.stdout.flush()
				time.sleep(1)

def worker_pool(queue, size):

	workers = []
	dtool = distool()
	dtool.start()
	workers.append(dtool)

	for i in range(size):

		worker = checkweb(queue)
		worker.start()
		workers.append(worker)

	return workers

def uurl(url, snum, enum):

	ulist = []

	for i in range(snum,enum):	

        	para = i
		uu = url+str(para)
		if uu: queue.put(uu)
		ulist.append(uu)


def main(url, threads, snum, enum):

	global queue, regex
	print "\n\tThreads: %d,URL: %s, startNUM: %d, endNUM: %d, regular: %s\n"%(threads, url, snum, enum, regex)
	uurl(url, snum, enum)
	worker_threads = worker_pool(queue, threads)
	start_time = time.time()

	

	for worker in worker_threads:

		queue.put('quit')
	
	for worker in worker_threads:

		worker.join()

	print "\ncomplete! "+format(time.time() - start_time)

	return "end"


if __name__ == '__main__':

	parser = optparse.OptionParser('usage: %prog [options] \n')
	parser.add_option('-t', '--threads', dest='threads_num', 
		default=10, type='int', help='Number of threads. default = 10')
	parser.add_option('-r', '--regex', dest='regex', 
		default='乐视|头条|中科院', type='string', 
		help='the regex to find default = leshi|toutiao|zhongke in chinese')
	parser.add_option('-u', '--url', dest='url', 
		default='http://www.wooyun.org/bugs/page/', type='string', 
		help='dest url used to spider. default = http://www.wooyun.org/bugs/page/')
	parser.add_option('-s', '--para_start', dest='spara', 
		default=100, type='int', help='start num of url. default = 100')
	parser.add_option('-e', '--para_end', dest='epara',
		default=200, type='int', help='end num of url. default = 200')

	(options, args)  = parser.parse_args()

	if len(sys.argv) < 3:

		parser.print_help()
		print "  -r REGEX, --regex=REGEX  the regex to find default = 乐视|头条|中科院"
        	sys.exit(0)

	r = '.*?(\|.*?)*'
	rreg = options.regex

	if re.search(r, rreg) == None:

		print "\ninput error\n "
		print "\nregex PS: 乐视|头条|中科院\n"
		sys.exit(0)

	print "\nstart!\n"
	i = 0
	list = ['"\>','\<\/a\>']
	con = threading.Condition()
	queue = Queue()
	regex = options.regex
	threads = options.threads_num
	start = main(url=options.url, threads=options.threads_num, snum=options.spara,enum=options.epara)
