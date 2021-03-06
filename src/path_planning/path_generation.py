import numpy as np
import tf.transformations
import copy


def lemniscate_of_bernoulli(t, bounding_box):
    """Generates a shape similiar to the number "8".

    See https://de.wikipedia.org/wiki/Lemniskate_von_Bernoulli for details of
    the algorithm.

    Args:
        t (float): Line parameter in range [0; 2*Pi]
        bounding_box (tuple, list): Scale the path so it fits inside the
            bounding box.

    Returns:
        (x, y)
    """
    ax = bounding_box[0] / np.sqrt(2) * 0.5
    ay = bounding_box[1]
    a = np.min([ax, ay])
    x = (a * np.sqrt(2) * np.cos(t)) / (np.sin(t)**2 + 1.0)
    y = (a * np.sqrt(2) * np.cos(t) * np.sin(t)) / (np.sin(t)**2 + 1.0)
    return x, y


def lemniscate_of_gerono(t, bounding_box):
    """Creates an "8" shaped curve.

    See https://mathworld.wolfram.com/EightCurve.html for details.

    Args:
        t (float, vector): Line parameter in range [0; 2pi]
        bounding_box (tuple, list): The path is scaled so it fits inside the
            bounding box.

    Returns:
        (x, y)
    """
    ax = bounding_box[0] * 0.5
    ay = bounding_box[1]
    a = np.min([ax, ay])

    x = a * np.sin(t)
    y = a * np.sin(t) * np.cos(t)
    return x, y


def super_ellipse(t, a=1.0, b=3.0, n=4.0):
    # https://en.wikipedia.org/wiki/Superellipse
    # 0 <= t < 2*pi
    x = np.abs(np.cos(t))**(2.0 / n) * a * np.sign(np.cos(t))
    y = np.abs(np.sin(t))**(2.0 / n) * b * np.sign(np.sin(t))
    return x, y


def circle(t, r=1.0):
    x = r * np.cos(t)
    y = r * np.sin(t)
    return x, y


def get_yaw_angle(x, y):
    # numerical computation of yaw angle using a line through the current and
    # the next waypoint
    # this works for any continous curve
    yaw = [0] * len(x)
    for i in range(len(x) - 1):
        yaw[i] = np.arctan2(y[i + 1] - y[i], x[i + 1] - x[i])
    # assuming that the next waypoint of the last waypoint is the first waypoint
    yaw[-1] = np.arctan2(y[0] - y[-1], x[0] - x[-1])

    return yaw


def scale_and_move(x, y, x_offset=0.7, y_offset=2.0, factor=1.0):
    # x is the shorter side of the tank, check this:
    if np.max(np.abs(x)) > np.max(np.abs(y)):
        # swap axes
        tmp = x
        x = y
        y = tmp

    x *= factor
    y *= factor

    x += x_offset
    y += y_offset

    return x, y


def xyz_to_dict_list(x, y, z):
    path = []
    for x_, y_, z_ in zip(x, y, z):
        path.append(dict(x=float(x_), y=float(y_), z=float(z_)))
    return path


def xyz_to_gantry_yaml(x, y, z, loop=True, start_position=None):
    path = xyz_to_dict_list(x, y, z)
    if start_position is None:
        start_position = copy.deepcopy(path[0])
    else:
        start_position = dict(x=float(start_position[0]),
                              y=float(start_position[1]),
                              z=float(start_position[2]))
    data = dict(start_position=start_position, loop=bool(loop), path=path)
    return data
