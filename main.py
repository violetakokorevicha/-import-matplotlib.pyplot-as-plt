import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Janvāris", "Februaris", "Marts", "Aprilis", "Maijs"])
y = np.array([10, 10, 6, 12, 8])

plt.grid(axis = 'y', color = 'gray', linewidth = 0.5)
plt.bar(x, y, width = 0.4, color = "#4CAF50", zorder = 3)
plt.show()