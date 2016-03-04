import math

t_tea = float(input("Temperature of the Tea: "))
t_air = float(input("Temperature of the Air: "))
t_min = float(input("Number of Minutes: "))

print("Minute     Temperature")
print("    0       ", t_tea)
time = 1
while time < t_min:
    t_tea = t_tea - .055* (t_tea-t_air)
    print("   ", time ,"      ", "%.1f" % t_tea)
    time = time + 1
