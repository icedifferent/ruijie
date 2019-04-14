#ruijie
锐捷校园wifi登录脚本
功能：网络账号掉线自动重连，账号在配置文件config.yaml里面修改
本脚本仅在scau校园网测试通过。
环境依赖缺啥装啥
python3 ./ruijie.py

{'Content-Length': '497', 'Pragma': 'no-cache', 'X-Powered-By': 'Servlet 2.4; JBoss-4.0.5.GA (build: CVSTag=Branch_4_0 date=200610162339)/Tomcat-5.5', 'Auth-Result': 'success', 'Expires': 'Wed, 31 Dec 1969 23:59:59 GMT', 'Cache-Control': 'max-age=0', 'Date': 'Sun, 14 Apr 2019 02:13:11 GMT', 'Set-Cookie': 'JSESSIONID=xxx; Path=/', 'Server': 'Apache-Coyote/1.1', 'Content-Type': 'text/html;charset=UTF-8'}

返回如上述的字段（'Auth-Result': 'success'）就代表成功啦，仅供自娱自乐。

