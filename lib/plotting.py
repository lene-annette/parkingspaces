import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import os
import pandas as pd
from matplotlib.ticker import FuncFormatter


def bar_plot_public_vs_private(y1,y2):
    plot_file = f'plot0.png'
    plot_dir = 'plots'
    # If the plot directory is not already present it will be created.
    if not os.path.isdir(plot_dir):
        os.makedirs(plot_dir)

    my_sum = sum(y1) + sum(y2)
    new_y1 = [(x/my_sum)*100 for x in y1]
    new_y2 = [(x/my_sum)*100 for x in y2]

    bar_width = 0.4
    x = 10
    ind = np.arange(x)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(ind, new_y1, bar_width, color='royalblue')
    ax.bar(ind+bar_width, new_y2, bar_width, color='seagreen')
    ax.set_ylabel('Parking spots in %')
    ax.set_title('Parking spots public/private in Copenhagen')
    ax.set_xticks(ind + bar_width / 2)
    ax.set_xticklabels( ('Vesterbro', 'Indre By', 'Brønshøj-Husum','Vanløse','Valby','Amager Øst','Amager Vest','Østerbro','Nørrebro','Bispebjerg'))
    plt.xticks(rotation=60)
    ax.legend(['Private','Public'])
    plt.savefig(os.path.join(plot_dir, plot_file))
    plt.show()
    plt.close()
def plot_parking_vs_income(df_private,df_ecar):
    plot_file = f'plot1.png'
    plot_dir = 'plots'
    # If the plot directory is not already present it will be created.
    if not os.path.isdir(plot_dir):
        os.makedirs(plot_dir)
 
    ax = plt.gca()
    df_p = df_private.sort_values('earnings',ascending=True)
    df_epark = df_ecar.sort_values('earnings',ascending=True)
    df_p.plot(kind='line', x='earnings', y='private',ax=ax)
    df_epark.plot(kind='line', x='earnings', y='Ecar parking',ax=ax)
    
    plt.ylabel('Number of parking spots')
    plt.xlabel('Earnings of city')
    ax.set_xticks(df_p.earnings)
    plt.xticks(rotation=45)
    ax.set_xticklabels(df_p['city_name'], minor=False)
    ax.set_xticklabels(df_p['earnings'], minor=True)
    plt.savefig(os.path.join(plot_dir, plot_file))
    plt.show()
    plt.close()