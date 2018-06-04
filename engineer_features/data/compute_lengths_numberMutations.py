import pandas as pd
import numpy as np
import sys
import argparse


def main():

    df = pd.read_csv(sys.stdin, sep='\t')

    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    parser.add_argument('--columns', nargs='*')
    args = parser.parse_args()

    df.columns = args.columns

    df = df[df.varflag != 'VARTRUE']
    df['length'] = df['end'] - df['start']

    group = df.groupby('unique_key', as_index=False)

    df1 = pd.DataFrame(group[['number_of_mutations', 'length']].sum())
    df1 = df1.rename(columns={'number_of_mutations': 'total_number_of_mutations', 'length': 'total_length'})

    df2 = df.loc[[np.array(indices)[0] for indices in group.groups.values()]]

    df3 = pd.merge(df1, df2, on='unique_key').drop(columns=['start', 'end', 'number_of_mutations', 'length'])

    df3.to_pickle(args.file)


if __name__ == '__main__':
    main()
