# bindingenergy.py
"""
A programme to calculate the total binding energy between an increasing
number of objects given the pairwise distances between each object.
"""
import argparse
import numpy as np
from pathlib import Path

# ----
# Constants
# -----
SIGMA=3.41e-10
EPSILON=1.65e-21


def calculate_binding_energy(r):
    """
    Calculate the binding energy between two objects separated by distance r.
    """
    be = 4 * EPSILON * ((SIGMA / r) ** 12 - (SIGMA / r) ** 6)
    return be


def total_binding_energy(object_distances):
    """
    Calculate total binding energy for all pairwise distances.
    """
    total_energy = sum(calculate_binding_energy(r) for r in object_distances)
    return total_energy


def read_object_distances(file_path):
    """Read pairwise object distances from a file."""
    with open(file_path, "rt") as fh:
        distances = [float(line.strip()) for line in fh]
    return distances


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate the total binding energy of objects based on pairwise distances.")
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("-d",
                             "--distances",
                             type=float,
                             nargs="+",
                             help="Pairwise distances between objects (in meters) as space separated list, e.g. 1e-10, 2e-10, 1.5e-10'"
    )
    input_group.add_argument("-f", "--file", type=Path, help="File containing a list of pairwise distances.")
    parser.add_argument("-o", "--output", type=Path, help='Optional output file to write the results.')

    args = parser.parse_args()
    import sys

    # Get distances depending on how they are provided (on command line or file)
    if args.distances:
        distances = args.distances
    elif args.file:
        distances = read_object_distances(args.file)


    # Calculate total binding energy
    total_energy = total_binding_energy(distances)

    # Results summary
    # Always printed to screen and written to file if option provided.
    result_msg = f"Total Binding Energy: {total_energy:.6e} J"
    print(result_msg)

    if args.output:
        with open(args.output, "wt") as fh:
            fh.write(result_msg)
            fh.write("\n")
        print(f"Results written to {args.output}")
