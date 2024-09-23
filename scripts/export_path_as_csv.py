#!/usr/bin/env python3
import argparse

import yaml


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    filename: str = args.filename

    with open(filename, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)
    waypoints = data['waypoints']
    filename = filename.replace('yaml', 'csv')
    print(f'Writing file {filename}')
    with open(filename, 'w') as csv_file:
        csv_file.write('x, y, z\n')
        for waypoint in waypoints:
            line = (
                ','.join(
                    [str(waypoint['x']), str(waypoint['y']), str(waypoint['z'])]
                )
                + '\n'
            )
            csv_file.write(line)


if __name__ == '__main__':
    main()
