
default:	build

clean:
	rm -rf Makefile /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile

build:
	$(MAKE) -f /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/Makefile

install:
	$(MAKE) -f /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/Makefile install

modules:
	$(MAKE) -f /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/Makefile modules

upgrade:
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/sbin/nginx -t

	kill -USR2 `cat /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/logs/nginx.pid`
	sleep 1
	test -f /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/logs/nginx.pid.oldbin

	kill -QUIT `cat /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/logs/nginx.pid.oldbin`
