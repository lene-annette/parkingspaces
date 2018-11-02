'''
Usage: 
    python main.py [<url>]
Example:
   python main.py http://wfs-kbhkort.kk.dk/k101/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=k101:p_pladser&outputFormat=csv&SRSNAME=EPSG:4326
'''

import os
import sys
from lib.converter import convert
from lib.download import download 
import lib.plotting as plotter
import lib.statistic as stat

if __name__ == '__main__':
    print('Plain product cph parking analyzer:')

    file_dir = 'csv'
    # If the csv directory doesn't already exits it will be created.
    # if not os.path.isdir(file_dir):
    #     os.makedirs(file_dir)
    # try:
    #     _, url = sys.argv
    #     file_name = os.path.join(file_dir, os.path.basename(url))
    #     print(f'\nDownloading file : {os.path.basename(url)} ...')
    #     download(url, file_name)  
    #     print('Download completed succesfully!')
    # except Exception as e:
    #     print(__doc__)
    #     sys.exit(1)  

    file_name = 'p_pladser.csv' 
    data_set = convert(file_name)

    print(stat.count_indreby(data_set))
    print(stat.even_or_uneven(data_set))
    x, y1, y2 = stat.distibution_of_public_vs_nonpublic(data_set)
    print(plotter.bar_plot_public_vs_private(x,y1,y2))
