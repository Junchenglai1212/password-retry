# 密碼重試程式
# password = 'a123456'
# 讓使用者重複輸入密碼 #while
# 最多輸入3次
# 如果正確#if 就印出 "登入成功！"
# 如果不正確 就印出 "密碼錯誤！ 還有＿次機會！"

password = 'a123456'
i = 3
while True:
    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('登入成功！')
        break #逃出迴圈
    else:
    	i = i - 1
    	print('密碼錯誤！ 還有',i,'機會！')
    	if i == 0:
    	    break