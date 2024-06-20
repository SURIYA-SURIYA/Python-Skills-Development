import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6])
y = np.array([10,20,30,40,50,60])
plt.scatter(x,y)
plt.xlabel("numbers")
plt.ylabel("percentage")
plt.title('students details')
plt.show()