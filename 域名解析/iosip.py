# with open("android_ip.txt","r") as f:
#     for line in f.readlines():
#         ipList = line.split('.')
#         if len(ipList) == 4:
#             try :
#                 int(ipList[0])
#                 with open('result.txt', 'a+') as r:  # result.txt里面存储的是批量解析后的结果
#                     r.write(line + "\n")  # 显示有ip绑定的域名，用空格隔开
#             except:
#                 pass

# file_list = []  #创建一个空列表
#
# with open("result.txt","r") as f:
#     file_2 = f.readlines()
#     for file in file_2:
#         file_list.append(file)
#     out_file1 = set(file_list)    #set()函数可以自动过滤掉重复元素
#     last_out_file = list(out_file1)
#     for out in last_out_file:
#         ipList = out.split('.')
#
#         with open('android_ip.txt', 'a+') as r:  # result.txt里面存储的是批量解析后的结果
#             r.write(out)  # 显示有ip绑定的域名，用空格隔开

#
# file = "testip1.txt"    #打开需要去重的文件
# with open(file, "r", encoding="utf-8") as f:
#     file_2 = f.readlines()
#     for file in file_2:
#         file_list.append(file)
#     out_file1 = set(file_list)    #set()函数可以自动过滤掉重复元素
#     last_out_file = list(out_file1)
#     for out in last_out_file:
#         ipList = out.split('.')
#         if len(ipList) == 4:
#             with open('result.txt', 'a+') as r:  # result.txt里面存储的是批量解析后的结果
#                 r.write(out)  # 显示有ip绑定的域名，用空格隔开
# from _dbm import open

with open("/Users/app005synergy/Documents/Python/域名解析/result.txt","r") as f:
    # words = ""
    file = f.readlines()
    for line in file:
        line = line.replace("\n","") + ","
        with open("/Users/app005synergy/Documents/Python/域名解析/testip1.txt", "a+") as r:
            r.write(line)
        print(line)
    print(file)

    #


