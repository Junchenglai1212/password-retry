# 密碼重試程式
# password = 'a123456'
# 讓使用者重複輸入密碼 #while
# 最多輸入3次
# 如果正確#if 就印出 "登入成功！"
# 如果不正確 就印出 "密碼錯誤！ 還有＿次機會！"

password = 'a123456'
while True:
    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('登入成功！')
        break
    else:
    	print('密碼錯誤！ 還有2次機會！')

    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('登入成功！')
        break
    else:
    	print('密碼錯誤！ 還有1次機會！')

    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('登入成功！')
        break
    else:
    	print('密碼錯誤！ 登入鎖定')
    	break