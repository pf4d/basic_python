import re
import datetime          as dt
import calendar          as cal
import matplotlib.dates  as dates
from pylab import *


data  = open("groceries_in.txt")
p     = re.compile('([0-9]+.[0-9]+.[0-9]+)-([0-9]+.[0-9]+).*?\n')
date  = []
spent = []

# fill the arrays values from the .txt file :
for l in data.readlines():
  m = p.match(l)
  if m != None:
    dateSplit = m.group(1).rsplit('.')
    d = dt.datetime(int(dateSplit[2]), 
                    int(dateSplit[0]), 
                    int(dateSplit[1]))
    date.append(d)
    spent.append(float(m.group(2)))
data.close()
date.sort()

# total time in days :
start   = date[0] - dt.timedelta(1)
end     = date[-1]
totTime = end - start

# total costs :
costPerDay = sum(spent) / totTime.days
total      = sum(spent)


# create an array of monthly expendatures :
avg = []
for i in range(len(spent)):
  avgCostToDate = sum(spent[:i]) / (date[i] - start).days
  avg.append(avgCostToDate)


# calculate monthly costs :
month_total   = []
month_tot_str = []
cont_date     = []
tot           = 0.0
month         = date[0].month
year          = date[0].year
date_n        = date[0]
for i,d in enumerate(date):
  # tallying monthly totals :
  if d.month == month and d.year == year:
    tot += spent[i]
  # calculate the monthly totals and append :
  else:
    month_tot_str.append('$' + str(round(tot, 2)))
    min_d, max_d = cal.monthrange(year, month)
    for i in range(date_n.day, max_d+2):
      month_total.append(tot)
      cont_date.append(date_n)
      date_n += dt.timedelta(1)
    tot   = spent[i]
    month = d.month
    year  = d.year

# finish off the last part of the month :
month_tot_str.append('$' + str(round(tot, 2)))
for i in range(date_n.day, d.day+1):
  month_total.append(tot)
  cont_date.append(date_n)
  date_n += dt.timedelta(1)

# update output file with statistics :
data = open("groceries_out.txt", "w")
data.write('Grocery / Dog Expenses:\n\n\n')
for d, s in zip(date, spent):
  data.write(d.strftime("%m.%d.%y") + ' - ' + str(s) + '\n')
data.write('\n\nTotal: $%.2f' % total)
data.write('\n\nAverage cost per day: $%.2f' % costPerDay)
data.close()

# plotting :
totTime = date[-1] - date[0]
days    = totTime.days
fig     = figure(figsize=(12,5))
tit     = "Food Expendature for %s days : $%.2f" % (days, total)
ax1  = fig.add_axes([.1,.2,.8,.7], title = tit) # [left, bottom, width, height]
ax2  = ax1.twinx()
ax1.grid()
ax1.plot(date,      spent,       'ro', lw=1, label='expendatures')
ax1.plot(date,      avg,         'b-', lw=2, label='average cost per day')
ax2.plot(cont_date, month_total, 'g-', lw=2, label='monthly total', 
         drawstyle='steps')
leg = ax1.legend(loc='upper left')
leg.get_frame().set_alpha(0.5)
ax1.set_ylabel('Cost ($)')
ax2.set_ylabel('Total Monthly Cost ($)', color='g')
ax1.set_xlabel("Average Cost Per Day : $%.2f" % costPerDay)
for tl in ax2.get_yticklabels():
  tl.set_color('g')
plt.show()



