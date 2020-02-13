#oop 1

class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    def watch_movie(self, movie_name):
        if self.age < 18:
            print('%s只能观看《灰太狼》' %  self.name)
        else:
            print('%s正在观看%s' % (self.name, movie_name))

def main():
    test = Student('Lisa', 22)
    test.study('python')
    test.watch_movie('love letter')

if __name__ == '__main__':
    main()
