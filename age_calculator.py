
from datetime import date


def get_dob():
    # write code here
	year = input("Enter year of birth")
	month = input("Enter month of birth")
	day = input("Enter day of birth")
	return date(int(year), int(month), int(day))


def get_age(dob):
    # write code here
	today = date.today()
	age =int((today - dob).days / 356)
	return age


def main():
	# write code here
	dob = get_dob()
	print(dob)
	if dob == None:
		return
	else:
		age = get_age(dob)
		if age < 0:
			print("You should choose a valid date of birth")
			return
		else:
			print(f"Your age is {age}")
			return


if __name__ == '__main__':
    main()
