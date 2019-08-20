# 練習先建立Github專案，在開始寫code
# 請使用者輸入年齡、國家。並判斷他能不能開車！
age = input('請輸入年齡： ')
country = input('請輸入國家： ')
age = float(age)
if country == '台灣':
	if age >= 18:
		print('你有考駕照的資格')
	else:
		print('你尚未具有考駕照的資格')
