import rospy
from path_planning import path_generation as pg
import numpy as np
import sys
import argparse
import yaml


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("-a",
                        type=float,
                        help="Half of the ellipse's length in x direction.",
                        default=1.0)
    parser.add_argument("-b",
                        type=float,
                        help="Half of the ellipse's length in y direction.",
                        default=1.0)
    parser.add_argument(
        "-p",
        type=float,
        help=
        "Power of the super ellipse. Choose 1.0 for normal ellipse or > 1.0 for oval.",
        default=1.0)
    parser.add_argument("-n",
                        type=int,
                        help="Number of discrete path points.",
                        default=500)
    parser.add_argument("-xshift",
                        type=float,
                        help="Shift in x direction.",
                        default=0.0)
    parser.add_argument("-yshift",
                        type=float,
                        help="Shift in y direction.",
                        default=0.0)
    parser.add_argument("-z",
                        type=float,
                        help="Depth coordinate of the path.",
                        default=-0.8)
    parser.add_argument("-plot",
                        help="Flag to toggle plotting.",
                        action="store_true")
    args = parser.parse_args(args[1:])
    t = np.linspace(0, 2 * np.pi, args.n)
    x, y = pg.super_ellipse(t, a=args.a, b=args.b, n=args.p)
    x += args.xshift
    y += args.yshift
    z = np.zeros_like(x)
    z *= args.z
    data = pg.xyz_to_gantry_yaml(x, y, z)
    f = open("output.yaml", "w")
    yaml.dump(data, f, default_flow_style=True)
    f.close()
    print(args)
    if args.plot:
        import matplotlib.pyplot as plt
        i = np.linspace(0.0, 1.0, num=args.n)
        h = plt.scatter(x, y, marker="v", c=i)
        plt.scatter(x[0], y[0], marker="o")
        plt.gca().set_aspect("equal", adjustable="box")
        plt.colorbar(h)
        plt.show()


if __name__ == "__main__":
    main(rospy.myargv(argv=sys.argv))
