import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import os
import matplotlib.dates as mdates
import pandas as pd


def bar_plot_public_vs_private(x,y1,y2):

    bar_width = 0.4
    new_x = 10
    ind = np.arange(new_x)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    reacts1 = ax.bar(ind, y1, bar_width, color='royalblue')
    reacts2 = ax.bar(ind+bar_width, y2, bar_width, color='seagreen')
    ax.set_ylabel('Parking spots')
    ax.set_title('Parking spots public/private in Copenhagen')
    ax.set_xticks(ind + bar_width / 2)
    ax.set_xticklabels( ('Vesterbro-Kongens Enghave', 'Indre By', 'Brønshøj-Husum','Vanløse','Valby','Amager Øst','Amager Vest','Østerbro','Nørrebro','Bispebjerg'))
    plt.xticks(rotation=90)
    ax.legend(['Private','Public'])
    plt.show()