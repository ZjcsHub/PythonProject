# coding=utf8
class Persion:
    name = []


p1 = Persion()
p2 = Persion()
p1.name.append("小美")
print(p1.name)
print(p2.name)
print(Persion.name)

# 单例模式

class Singleton(object):
    """
    单例模式
    """
    class _A(object):
        """
        真正干活类，对外隐藏
        """
        def __init__(self):
            pass
        def display(self):
            """返回当前实例的 ID，是全局唯一的"""
            return id(self)

    # 类变量，用于存储 _A的实例

    _instance = None

    def __init__(self):
        if Singleton._instance is None:
            Singleton._instance = Singleton._A()

    def __getattr__(self, item):
        """所有的属性都应该从 Singleton._instance 获取"""
        return getattr(self._instance,item)

if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    print(id(s1),s1.display())
    print(id(s2),s2.display())
