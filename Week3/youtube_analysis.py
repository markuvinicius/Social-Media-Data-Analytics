#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 23:03:13 2017

@author: Marku
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm



def youtube_analysis(options):

    #load youtube file
    youtube_data = pd.read_csv(options.f)  
    
    h = options.hist
    if ( h ):            
        plt.figure()
        hist,edges1 = np.histogram(youtube_data.viewCount)
        plt.bar(edges1[:-1],hist,width=edges1[1:]-edges1[:-1])
        plt.savefig(h)
        
    corr = options.corr
    if ( corr ):
        print(youtube_data.corr())
        
    scatt = options.scatter
    if (scatt):
        print(scatt)
        #todo: Gerar e salvar graficos de dispersão para todas as dimensões 

        #plt.figure()
        #plt.scatter(youtube_data[scatt[0]],youtube_data[scatt[1]])
        #plt.savefig(scatt[2])
        
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Youtube Analysis')
    parser.add_argument("-f", help="Read From File", default="")
    parser.add_argument("-hist", help="Histogram", default="")
    parser.add_argument("-corr", help="correlation", default="")
    parser.add_argument("-scatter", help="Scatter Plot", default="")
    args = parser.parse_args()

    youtube_analysis(args)


l = "[dislikeCount,commentCount,scatt_disl_com]"

s = l.split(",")

type(s)

s