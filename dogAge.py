from datetime import *


birth  = datetime(2010, 11, 24)  # birthdate Nov. 24th, 2010
today  = datetime.today()        # current date

time   = today - birth
age    = time.days/365           # current age
dogAge = 7*time
dogAge = dogAge.days/365         # current dog age

sstime = timedelta(365*16/7)     # time to turn 16
ssdate = birth + sstime          # date of 16th birthday (in dog years)

print "Gabby is %i years old" % dogAge


