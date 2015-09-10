# search_wooyun


由于近期乌云不让我的好朋友小白搜索漏洞了，我拿出个小脚本给他


Usage: search_wooyun.py [options] 

  Options:

  -h, --help            show this help message and exit
  
  -t THREADS_NUM, --threads=THREADS_NUM
                        Number of threads. default = 10
                        
  -r REGEX, --regex=REGEX
                        the regex to find default = leshi|toutiao|zhongke in chinese
                        
  -u URL, --url=URL     dest url used to spider. default = http://www.wooyun.org/bugs/page/
  
  -s SPARA, --para_start=SPARA
                        start num of url. default = 100
                        
  -e EPARA, --para_end=EPARA
                        end num of url. default = 200
                        
  -r REGEX, --regex=REGEX  the regex to find default = 乐视|头条|中科院
  
