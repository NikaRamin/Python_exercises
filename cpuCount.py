# Write a Python program to find out the number of CPUs used.

import os
cpuCount = os.cpu_count()
print("The number of CPUs used:",cpuCount)
