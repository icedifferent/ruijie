"""
 * @Author: JianZeng Lu 
 * @Date: 2019-04-12 22:22:46 
 * @Last Modified by:   JianZeng Lu 
 * @Last Modified time: 2019-04-12 22:22:46 
"""
import requests
import json
import re
import time
import socket
import yaml
import os
# def login(userName,userPwd):
#     while(True):
#         url="http://1.1.1.1"
#         # url="http://www.baidu.com"
#         response=""
#         try:
#             response=requests.get(url,timeout=60)
#         except:
#             print(" Wifi adaptor is not working or wifi is not working")
#             time.sleep(30*5)#here should to fix the adaptor or fix the wifi
#             continue
#         #Wifi adaptor correct
#         reUrl=re.findall(".*href='(.*)'.*",str(response.content))#get the redirection url
#         if(len(reUrl)==0):#already logined
#             # print("net may be working")
#             time.sleep(30)#check every 30 mins
#             continue#don't need to login or network  is error(can not redirect)
#         print("trying to login"+reUrl[0])
#         try:
#             subUrl=reUrl[0].split("index.jsp?")#get the param
#             mainUrl=reUrl[0].split("/eporta")
#             loginUrl=mainUrl[0]+"/eportal/userV2.do?method=login&param=true&fromHtml=true&version=52472d65506f7274616c20454e54455250524953455f312e3433287033295f4275696c643230313430343235&userAgentForLogin=0&"+subUrl[1]+"&pageUuid=msg_bch_pc"
#             pyload={"usernameHidden":userName,"username":userName,"authorMode":"","pwd":userPwd,"phone":"","authorizationCode":"","regist_validcode":"","phonenum":"","regist_validcode_sm":"","authorCode":"",}
#             response=requests.post(loginUrl,pyload)
#         except Exception as e:
#             print(e)
#             time.sleep(30)
#         print(response.headers)
#         time.sleep(30)#check every 30 mins


def login(userName,userPwd):
    while(True):
        url="http://1.1.1.1"
        response=""
        try:
            response=requests.get(url,timeout=60)
        except:
            print(" Wifi adaptor is not working or wifi is not working")
            time.sleep(30*5)#here should to fix the adaptor or fix the wifi
            continue
        #Wifi adaptor correct
        reUrl=re.findall(".*href='(.*)'.*",str(response.content))#get the redirection url
        if(len(reUrl)==0):#already logined
            # print("net may be working")
            time.sleep(30)#check every 30 mins
            continue#don't need to login or network  is error(can not redirect)
        print("trying to login"+reUrl[0])
        try:
            subUrl=reUrl[0].split("index.jsp?")#get the param
            mainUrl=reUrl[0].split("/eporta")
            loginUrl=mainUrl[0]+"/eportal/InterFace.do?method=login"
#             userId: 30002563
# password: 30002563
# service: 
# queryString: wlanuserip%3D0ec1745712c5900e4a99df459fd79ebd%26wlanacname%3D7069b28464ca0182df540859d63300ed%26ssid%3Db3851c63ebfed3df%26nasip%3D2f4f7a25969fab2e91ac7c0b0c2c2d1a%26mac%3Db23cc70ebe2ff22a9edce2d8d7953328%26t%3Dwireless-v2%26url%3D01f3e58a0306370bc8e9aaa76bb4c470
# operatorPwd: 
# operatorUserId: 
# validcode: 
# passwordEncrypt: false
            #print(subUrl)
            pyload={"userId":userName,"service":"","password":userPwd,"operatorPwd":"","operatorUserId":"","validcode":"","passwordEncrypt":"false","queryString":subUrl[1]}
            
            response=requests.post(loginUrl,pyload)
        except Exception as e:
            print(e)
            time.sleep(30)
        print(response.headers)
        time.sleep(30)#check every 30 mins
if __name__ == "__main__":
    f = open('config.yaml', encoding='utf-8')
    res = yaml.load(f, Loader=yaml.BaseLoader)
    user=res['user']
    login(user['userName'],user['userPwd'])