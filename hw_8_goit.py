from datetime import datetime, date, timedelta

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
today_date = date.today()
delta1 = timedelta(days = 5)
delta2 = timedelta(days = 2)
today_year = today_date.year

def get_birthdays_per_week(users):
	bd_list = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": []
    }
	for user in users:
		if 'birthday' in user:
			new_date = user['birthday'].replace(year = today_year)
			if new_date <= (today_date + delta1) and new_date >= (today_date - delta2):
				if date.weekday(new_date) in (0, 5, 6):
					bd_list.get('Monday').append(user.get('name'))
				elif date.weekday(new_date) == 1:
					bd_list.get('Tuesday').append(user.get('name'))
				elif date.weekday(new_date) == 2:
					bd_list.get('Wednesday').append(user.get('name'))
				elif date.weekday(new_date) == 3:
					bd_list.get('Thursday').append(user.get('name'))
				elif date.weekday(new_date) == 4:
					bd_list.get('Friday').append(user.get('name'))
	print_users_list(bd_list)

def print_users_list(users_list: dict):
    for key, value in users_list.items():
        if value:
            print(f"{key}: {', '.join(value)}")

get_birthdays_per_week(users)	