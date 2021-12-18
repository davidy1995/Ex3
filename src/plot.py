import random
import numpy as np
from matplotlib import pyplot as plt

from GraphAlgoInterface import GraphAlgoInterface
import src.GraphAlgo

# self.load_from_json("A0.json")
plt.title('Our graph')

x_values = [13,44,92]
y_values = [82,50,55]
size = len(x_values)
plt.scatter(x_values, y_values, color='green') # green node dot

for i in range(size):
    plt.text(x_values[i],y_values[i], "node id ", ha='center', fontsize=8)
    i =+1

# z_values = []
# plt.text(13,82,"node id", ha='center',fontsize=8)

# for i in range(1):
#     x_values.append(random.randint(0, 100))
#     y_values.append(random.randint(0, 100))
plt.xlim(0, 100) #limit X
plt.ylim(0, 100) # limit Y
plt.scatter(x_values, y_values, color='green') # green node dot
plt.plot(x_values,y_values) # making lines

plt.show()