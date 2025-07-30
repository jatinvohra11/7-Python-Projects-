from datetime import datetime

dob = input("Enter your DOB (YYYY-MM-DD): ")
dob_date = datetime.strptime(dob, "%Y-%m-%d")
today = datetime.today()
age = today.year - dob_date.year - ((today.month, today.day)<(dob_date.month, dob_date.day))
print("You are", age, "years old..")