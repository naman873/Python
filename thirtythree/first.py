import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

x,_=make_blobs(centers=3,random_state=42)
plt.scatter(x[:,0],x[:,1])

