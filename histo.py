import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0.0,10.0,200) #200 random floats between 0 and 10
plt.hist(x,10) # a histogram with 10 bars
plt.show()
