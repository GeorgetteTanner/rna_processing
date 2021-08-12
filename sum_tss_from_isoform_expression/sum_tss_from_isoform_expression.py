# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 11:50:55 2020

@author: medgnt
"""

import pandas as pd
import numpy as np
import argparse

parser = argparse.ArgumentParser(description="Sum expression of isoforms that share a transcription start site.")
parser.add_argument('-i', '--input', required=True, dest='input', help='Expression input file.')
parser.add_argument('-t', '--trans', required=True, dest='trans', help='Name of column containing transcript IDs.')
parser.add_argument('-e', '--exp', required=True, dest='exp', help='Comma separated list of names of columns containing expression values.')
parser.add_argument('-s', '--samples', required=False, dest='samples', help='Optional comma separated list of sample names to overwrite expression column headers.')
parser.add_argument('-m', '--mapping', required=True, dest='mapping', help='Mapping file for transcript to tss positions.')
parser.add_argument('-o', '--output', required=True, dest='output', help='Output directory and prefix for file names.')

args = parser.parse_args()
data = pd.read_table(args.input,sep='\t',header=0,index_col=False)

tssi={}
with open(args.mapping,'r+') as file:
    for line in file:
        l=line.strip().split()
        tssi[l[0]]=l[1]

for c in data.columns:
    if c not in args.exp.strip().split(',') and c !=args.trans:
        del data[c]
        print(c)
print(args.exp.strip().split(','))
tss=[]
dro=[]
for t in data[args.trans]:
    if t in tssi:
        tss.append(tssi[t])
    else:
        dro.append(t)
data.drop(dro,inplace=True)
print("Transcript IDs not listed in mappings files: " +str(len(dro)))

data['tss']=tss
print(str(data.columns))
data2=data.groupby(['tss']).sum()
print(str(data.columns))
data=data2

print(str(data.columns))
renames={}
if args.samples:
    for i in range(len(args.exp.strip().split(','))):
        renames[args.exp.strip().split(',')[i]]=args.samples.strip().split(',')[i]
print(str(data.columns))

data.rename(columns = renames, inplace = True)
print(str(data.columns))
data.to_csv(args.output+'_tss_expression.txt',sep='\t',header=True,index=True)

