# 读写文本文件

def main():
    try:
        f = open('helloworld.txt', 'r', encoding = 'utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeError:
        print('读取文件编码错误')
    finally:
        if f:
            f.close()

if __name__ == '__main__':
    main()

