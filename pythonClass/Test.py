
name = "I'm jacky"
result = name.find('Im')
print(result)

# 列表推导式
n_list = [x ** 2 for x in range(10) if x%2 == 0]
print(n_list)

# 错误处理
import datetime as dt

def read_date_from_file(filename):
    try:
        with open(filename) as file:
            in_date = file.read()

        in_date = in_date.strip()
        date = dt.datetime.strptime(in_date,'%Y-%m-%d')
        return date
    except ValueError as e:
        print('处理ValueError异常')
    except OSError as e:
        print('处理OSError异常')

date = read_date_from_file('readme.txt')
print('日期 = {0}'.format(date))

# 显示抛出异常 raise

class MyException(Exception):
    def __init__(self,message):
        super().__init__(message)

def read_date_from_file1(filename):
    try:
        file = open(filename)
        in_date = file.read()
        in_date = in_date.strip()
        date = dt.datetime.strptime(in_date,'%Y-%m-%d')
        return  date
    except ValueError as e:
        raise MyException('不是有效日期')
    except FileNotFoundError as e:
        raise MyException('文件找不到')
    except OSError as e:
        raise MyException('文件无法打开或找不到')

date1 = read_date_from_file1("readme.txt")
print('日期{0}'.format(date))
