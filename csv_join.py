from os import path
from sys import stderr
from sys import exit
import glob
import pandas as pd

import argparse

parser = argparse.ArgumentParser(description='Join csv files')
parser.add_argument('--directory',
                    dest="directory",
                    required=True,
                    type=str,
                    help='the csv directory to join files from')

args = parser.parse_args()

if not path.isdir(args.directory):
    stderr.write(f'Directory is not a folder or does not exist: {args.directory}')
    exit(1)

def get_files(directory):    
    file_extension = '.csv'
    return [i for i in glob.glob(f"{directory}/*{file_extension}")]

def read_csv(path):
    return pd.read_csv(path, delimiter=',', encoding='UTF-16')

directory = path.abspath(args.directory)
csv_files = get_files(directory)

joined = pd.concat(map(read_csv, csv_files))
print(joined.to_csv())