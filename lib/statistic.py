'''
    Functions to be used in order to analyze csv file. 
'''
import collections

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
    return (list_of_privat_parking, list_of_public_parking)

def famili_type_best_options (data_set):
    return 'WTF'

def distribution_of_parkingspots_for_income (data_set, data_set2):
    list_privat, list_public = distibution_of_public_vs_nonpublic(data_set)
    list_of_ecar = []
    c1=c2=c3=c4=c5=c6=c7=c8=c9=c10 = 0
    for data in data_set:
        if data[6] == 'Vesterbro-Kongens Enghave' and 'El-Bil plads' in data[7]:
            c1 += 1
        elif data[6] == 'Indre By' and 'El-Bil pladsvat' in data[7]:
            c2 += 1
        elif 'Husum' in data[6][9:14] and 'El-Bil plads' in data[7]:
            c3 += 1
        elif 'Vanl' in data[6][:4] and 'El-Bil plads' in data[7]:
            c4 += 1
        elif data[6] == 'Valby' and 'El-Bil plads' in data[7]:
            c5 += 1
        elif 'Amager' in data[6] and 'st' in data[6][8:10] and 'El-Bil plads' in data[7]:
            c6 += 1
        elif data[6] == 'Amager Vest' and 'El-Bil plads' in data[7]:
            c7 += 1
        elif data[6][1:] == 'sterbro' and 'El-Bil plads' in data[7]:
            c8 += 1
        elif data[6][2:8] == 'rrebro' and 'El-Bil plads' in data[7]:
            c9 += 1
        elif data[6] == 'Bispebjerg' and 'El-Bil plads' in data[7]:
            c10 += 1
    list_of_ecar.extend([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10])
    indkomst1=indkomst2=indkomst3=indkomst4=indkomst5=indkomst6=indkomst7=indkomst8=indkomst9=indkomst10 = 0
    list_of_earnings = []
    hustande1=hustande2=hustande3=hustande4=hustande5=hustande6=hustande7=hustande8=hustande9=hustande10= 0
    for data in data_set2:
        if data[2] == '1. Indre By':
            hustande1 += data[8]
            if data[6] == 1:
                indkomst1 += data[8]*(-50000)
            elif data[6] == 2:
                indkomst1 += data[8]*75000
            elif data[6] == 3:
                indkomst1 += data[8]*125000
            elif data[6] == 4:
                indkomst1 += data[8]*175000
            elif data[6] == 5:
                indkomst1 += data[8]*250000
            elif data[6] == 6:
                indkomst1 += data[8]*350000
            elif data[6] == 7:
                indkomst1 += data[8]*450000
            elif data[6] == 8:
                indkomst1 += data[8]*550000
            elif data[6] == 9:
                indkomst1 += data[8]*650000
            elif data[6] == 10:
                indkomst1 += data[8]*700000
        elif data[2] == '2. Østerbro':
            hustande2 += data[8]
            if data[6] == 1:
                indkomst2 += data[8]*(-50000)
            elif data[6] == 2:
                indkomst2 += data[8]*75000
            elif data[6] == 3:
                indkomst2 += data[8]*125000
            elif data[6] == 4:
                indkomst2 += data[8]*175000
            elif data[6] == 5:
                indkomst2 += data[8]*250000
            elif data[6] == 6:
                indkomst2 += data[8]*350000
            elif data[6] == 7:
                indkomst2 += data[8]*450000
            elif data[6] == 8:
                indkomst2 += data[8]*550000
            elif data[6] == 9:
                indkomst2 += data[8]*650000
            elif data[6] == 10:
                indkomst2 += data[8]*700000
            
        elif data[2] == '3. Nørrebro':
            hustande3 += data[8]
            if data[6] == 1:
                indkomst3 += data[8]*(-50000)
            elif data[6] == 2:
                indkomst3 += data[8]*75000
            elif data[6] == 3:
                indkomst3 += data[8]*125000
            elif data[6] == 4:
                indkomst3 += data[8]*175000
            elif data[6] == 5:
                indkomst3 += data[8]*250000
            elif data[6] == 6:
                indkomst3 += data[8]*350000
            elif data[6] == 7:
                indkomst3 += data[8]*450000
            elif data[6] == 8:
                indkomst3 += data[8]*550000
            elif data[6] == 9:
                indkomst3 += data[8]*650000
            elif data[6] == 10:
                indkomst3 += data[8]*700000
        elif data[2] == '4. Vesterbro/Kongens Enghave':
            hustande4 += data[8]
            if data[6] == 1:
                indkomst4 += data[8]*(-50000)
            elif data[6] == 2:
                indkomst4 += data[8]*75000
            elif data[6] == 3:
                indkomst4 += data[8]*125000
            elif data[6] == 4:
                indkomst4 += data[8]*175000
            elif data[6] == 5:
                indkomst4 += data[8]*250000
            elif data[6] == 6:
                indkomst4 += data[8]*350000
            elif data[6] == 7:
                indkomst4 += data[8]*450000
            elif data[6] == 8:
                indkomst4 += data[8]*550000
            elif data[6] == 9:
                indkomst4 += data[8]*650000
            elif data[6] == 10:
                indkomst4 += data[8]*700000
        elif data[2] == '5. Valby':
            hustande5 += data[8]
            if data[6] == 1:
                indkomst5 += data[8]*(-50000)
            elif data[6] == 2:
                indkomst5 += data[8]*75000
            elif data[6] == 3:
                indkomst5 += data[8]*125000
            elif data[6] == 4:
                indkomst5 += data[8]*175000
            elif data[6] == 5:
                indkomst5 += data[8]*250000
            elif data[6] == 6:
                indkomst5 += data[8]*350000
            elif data[6] == 7:
                indkomst5 += data[8]*450000
            elif data[6] == 8:
                indkomst5 += data[8]*550000
            elif data[6] == 9:
                indkomst5 += data[8]*650000
            elif data[6] == 10:
                indkomst5 += data[8]*700000
        elif data[2] == '6. Vanløse':
            hustande6 += data[8]
            if data[6] == 1:
                indkomst6 += data[8]*(-50000)
            elif data[6] == 2:
                indkomst6 += data[8]*75000
            elif data[6] == 3:
                indkomst6 += data[8]*125000
            elif data[6] == 4:
                indkomst6 += data[8]*175000
            elif data[6] == 5:
                indkomst6 += data[8]*250000
            elif data[6] == 6:
                indkomst6 += data[8]*350000
            elif data[6] == 7:
                indkomst6 += data[8]*450000
            elif data[6] == 8:
                indkomst6 += data[8]*550000
            elif data[6] == 9:
                indkomst6 += data[8]*650000
            elif data[6] == 10:
                indkomst6 += data[8]*700000
        elif data[2] == '7. Brønshøj-Husum':
            hustande7 += data[8]
            if data[6] == 1:
                indkomst7 += data[8]*(-50000)
            elif data[6] == 2:
                indkomst7 += data[8]*75000
            elif data[6] == 3:
                indkomst7 += data[8]*125000
            elif data[6] == 4:
                indkomst7 += data[8]*175000
            elif data[6] == 5:
                indkomst7 += data[8]*250000
            elif data[6] == 6:
                indkomst7 += data[8]*350000
            elif data[6] == 7:
                indkomst7 += data[8]*450000
            elif data[6] == 8:
                indkomst7 += data[8]*550000
            elif data[6] == 9:
                indkomst7 += data[8]*650000
            elif data[6] == 10:
                indkomst7 += data[8]*700000
        elif data[2] == '8. Bispebjerg':
            hustande8 += data[8]
            if data[6] == 1:
                indkomst8 += data[8]*(-50000)
            elif data[6] == 2:
                indkomst8 += data[8]*75000
            elif data[6] == 3:
                indkomst8 += data[8]*125000
            elif data[6] == 4:
                indkomst8 += data[8]*175000
            elif data[6] == 5:
                indkomst8 += data[8]*250000
            elif data[6] == 6:
                indkomst8 += data[8]*350000
            elif data[6] == 7:
                indkomst8 += data[8]*450000
            elif data[6] == 8:
                indkomst8 += data[8]*550000
            elif data[6] == 9:
                indkomst8 += data[8]*650000
            elif data[6] == 10:
                indkomst8 += data[8]*700000
        elif data[2] == '9. Amager Øst':
            hustande9 += data[8]
            if data[6] == 1:
                indkomst9 += data[8]*(-50000)
            elif data[6] == 2:
                indkomst9 += data[8]*75000
            elif data[6] == 3:
                indkomst9 += data[8]*125000
            elif data[6] == 4:
                indkomst9 += data[8]*175000
            elif data[6] == 5:
                indkomst9 += data[8]*250000
            elif data[6] == 6:
                indkomst9 += data[8]*350000
            elif data[6] == 7:
                indkomst9 += data[8]*450000
            elif data[6] == 8:
                indkomst9 += data[8]*550000
            elif data[6] == 9:
                indkomst9 += data[8]*650000
            elif data[6] == 10:
                indkomst9 += data[8]*700000
        elif data[2] == '10. Amager Vest':
            hustande10 += data[8]
            if data[6] == 1:
                indkomst10 += data[8]*(-50000)
            elif data[6] == 2:
                indkomst10 += data[8]*75000
            elif data[6] == 3:
                indkomst10 += data[8]*125000
            elif data[6] == 4:
                indkomst10 += data[8]*175000
            elif data[6] == 5:
                indkomst10 += data[8]*250000
            elif data[6] == 6:
                indkomst10 += data[8]*350000
            elif data[6] == 7:
                indkomst10 += data[8]*450000
            elif data[6] == 8:
                indkomst10 += data[8]*550000
            elif data[6] == 9:
                indkomst10 += data[8]*650000
            elif data[6] == 10:
                indkomst10 += data[8]*700000
    average1 = indkomst1/hustande1
    average2= indkomst2/hustande2
    average3 = indkomst3/hustande3
    average4 = indkomst4/hustande4
    average5 = indkomst5/hustande5
    average6 = indkomst6/hustande6
    average7 = indkomst7/hustande7
    average8 = indkomst8/hustande8
    average9 = indkomst9/hustande9
    average10 = indkomst10/hustande10
    list_of_earnings.extend([average4,average1,average7,average6,average5,average9,average10,average2,average3,average8])
    return (list_of_earnings, list_privat, list_of_ecar)
