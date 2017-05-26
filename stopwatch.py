import sys
import time

t0 = time.time()       # initial time
fg = '\033[38;5;1m'   # for colors

try:
  while True:
    tn = time.time()   # current time
    s  = tn - t0       # seconds
    m  = s/60.         # minutes
    h  = m/60.         # hours
    
    s  = s % 60        # reset seconds
    m  = m % 60        # reset minutes
     
    sys.stdout.write(fg + "\r%02d:%02d:%02d \033[0m" % (h,m,s))
    sys.stdout.flush()
    
    time.sleep(1)      # sleep for 1 second.

except KeyboardInterrupt:
  print "\ndone - total time: %0.2f hours" % ((tn - t0) / 60 / 60)
