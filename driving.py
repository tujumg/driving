
country = input('請輸入國家')
age = input('請輸入年齡')
age = int(age)
if country == 'taiwan':
	if age < 18:
		print('還不能考')
	else:
		print('可以考')