import matplotlib.pyplot as plt
import numpy as np
import yaml

x_width = 0.8
y_width = 2.0
x_offset = 1.0
y_offset = 2.0

left_y = np.linspace(y_offset - y_width / 2, y_offset + y_width / 2, num=100)
left_x = np.linspace(x_offset - x_width / 2, x_offset - x_width / 2, num=100)
left_z = np.linspace(-0.3, -0.3, num=100)

right_y = np.linspace(y_offset + y_width / 2, y_offset - y_width / 2, num=100)
right_x = np.linspace(x_offset + x_width / 2, x_offset + x_width / 2, num=100)
right_z = left_z

top_y = np.linspace(y_offset + y_width / 2, y_offset + y_width / 2, num=100)
top_x = np.linspace(x_offset - x_width / 2, x_offset + x_width / 2, num=100)
top_z = np.linspace(-0.3, -0.3, num=100)

bot_y = np.linspace(y_offset - y_width / 2, y_offset - y_width / 2, num=100)
bot_x = np.linspace(x_offset + x_width / 2, x_offset - x_width / 2, num=100)
bot_z = np.linspace(-0.3, -0.3, num=100)

data = {}
waypoints = []
for i in range(100):
    waypoints.append(
        {'x': float(top_x[i]), 'y': float(top_y[i]), 'z': float(top_z[i])}
    )
for i in range(100):
    waypoints.append(
        {'x': float(right_x[i]), 'y': float(right_y[i]), 'z': float(right_z[i])}
    )
for i in range(100):
    waypoints.append(
        {'x': float(bot_x[i]), 'y': float(bot_y[i]), 'z': float(bot_z[i])}
    )
for i in range(100):
    waypoints.append(
        {'x': float(left_x[i]), 'y': float(left_y[i]), 'z': float(left_z[i])}
    )

data['waypoints'] = waypoints
data['loop'] = True

with open('rectangle.yaml', 'w') as file:
    yaml.dump(data, file)
x = [waypoint['x'] for waypoint in waypoints]
y = [waypoint['y'] for waypoint in waypoints]
z = [waypoint['z'] for waypoint in waypoints]
plt.plot(x, y)
plt.show()
