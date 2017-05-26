from pylab import *

p_s_01 =  1782.00
p_s_02 =  1673.06
p_s_03 =  2242.00
p_s_04 =  5422.00
p_s_05 =  4326.00
p_s_06 =  5500.00
p_s_07 =  9391.00
p_s_08 =   234.00
p_s_09 = 15742.77
p_s_10 =  2643.09
p_s_11 = 16291.73
p_s_12 =  7870.90

p_f_02 =  3743.92
p_f_03 =  2218.43
p_f_04 =  3803.05
p_f_05 =  4956.72
p_f_06 =  1267.70
p_f_07 =  1669.42

r_s_01 = 0.06
r_s_02 = 0.068
r_s_03 = 0.06
r_s_04 = 0.045
r_s_05 = 0.068
r_s_06 = 0.056
r_s_07 = 0.068
r_s_08 = 0.034
r_s_09 = 0.068
r_s_10 = 0.068
r_s_11 = 0.0621
r_s_12 = 0.0584

r_f_02 = 0.068
r_f_03 = 0.068
r_f_04 = 0.068
r_f_05 = 0.068
r_f_06 = 0.068
r_f_07 = 0.068

p_v = [p_s_01,
       p_s_02,
       p_s_03,
       p_s_04,
       p_s_05,
       p_s_06,
       p_s_07,
       p_s_08,
       p_s_09,
       p_s_10,
       p_s_11,
       p_s_12,
       p_f_02,
       p_f_03,
       p_f_04,
       p_f_05,
       p_f_06,
       p_f_07]

r_v = [r_s_01,
       r_s_02,
       r_s_03,
       r_s_04,
       r_s_05,
       r_s_06,
       r_s_07,
       r_s_08,
       r_s_09,
       r_s_10,
       r_s_11,
       r_s_12,
       r_f_02,
       r_f_03,
       r_f_04,
       r_f_05,
       r_f_06,
       r_f_07]

def f(p,r,t):
  return p*exp(r*t)

F = 0.0
t = linspace(0,20,1000)

for p,r in zip(p_v, r_v):
  F += f(p,r,t)


fig = figure()
ax  = fig.add_subplot(111)

ax.plot(t, F, 'k-', lw=2.0)
grid()
ax.set_xlabel('years')
ax.set_ylabel('dollars owed')
show()




