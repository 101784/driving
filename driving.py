country=input('請輸入國家: ')
age=int(input('請輸入年齡: '))
if country == '台灣':
	if age >=18:
		print('你可以開車,但需要考駕照')
	else:
		print('你還不能開車,等18才能')
elif country == '美國':
	if age >=16:
		print('你可以開車,但需要考駕照')
	else:
		print('你還不能開車,等18才能')
else :
	print('你只能輸入台灣/美國歐')