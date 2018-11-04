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

def convert2(file_name):
    '''
        this function cleans the data in the given csv file
    '''

    print('\nReading data from file to memory...')
    
    with open(file_name) as fp:
        reader = csv.reader(fp)
        next(reader)
        data_set2 = []

        print('cleaning up data...')
        
        for line in reader: 
            try:
                AAR,BYDEL,DISTRIKTSNAVN,HUSTYPE,FAMILIEGRUPPE,FAMILIETYPE,BRUTTOINDKOM,INDKOMSTKATEGORI,HUSTANDE = line
                #converting strings to int or float
                hustande = int(HUSTANDE)
                bruttoindkom = int(BRUTTOINDKOM)
                #appending cleaned data to array
                #OBS der er byttet om på BRUTTOINKOM og INDKOMST KATEGORI i data sættet
                data_set2.append([AAR,BYDEL,DISTRIKTSNAVN,HUSTYPE,FAMILIEGRUPPE,FAMILIETYPE,bruttoindkom,INDKOMSTKATEGORI,hustande])
            except:
                pass

    print('finished reading and cleaning data!')
    return data_set2
