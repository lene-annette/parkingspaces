import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import os
import matplotlib.dates as mdates
import pandas as pd
from matplotlib.ticker import FuncFormatter


def bar_plot_public_vs_private(y1,y2):

    my_sum = sum(y1) + sum(y2)
    new_y1 = [(x/my_sum)*100 for x in y1]
    new_y2 = [(x/my_sum)*100 for x in y2]

    bar_width = 0.4
    x = 10
    ind = np.arange(x)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    reacts1 = ax.bar(ind, new_y1, bar_width, color='royalblue')
    reacts2 = ax.bar(ind+bar_width, new_y2, bar_width, color='seagreen')
    ax.set_ylabel('Parking spots in %')
    ax.set_title('Parking spots public/private in Copenhagen')
    ax.set_xticks(ind + bar_width / 2)
    ax.set_xticklabels( ('Vesterbro', 'Indre By', 'Brønshøj-Husum','Vanløse','Valby','Amager Øst','Amager Vest','Østerbro','Nørrebro','Bispebjerg'))
    plt.xticks(rotation=60)
    ax.legend(['Private','Public'])
    plt.show()

def plot_parking_vs_income(earnings,private_list,ecars):
    bar_width = 0.4
    x =10
    index = np.arange(x)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    reacts1 = ax.bar(index, private_list, bar_width, color='red')
    reacts2 = ax.bar(index+bar_width, ecars, bar_width, color='seagreen')
    ax.set_xticks(index + bar_width / 2)
    plt.xticks(rotation=60)
    ax.set_xlabel('average earnings')
    ax.set_ylabel('antal parkerings pladser')
    ax.set_xticklabels( ('Vesterbro', 'Indre By', 'Brønshøj-Husum','Vanløse','Valby','Amager Øst','Amager Vest','Østerbro','Nørrebro','Bispebjerg'))
    ax.legend(['Privat','Elbil'])
    plt.show()