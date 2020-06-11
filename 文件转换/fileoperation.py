# encoding=utf-8
import os

coding = ['收到数据','#OP code Error','run','executer','prn_threshold','offset','max_object_size','OTA','index','写数据','#cmd']

fileName = "Ios_cz.txt" #input("输入文件路径：")
isExist = os.path.exists(fileName)

with open(fileName, "r") as f:
    lines = f.readlines()
    outPutstring = ""
    for line in lines:
        # print(line)
        for cod in coding:
            if line.startswith(cod):
                outPutstring += (line + "\n")

    # print(outPutstring)
    with open("OutPut", "a") as a:
        a.write(outPutstring)
        a.close()