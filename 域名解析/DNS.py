# coding: utf-8

# import socket
# import csv
# import requests
# import threading
# import queue

# q = queue.Queue()
# threading_num = 50
#
#
# with open("AndroidLink.txt", "r") as f:
#     filedata = f.readlines()
#     q.put(filedata)
#     f.close()
#
# def run():
#     while not q.empty():
#         filedata = q.get()
#         for i in filedata:
#             url = str(i).replace("\n",'')
#             print(url)
#             try:
#                 myaddr = socket.getaddrinfo(url, 'http')
#                 #print(str(myaddr[0][4][0])[:3])
#                 if str(myaddr[0][4][0])[:3] != str(172):
#                     #print(url+" "+str(myaddr[0][4][0]))
#                     #value_array.append(url).append(str(myaddr[0][4][0]))
#                     with open("public_domain.csv","a") as fw:
#                         writer = csv.writer(fw)
#                         writer.writerow([url, str(myaddr[0][4][0])])
#             except:
#                 #print('can't open')
#                 pass
#         #f.close()
#
# if __name__ =="__main__":
#     print('begin')
#     for i in range(threading_num):
#         t = threading.Thread(target=run)
#         t.start()
#         t.join()
#     print('over')
import socket
from urllib.parse import urlparse
with open("AndroidLink.txt","r") as f:
    for line in f.readlines():
        url = line.strip('\n')

        try:
            hostname = urlparse(url).netloc
            ip = socket.gethostbyname(hostname)
            print(ip)
            pass
        except Exception as e:
            with open('error.txt', 'a+') as ERR:  # error.txt为没有IP绑定的域名
                ERR.write(line.strip() + '\n')

        else:
            with open('result.txt', 'a+') as r:  # result.txt里面存储的是批量解析后的结果
                r.write(hostname + "\n")  # 显示有ip绑定的域名，用空格隔开
                r.write(ip+"\n")
                r.write('\n')


