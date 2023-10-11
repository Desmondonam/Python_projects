'''
This is a code that is meant to calculate the age of some. They give the year of birth
and the output will be the age they have in years
'''

def ageCalculator(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    print(age)
ageCalculator(1999, 9, 3)