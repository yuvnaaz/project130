import pandas as pd
import csv

df = pd.read_csv("main.csv")

del df['Index']
del df['index']

df = df.rename({
    'star_name': 'brown_dwarf_name',
    'distance': 'brown_dwarf_dist',
    'radius':'brown_dwarf_radius',
    'mass':'brown_dwarf_mass'
}, axis = 'columns')

df.to_csv('main.csv')