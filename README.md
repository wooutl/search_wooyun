# search_wooyun

---
由于近期乌云不让我的好朋友小白搜索漏洞了，我拿出个小脚本给他

###支撑中文正则
    提前设置编码utf8
    多个关键字以"|"分隔，如 "乐视|头条|中科院"

###默认参数：
    线程 10
    URL: http://www.wooyun.org/bugs/page/
    起始页: 100
    结束页: 200
    正则: 乐视|头条|中科院

###Usage: search_wooyun.py [options] 

    Options:

        -h, --help            show this help message and exit
  
        -t THREADS_NUM, --threads=THREADS_NUM
        Number of threads. default = 10
                        
        -r REGEX, --regex=REGEX
        the regex to find default = leshi|toutiao|zhongke in chinese
                        
        -u URL, --url=URL     
        dest url used to spider. default = http://www.wooyun.org/bugs/page/
  
        -s SPARA, --para_start=SPARA
        start num of url. default = 100
                        
        -e EPARA, --para_end=EPARA
        end num of url. default = 200
                        
        -r REGEX, --regex=REGEX  
        the regex to find default = 乐视|头条|中科院
  
  


###最少指定一个参数
    [root@centos63 ~]# python search_wooyun.py -t 30 -s 100 -e 300 -r "yershop"

    start!


        Threads: 30,URL: http://www.wooyun.org/bugs/page/, startNUM: 100, endNUM: 300, regular: yershop

        KEY: yershop, ID: 2015-0134558, URL: http://wooyun.org/bugs/wooyun-2015-0134558, TITLE: yershop逻辑错误（可0元购物）
        KEY: yershop, ID: 2015-0133005, URL: http://wooyun.org/bugs/wooyun-2015-0133005, TITLE: yershop商城系统最新版一处xff注入(demo演示)
        KEY: yershop, ID: 2015-0132734, URL: http://wooyun.org/bugs/wooyun-2015-0132734, TITLE: yershop商城系统30处sql注入

    [root@centos63 ~]# python search_wooyun.py -t 1

    start!

        Threads: 1,URL: http://www.wooyun.org/bugs/page/, startNUM: 100, endNUM: 200, regular: 乐视|头条|中科院

        KEY: 乐视, ID: 2015-0136003, URL: http://wooyun.org/bugs/wooyun-2015-0136003, TITLE: 乐视某站设计缺陷到SQL注入（涉及22个库DBA权限）

        KEY: 乐视, ID: 2015-0135249, URL: http://wooyun.org/bugs/wooyun-2015-0135249, TITLE: 乐视某开发平台管理弱口令

        KEY: 头条, ID: 2015-0134995, URL: http://wooyun.org/bugs/wooyun-2015-0134995, TITLE: 汽车头条sql注射漏洞

        KEY: 乐视, ID: 2015-0134979, URL: http://wooyun.org/bugs/wooyun-2015-0134979, TITLE: 乐视某站SQL注入（修复不当）

        KEY: 中科院, ID: 2015-0133981, URL: http://wooyun.org/bugs/wooyun-2015-0133981, TITLE: 中科院某研究所系统存在弱口令

        KEY: 乐视, ID: 2015-0133394, URL: http://wooyun.org/bugs/wooyun-2015-0133394, TITLE: 视频网站安全之乐视视频APP高危SQL注入漏洞(管理员账户密码\百万级用户数据)

        KEY: 中科院, ID: 2015-0132763, URL: http://wooyun.org/bugs/wooyun-2015-0132763, TITLE: 某通用图书馆管理SQL注入(涉及各地党校/中科院)

