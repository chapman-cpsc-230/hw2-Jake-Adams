import math

t_tea = float(input("Temperature of the Tea: "))
t_air = float(input("Temperature of the Air: "))
t_min = float(input("Number of Minutes: "))

print("Minute     Temperature")
#print("    0       ", t_tea)
time = 0
while time < t_min*60:
    if time%60 == 0:
        print("   ", time/60 ,"      ", "%.1f" % t_tea)
        t_tea = t_tea - .055* (t_tea-t_air)/60
        time = time + 1
    else:
        t_tea = t_tea - .055* (t_tea-t_air)/60
        #print("   ", time ,"      ", "%.1f" % t_tea)
        time = time + 1
