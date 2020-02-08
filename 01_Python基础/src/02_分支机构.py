username = input('请输入您的用户名:')

if username == 'admin':
    password = input('请输入密码:')
    if password == '123456':
        print('身份验证成功')
    else:
        print('您的密码错误，请重新输入')
else:
    print('无此身份')
