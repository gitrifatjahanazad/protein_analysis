import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import json
import ast

import redis
redis = redis.StrictRedis(host='localhost', port=6379,db=0)
#sudo apt-get install python-tk
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for entry in range(1,100):
    molecule = redis.get("1out"+str(entry))
    print molecule
    molecule = ast.literal_eval(molecule)
    ax.scatter(float(molecule["x"]),float(molecule["y"]),float(molecule["z"]))

plt.show()