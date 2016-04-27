# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:05:32 2016


Does pivot-table work on the TBA data
"""

import pandas as pd
from tkinter import filedialog as fd

def crunchauto(df,idx):

    
    
    df['Moved'] = df['Crossing'] + df['Reach']
    
    melted = pd.melt(df, id_vars=['Week','Event','Match','Type'], var_name='AutoMeasure')
    melted.head()
    #pivoted = melted.pivot(index='Week', columns='AutoMeasure', values='value')
    pivoted = pd.pivot_table(melted, index=idx, columns='AutoMeasure', values='value')
    
    p2 = pd.pivot_table(df, index=idx, columns='Type', values='Moved')
    
    p2 = p2[['qm', 'qf', 'sf', 'f1']]
    
    print('Autonomous averages per match\n')
    print(pivoted)
    
    print('\nMean autonomous movement\n')
    print(p2)
    
    
    p3 = pd.pivot_table(df, index=idx, columns='Type', values='Low')
    p3 = p3[['qm', 'qf', 'sf', 'f1']]
    
    print('\nMean autonomous low goals\n')
    print(p3)
    
    p3 = pd.pivot_table(df, index=idx, columns='Type', values='High')
    p3 = p3[['qm', 'qf', 'sf', 'f1']]
    
    print('\nMean autonomous high goals\n')
    print(p3)
    
    #print(list(p2.columns.values))

def crunchtele(df):
   
    #print(list(df.columns.values))
    
    p1 = pd.pivot_table(df, index='Week', columns='Type', values='High')
    p1 = p1[['qm', 'qf', 'sf', 'f1']]
    print('\nMean teleop high goals\n')    
    print(p1)
    
    p1 = pd.pivot_table(df, index='Week', columns='Type', values='Low')
    p1 = p1[['qm', 'qf', 'sf', 'f1']]
    print('\nMean teleop Low goals\n')    
    print(p1)
    
    p1 = pd.pivot_table(df, index='Week', columns='Type', values='Challenges')
    p1 = p1[['qm', 'qf', 'sf', 'f1']]
    print('\nMean teleop Challenges\n')    
    print(p1)
    
    p1 = pd.pivot_table(df, index='Week', columns='Type', values='Scales')
    p1 = p1[['qm', 'qf', 'sf', 'f1']]
    print('\nMean teleop Scales\n')    
    print(p1)
    
    p1 = pd.pivot_table(df, index='Week', columns='Type', values='Breaches')
    p1 = p1[['qm', 'qf', 'sf', 'f1']]
    print('\nMean teleop Breaches\n')    
    print(p1)
    
    p1 = pd.pivot_table(df, index='Week', columns='Type', values='Captures')
    p1 = p1[['qm', 'qf', 'sf', 'f1']]
    print('\nMean teleop Captures\n')    
    print(p1)

def crunchdef(file):
    pass
    
def go():
    afile='C://Users//stat//Documents//GitHub//2016Scouting-DefenseSetup-and-Crunching//General Analysis//data through week 5-auto.csv'
    adf = pd.read_csv(afile)
    crunchauto(adf, 'Week')
    
    tfile='C://Users//stat//Documents//GitHub//2016Scouting-DefenseSetup-and-Crunching//General Analysis//data through week 5-tele.csv'
    tdf = pd.read_csv(tfile)    
    crunchtele(tdf)
    
    dfile='C://Users//stat//Documents//GitHub//2016Scouting-DefenseSetup-and-Crunching//General Analysis//data through week 5-def.csv'
    ddf = pd.read_csv(dfile)        
    crunchdef(ddf)
    
    print('\nComparing our events:\n')
    asub = adf[adf.Event.isin(['mokc','ohci'])]
    crunchauto(asub, 'Event')
    