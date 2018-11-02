'''
    Functions to be used in order to analyze csv file. 
'''


def count_indreby(data_set):
    count = 0
    for data in data_set:
        if data[6] == 'Indre By':
            count += data[2]
    return f'\nThere are {count} parking spaces in Indre By'