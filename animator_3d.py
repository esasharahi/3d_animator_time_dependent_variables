# esasharahi@gmail.com

import pandas as pd
import matplotlib.animation as animation
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
culs_names = list(df.columns)

t = df[culs_names[0]]
x = df[culs_names[1]]
y = df[culs_names[2]]
z = df[culs_names[3]]

fig = plt.figure()
ax = plt.axes(projection='3d')


def update_plot(i):
    ax.cla()
    ax.plot(x[:i], y[:i], z[:i])
    #ax.scatter3D(x[:i], y[:i], z[:i])
    #ax.scatter3D(x[:i], y[:i], z[:i], c=x[:i] + y[:i] + z[:i])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title(f'time: {t[i]}')

ani = animation.FuncAnimation(fig, update_plot, frames=len(t), interval=150)
plt.show()
