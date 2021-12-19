
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import ConnectionPatch
# self.load_from_json("A0.json")
plt.title('Our graph')
fig, (ax1) = plt.subplots(figsize=(3, 3))
x_values = [13,44,92]
y_values = [82,50,55]
id = [1,2,3]
xyA = (x_values[0],y_values[0])
xyB = (x_values[1],y_values[1])
xyC = (x_values[2],y_values[2])
size = len(x_values)
plt.scatter(x_values, y_values, color='green') # green node dot
# dsada

# id's on nodes
for i in range(size):
    plt.text(x_values[i],y_values[i], f'{id[i]}', ha='center', fontsize=8)
    i =+1


# z_values = []
# plt.text(13,82,"node id", ha='center',fontsize=8)

coordsA = "data"
coordsB = "data"

plt.xlim(0, 100) #limit X
plt.ylim(0, 100) # limit Y
plt.scatter(x_values, y_values, color='green') # green node dot
# plt.plot(x_values,y_values,) # making lines

con = ConnectionPatch(xyA,xyB,coordsA,coordsB, arrowstyle="<|-|>",shrinkA=3, shrinkB=3,) # make arrows between nodes
con1 = ConnectionPatch(xyB,xyC,coordsA,coordsB, arrowstyle="<|-|>",shrinkA=3, shrinkB=3,) # make arrows between nodes
ax1.add_artist(con)
ax1.add_artist(con1)
plt.show()