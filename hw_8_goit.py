from datetime import datetime, date, timedelta
import calendar
users = [
	{
		'name': 'Bill', 'birthday': date(year = 2003, month = 9, day = 30)
	},
	{
		'name': 'Maria', 'birthday': date(year = 1997, month = 10, day =  1)
	},
	{
		'name': 'Jesus', 'birthday': date(year = 1995, month = 8, day =  21)
	},
	{
		'name': 'Jack', 'birthday': date(year = 1985, month = 8, day =  22)
	}
]
Monday = []
Tuesday = []
Wednesday = []
Thursday = []
Friday = []
today_date = date.today()
delta1 = timedelta(days = 5)
delta2 = timedelta(days = 2)
today_year = today_date.year

def get_birthdays_per_week(users):
	for i in users:
		if 'birthday' in i:
			new_date = i['birthday'].replace(year = today_year)
			if new_date <= (today_date + delta1) and new_date >= (today_date - delta2):
				if date.weekday(new_date) == 0 or date.weekday(new_date) == 5 or date.weekday(new_date) == 6:
					Monday.append(i['name'])
				elif date.weekday(new_date) == 1:
					Tuesday.append(i['name'])
				elif date.weekday(new_date) == 2:
					Wednesday.append(i['name'])
				elif date.weekday(new_date) == 3:
					Thursday.append(i['name'])
				elif date.weekday(new_date) == 4:
					Friday.append(i['name'])
	if date.weekday(today_date) == 0 or date.weekday(today_date) == 5 or date.weekday(today_date) == 6:
		if len(Monday):
			print('Monday:', Monday)
		if len(Tuesday):
			print('Tuesday:', Tuesday)
		if len(Wednesday):
			print('Wednesday:', Wednesday)
		if len(Thursday):	
			print('Thursday:', Thursday)
		if len(Friday):	
			print('Friday:', Friday)
	elif date.weekday(today_date) == 1:	
		if len(Tuesday):
			print('Tuesday:', Tuesday)
		if len(Wednesday):	
			print('Wednesday:', Wednesday)
		if len(Thursday):	
			print('Thursday:', Thursday)
		if len(Friday):	
			print('Friday:', Friday)
		if len(Monday):	
			print('Monday:', Monday)
	elif date.weekday(today_date) == 2:		
		if len(Wednesday):	
			print('Wednesday:', Wednesday)
		if len(Thursday):	
			print('Thursday:', Thursday)
		if len(Friday):	
			print('Friday:', Friday)
		if len(Monday):	
			print('Monday:', Monday)
		if len(Tuesday):	
			print('Tuesday:', Tuesday)
	elif date.weekday(today_date) == 3:		
		if len(Thursday):	
			print('Thursday:', Thursday)
		if len(Friday):	
			print('Friday:', Friday)
		if len(Monday):	
			print('Monday:', Monday)
		if len(Tuesday):	
			print('Tuesday:', Tuesday)
		if len(Wednesday):	
			print('Wednesday:', Wednesday)
	elif date.weekday(today_date) == 4:		
		if len(Friday):	
			print('Friday:', Friday)
		if len(Monday):	
			print('Monday:', Monday)
		if len(Tuesday):	
			print('Tuesday:', Tuesday)
		if len(Wednesday):	
			print('Wednesday:', Wednesday)
		if len(Thursday):	
			print('Thursday:', Thursday)

get_birthdays_per_week(users)