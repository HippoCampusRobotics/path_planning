import rospy
from path_planning import path_generation as pg
import numpy as np
import sys
import argparse
import yaml


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("-alg",
                        choices=["bernoulli", "gerono"],
                        help="Type of the lemniscate.",
                        default="bernoulli")
    parser.add_argument("-max_height",
                        type=float,
                        help="Maximum size in y direction.",
                        default=3.0)
    parser.add_argument("-max_width",
                        type=float,
                        help="Maximum size in x direction.",
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
    if args.alg == "bernoulli":
        y, x = pg.lemniscate_of_bernoulli(t, [args.max_height, args.max_width])
    elif args.alg == "gerono":
        y, x = pg.lemniscate_of_gerono(t, [args.max_height, args.max_width])
    else:
        print("Do not know type: {}".format(args.type))
        exit(1)
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
        i = np.linspace(0, args.n - 1, num=args.n)
        h = plt.scatter(x, y, marker="v", c=i)
        plt.scatter(x[0], y[0], marker="o")
        plt.gca().set_aspect("equal", adjustable="box")
        plt.colorbar(h)
        plt.show()


if __name__ == "__main__":
    main(rospy.myargv(argv=sys.argv))
