import numpy as np
import matplotlib.pyplot as plt 

x = np.random.uniform(0.0,10.0,20)
y = np.random.uniform(0.0,10.0,20)

plt.scatter(x,y)
plt.show()

x2 = np.random.normal(5.0, 1.0, 1000)
y2 = np.random.normal(10.0, 2.0, 1000)


plt.scatter(x2,y2)
plt.show()
