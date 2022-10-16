import matplotlib.pyplot as plt
import matplotlib.animation as anim
import math as mt
import numpy as np
import random as rd
x = np.arange(0,10,0.01)
plt.bar(x,np.e**x,color=rd.choices(["g","b","r","orange","yellow","black"],k=1001))
plt.show()