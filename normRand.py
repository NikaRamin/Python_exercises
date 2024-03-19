import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(10.0,0.1,100000)
plt.hist(x,100)
plt.show()