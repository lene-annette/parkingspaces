'''
    Functions to be used in order to analyze csv file. 
'''


def count_indreby(data_set):
    count = 0
    space_on_road = 0
    road_with_most_spots = ''
    for data in data_set:
        if data[6] == 'Indre By':
            count += data[2]
            if data[2] > space_on_road:
                space_on_road = data[2]
                road_with_most_spots = data[1]
    return f'\nThere are {count} parking spaces in Indre By & the road with the most parkingspots is {road_with_most_spots}'

def even_or_uneven(data_set):
    even = []
    uneven= []
    for data in data_set:
        if data[5] == 'Lige husnr.':
            even.append(data)
        elif data[5] == 'Ulige husnr.':
            uneven.append(data)
    even_marked = 0
    uneven_marked = 0
    #Making it search for only 'Af' because data is faulty so æ is just a box of dots
    for e in even:
        if e[8][0:2] == 'Af':
            even_marked += 1
    for u in uneven:
        if u[8][0:2] == 'Af':
            uneven_marked += 1

    #uneven_marked is the larger number
    #Even has the most spots
    if len(even) > len(uneven):
        return f'\nThere is most parking spot in the even side with {len(even)} but there are more spots with marked parking in the uneven side with {uneven_marked}'

    elif len(even) < len(uneven):
        return f'\nThere is most parking spot in the uneven side with {len(uneven)} spots'

def distibution_of_public_vs_nonpublic(data_set):
    list_of_subcity = []
    list_of_privat_parking = []

    for data in data_set:
        if data[6] not in list_of_subcity:
            list_of_subcity.append(data[6])
        else:
            continue

    list_of_privat_parking = []
    list_of_public_parking = []
    c1=c2=c3=c4=c5=c6=c7=c8=c9=c10 = 0
    oc1=oc2=oc3=oc4=oc5=oc6=oc7=oc8=oc9=oc10 = 0

    
    for data in data_set:
        if data[6] == 'Vesterbro-Kongens Enghave' and 'Privat' in data[4]:
            c1 += 1
        elif data[6] == 'Indre By' and 'Privat' in data[4]:
            c2 += 1
        elif 'Husum' in data[6][9:14] and 'Privat' in data[4]:
            c3 += 1
        elif 'Vanl' in data[6][:4] and 'Privat' in data[4]:
            c4 += 1
        elif data[6] == 'Valby' and 'Privat' in data[4]:
            c5 += 1
        elif 'Amager' in data[6] and 'st' in data[6][8:10] and 'Privat' in data[4]:
            c6 += 1
        elif data[6] == 'Amager Vest' and 'Privat' in data[4]:
            c7 += 1
        elif data[6][1:] == 'sterbro' and 'Privat' in data[4]:
            c8 += 1
        elif data[6][2:8] == 'rrebro' and 'Privat' in data[4]:
            c9 += 1
        elif data[6] == 'Bispebjerg' and 'Privat' in data[4]:
            c10 += 1
    list_of_privat_parking.extend([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10])

    for data in data_set:
        if data[6] == 'Vesterbro-Kongens Enghave' and 'Kommunevej' in data[4]:
            oc1 += 1
        elif data[6] == 'Indre By' and 'Kommunevej' in data[4]:
            oc2 += 1
        elif 'Husum' in data[6][9:14] and 'Kommunevej' in data[4]:
            oc3 += 1
        elif 'Vanl' in data[6][:4] and 'Kommunevej' in data[4]:
            oc4 += 1
        elif data[6] == 'Valby' and 'Kommunevej' in data[4]:
            oc5 += 1
        elif 'Amager' in data[6] and 'st' in data[6][8:10] and 'Kommunevej' in data[4]:
            oc6 += 1
        elif data[6] == 'Amager Vest' and 'Kommunevej' in data[4]:
            oc7 += 1
        elif data[6][1:] == 'sterbro' and 'Kommunevej' in data[4]:
            oc8 += 1
        elif data[6][2:8] == 'rrebro' and 'Kommunevej' in data[4]:
            oc9 += 1
        elif data[6] == 'Bispebjerg' and 'Kommunevej' in data[4]:
            oc10 += 1
    list_of_public_parking.extend([oc1,oc2,oc3,oc4,oc5,oc6,oc7,oc8,oc9,oc10])
    del list_of_subcity[-2]
    print(list_of_subcity)
    return (list_of_subcity, list_of_privat_parking, list_of_public_parking)