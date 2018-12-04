#!/usr/bin/python3

import numpy as np
import argparse
import os

parser = argparse.ArgumentParser(description='Generate test data for Quadratic Assignment problem.')
parser.add_argument('N', type=int, help='Number of locations and factories')
parser.add_argument('-o', type=str, help='output file name')

args = parser.parse_args()

points = np.random.randint(0, 1000, size=(2, args.N))
indexes = np.arange(0, args.N)

locations = np.random.randint(0, 1000, size=(args.N, args.N))
locations = (locations + locations.T) / 2 - np.diag(locations.diagonal())

flow = np.random.randint(0, 1000, size=(args.N, args.N))
flow = (flow + flow.T) / 2 - np.diag(flow.diagonal())

zeroFlow = np.random.randint(0, args.N, size=(args.N, 2))
for i, j in zeroFlow:
    flow[i][j] = 0
    flow[j][i] = 0

out = f'qa_{args.N}.out'
if args.o:
    out = args.o

if os.path.isdir('qa_data'):
    out = os.path.join('qa_data', out)

with open(out, 'w') as file:
    np.savetxt(file, locations, fmt='%4d', header=f'Locations: {args.N}')
    np.savetxt(file, flow, fmt='%4d', header='Flow:')

