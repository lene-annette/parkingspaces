'''
converts the csv file into a more useful representation of the data for our exercise
'''

import csv

def convert(file_name):
    '''
        this function cleans the data in the given csv file
    '''

    print('\nReading data from file to memory...')
    
    with open(file_name,encoding='utf-8') as fp:
        reader = csv.reader(fp)
        next(reader)
        data_set = []

        print('cleaning up data...')
        
        for line in reader: 
            try:
                _,vejkode,vejnavn,antal_pladser,restriktion,vejstatus,vejside,bydel,p_ordning,p_type,_,_,_,_,_,_,_,_ = line
                #converting strings to int or float
                antal_pladser = int(antal_pladser)
                #appending cleaned data to array
                data_set.append([vejkode,vejnavn,antal_pladser,restriktion,vejstatus,vejside,bydel,p_ordning,p_type])
            except:
                pass

    print('finished reading and cleaning data!')
    return data_set
