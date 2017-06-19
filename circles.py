import matplotlib.pyplot as plt

circle1 = plt.Circle((0.4, 0.4), 0.001, color='r')
circle2 = plt.Circle((0.5, 0.5), 1.0, color='blue')
circle3 = plt.Circle((0.6, 0.6), 0.002, color='#CCCCFF', clip_on=False)

fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
# fig = plt.gcf()
# ax = fig.gca()


ax.add_artist(circle2)
ax.add_artist(circle1)
ax.add_artist(circle3)

fig.savefig('plotcircles.png')
