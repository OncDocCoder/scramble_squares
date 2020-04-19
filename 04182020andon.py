import colorama
from colorama import Fore, Back, Style

card3 = [[-4, 1, 3, 2, 'North', 'A'], [4, 2, -2, 3, 'North', 'B'], [-4, 2, 3, -1, 'North', 'C'],
        [1, -2, -3, -4, 'North', 'D'], [-3, 2, -1, 1, 'North', 'E'], [-3, -2, 4, -1, 'North', 'F'],
        [-2, -3, -1, 4, 'North', 'G'], [4, 2, -3, -1, 'North', 'H'], [-3, -4, -1, 4, 'North', 'I']]  # hotrods
card = [[3, 2, -1, -3, 'North', 'A'], [3, -1, 2, -1, 'North', 'B'], [-4, -3, 2, 4, 'North', 'C'],
         [1, -2, -4, 3, 'North', 'D'], [4, -1, -2, 4, 'North', 'E'], [-2, -4, -3, 1, 'North', 'F'],
         [-2, 4, 1, -3, 'North', 'G'], [1, -3, -2, 4, 'North', 'H'], [-2, 1, -3, 4, 'North', 'I']]  # guitars
card2 = [[-4, 2, 1, -3, 'North', 'A'], [-2, 4, 3, -1, 'North', 'B'], [-3, -4, -1, -2, 'North', 'C'],
        [2, 3, 1, -1, 'North', 'D'], [4, -1, -2, -3, 'North', 'E'], [4, -4, -2, 1, 'North', 'F'],
        [-3, 1, -2, 4, 'North', 'G'], [-2, 4, 3, 1, 'North', 'H'], [3, 4, 2, -1, 'North', 'I']]  # sharks

fillercard = [6, 6, 6, 6]
#for item in card:
##    for i, j in enumerate(item):
###       print(i, j)

def corner_compare(side_1, side_1_value, side_2,
                   side_2_value):
    result = []
    preresult = []
    # side1 is B side of the corner, side2 is A side of the corner. For NW, A side faces N. For SW, A side faces W, For SE, A side faces S. For NE, A side faces E.
    #print("corner compare")
    #print("side 1 value ", side_1_value)
    #print('sardine', side_2)
    #side_2.append(fillercard)
    a = len(side_2)
    # print("side 2 value is ", side_2_value)
    b = 0
    #print ("length of side 2 is ", a)
    for item in side_2:
        if side_1_value in item:
            preresult.append(item)
    #print("preresult is ", preresult)
    if len(preresult) > 0:
    # print("length of preresult is ", c)
        d = 0
        #preresult.append(fillercard)
        for item in preresult:
        # need to find out if values are next to each other
        # is the index of element2  one greater than element 1 unless index of element 2 is
        # 3 at which is the index of element2 equal to zero
            if item == fillercard or item == 6 :
                break
            else:
                index_preresult1 = preresult[d].index(side_1_value)
                index_preresult2 = preresult[d].index(side_2_value)
                if index_preresult2 == 3:
                    if index_preresult2 - 3 == index_preresult1:
                        result.append(preresult[d])
                        d += 1
                    else:
                        d += 1

                elif index_preresult2 + 1 == index_preresult1:
                    result.append(preresult[d])
                    d += 1
                else:
                    d += 1
    # print (" possible corner squares are",  result)
    corner_counter = len(result)
    #result.append(fillercard)
    #result.append(fillercard)
    #print("felix, " , result)
    return result

def cornercard(corner_value, centercard, first_candidate, second_candidate, third_candidate, fourth_candidate, fifth_candidate, sixth_candidate, seventh_candidate, eighth_candidate ):
    # finds the cards for corner, order--centercard, first_candidate is north, second is west, third is south, fourth is east, fifth is northwest, sixth is southwest, seventh is southeast, eighth is northeast
    corner_holder = []
    for target in card:
        if corner_value in target:
            corner_holder.append(target)
    if centercard in corner_holder:
        corner_holder.remove(centercard)
    if first_candidate in corner_holder:
        corner_holder.remove(first_candidate)
    if second_candidate in corner_holder:
        corner_holder.remove(second_candidate)
    if third_candidate in corner_holder:
        corner_holder.remove(third_candidate)
    if fourth_candidate in corner_holder:
        corner_holder.remove(fourth_candidate)
    if fifth_candidate in corner_holder:
        corner_holder.remove((fifth_candidate))
    if sixth_candidate in corner_holder:
        corner_holder.remove((sixth_candidate))
    if seventh_candidate in corner_holder:
        corner_holder.remove((seventh_candidate))
    if eighth_candidate in corner_holder:
        corner_holder.remove((eighth_candidate))
    corner_holder.append(fillercard)
    corner_holder.append(fillercard)
    #print("sigmund ", corner_holder)


    return corner_holder  # northeast_east cards from east

def totheright(card_to_test, index):
    # this gets the value to the right of the matching card
    card_for_index = card_to_test

    # print("card for index ", card_for_index)
    if index < 3:
        num_cardright = card_for_index[index + 1]
    else:
        num_cardright = card_for_index[index - 3]
    # print("the value facing to the right of the match is ", num_cardright)
    matcher_right = num_cardright * -1

    return (matcher_right)


def totheleft(card_to_test, index):
    # This gets the value to the left of the matching card
    card_for_index = card_to_test

    # print("card for index ", card_for_index)
    if index > 0:
        num_cardleft = card_for_index[index - 1]
    else:
        num_cardleft = card_for_index[index + 3]
    # print("the value facing to the left of the match is ", num_cardleft)
    matcher_left = num_cardleft * -1

    return (matcher_left)


def findtruecompass(anti_center_side, center_side, cardone, cardtwo, cardthree, cardfour, cardfive, cardsix, cardseven, cardeight) -> object:
    # finds cards for center north, west, south, east. cardone is center, cardtwo is north, cardthree is west, cardfour is south, cardfive is east, cardsix is northwest, cardseven is southwest, cardeight is southeast
    # print(Fore.BLUE)
    # print("center north is ", center_north)
    # print("anti center north is", anti_center_north)

    bag_holder = []
    for i in range(len(card)):

        if anti_center_side in card[i]:
            bag_holder.append(card[i])
    #print(cardthree, cardfour, cardfive)
    if centercard in bag_holder:
        bag_holder.remove(centercard)
    if cardtwo in bag_holder:
        bag_holder.remove(cardtwo)
    if cardthree in bag_holder:
        bag_holder.remove(cardthree)
    if cardfour in bag_holder:
        bag_holder.remove(cardfour)
    if cardfive in bag_holder:
        bag_holder.remove(cardfive)
    if cardsix in bag_holder:
        bag_holder.remove(cardsix)
    if cardseven in bag_holder:
        bag_holder.remove(cardseven)
    if cardeight in bag_holder:
        bag_holder.remove(cardeight)
    bag_holder.append(fillercard)
    bag_holder.append(fillercard)

    #print("pizzapie, " , bag_holder, end='')

    return bag_holder  # the array of possible center_north cards

def cards_for_center(candidate_c):
    center_north = candidate_c[0]
    center_west = candidate_c[3]
    center_south = candidate_c[2]
    center_east = candidate_c[1]
    anti_center_north = center_north * -1
    anti_center_east = center_east * -1
    anti_center_south = center_south * -1
    anti_center_west = center_west * -1
    return (
        center_north, anti_center_north, center_east, anti_center_east, center_south, anti_center_south, center_west,
        anti_center_west)

for centercard in card:
    # print(Fore.YELLOW)
    center_candidate = centercard
    print("Card in center ", center_candidate[5])
    ##print("hello")
    center_north, anti_center_north, center_east, anti_center_east, center_south, anti_center_south, center_west, anti_center_west = cards_for_center(
        center_candidate)
    north_holder = findtruecompass(anti_center_north, center_north, centercard, fillercard, fillercard, fillercard, fillercard, fillercard, fillercard, fillercard)
    #print(Fore.RED)
    #print(north_holder)
    #print(Style.RESET_ALL)



    for north_candidate in north_holder:
        if north_candidate == fillercard:
            break
        else:
            #north_candidate = north_holder[nnn]
            # print(Fore.MAGENTA)
            # print("Card to north is ", north_candidate[5], end='')
            # print(Style.RESET_ALL)
            index_anticenternorth = north_candidate.index(anti_center_north)
            nw_north_value = totheright(north_candidate, index_anticenternorth)
            ne_north_value = totheleft(north_candidate, index_anticenternorth)

            ####find west
            west_holder = findtruecompass(anti_center_west, center_west, centercard, north_candidate, fillercard, fillercard, fillercard, fillercard, fillercard, fillercard)
            # finds cards for center north, west, south, east. cardone is center, cardtwo is north, cardthree is west, cardfour is south, cardfive is east, cardsix is northwest, cardseven is southwest, cardeight is southeast
            #print(Fore.BLUE)
            #print(west_holder)
            #print(Style.RESET_ALL)
            #west_holder_counter = 0
            for west_candidate in west_holder:
                if west_candidate == fillercard:
                    break
                else:
                    index_anticenterwest = west_candidate.index(anti_center_west)
                    nw_west_value = totheleft(west_candidate, index_anticenterwest)
                    #print("turquoise ", nw_west_value)
                    sw_west_value = totheright(west_candidate, index_anticenterwest)
                    northwest_holder_north = cornercard(nw_north_value, centercard, north_candidate, west_candidate, fillercard, fillercard, fillercard, fillercard, fillercard, fillercard)
                     #print("red ", northwest_holder_north)
                    northwest_holder_west = cornercard(nw_west_value, centercard, north_candidate, west_candidate, fillercard, fillercard, fillercard, fillercard, fillercard, fillercard)  # cards in northwest from west
                    #print("purple ", northwest_holder_west)
                    northwest_holder = corner_compare(northwest_holder_west, nw_west_value,
                                                                  northwest_holder_north, nw_north_value)
                    #print("centercard, northcandidate, westcandidate", centercard, north_candidate, west_candidate)
                    #print("northwestholder ", northwest_holder)

                    for nw_candidate in northwest_holder:
                            #print(Fore.LIGHTCYAN_EX)
                            #print("northwest candidate is ", nw_candidate, end='')
                            #print(Style.RESET_ALL)
                        if nw_candidate == fillercard:
                            break
                        else:
                            #####find south
                            south_holder = findtruecompass(anti_center_south, center_south, centercard, north_candidate,
                                                                  west_candidate, fillercard, fillercard, nw_candidate, fillercard, fillercard)
                            # finds cards for center north, west, south, east. cardone is center, cardtwo is north, cardthree is west, cardfour is south,
                            # cardfive is east, cardsix is northwest, cardseven is southwest, cardeight is southeast


                            #print(Fore.MAGENTA)
                            #print("south holder ", south_holder)
                            #print(Style.RESET_ALL)




                            for south_candidate in south_holder:
                                if south_candidate == fillercard:
                                    break
                                else:
                                    index_anticentersouth = south_candidate.index(anti_center_south)
                                    sw_south_value = totheleft(south_candidate, index_anticentersouth)
                                    #print("turquoise ", sw_south_value)
                                    se_south_value = totheright(south_candidate, index_anticentersouth)
                                    sw_holder_south= cornercard(sw_south_value, centercard, north_candidate,
                                                                        west_candidate, south_candidate, fillercard, nw_candidate,
                                                                        fillercard, fillercard, fillercard)
                                    # finds the cards for corner, order--centercard, first_candidate is north, second is west, third is south, fourth is east,
                                    #   fifth is northwest, sixth is southwest, seventh is southeast, eighth is northeast
                                    #print(Fore.YELLOW)
                                    #print("red ", sw_holder_south)
                                    southwest_holder_west = cornercard(sw_west_value, centercard, north_candidate,
                                                                       west_candidate, south_candidate, fillercard, nw_candidate,
                                                                       fillercard, fillercard,
                                                                       fillercard)  # cards in northwest from west
                                    #print("purple ", southwest_holder_west)
                                    southwest_holder = corner_compare(sw_holder_south, sw_south_value, southwest_holder_west, sw_west_value )
                                    for sw_candidate in southwest_holder:
                                        if sw_candidate == fillercard:
                                            break
                                        else:
                                    #print("southwest holder   ", southwest_holder)
                                            east_holder = findtruecompass(anti_center_east, center_east, centercard, north_candidate,
                                                                      west_candidate, south_candidate, fillercard, nw_candidate, sw_candidate, fillercard)
                                            #print("Jumbo ", east_holder)
                                            # finds cards for center north, west, south, east.
                                            # cardone is center, cardtwo is north, cardthree is west, cardfour is south, cardfive is east,
                                            # cardsix is northwest, cardseven is southwest, cardeight is southeast
                                            for east_candidate in east_holder:
                                                if east_candidate == fillercard:
                                                    break
                                                else:
                                                    index_anticentereast = east_candidate.index(anti_center_east)
                                                    se_south_value = totheright(south_candidate, index_anticentersouth)
                                                    # print("turquoise ", sw_south_value)
                                                    se_east_value = totheleft(east_candidate, index_anticentereast)
                                                    ne_east_value = totheright(east_candidate, index_anticentereast)
                                                    print("vermont ", ne_east_value)
                                                    se_holder_south = cornercard(se_south_value, centercard,
                                                                                 north_candidate,
                                                                                 west_candidate, south_candidate,
                                                                                 east_candidate, nw_candidate,
                                                                                 sw_candidate, fillercard, fillercard)
                                                    # finds the cards for corner, order--centercard, first_candidate is north, second is west, third is south, fourth is east,
                                                    #   fifth is northwest, sixth is southwest, seventh is southeast, eighth is northeast
                                                    #print("puppy ", se_holder_south)
                                                    se_holder_east = cornercard(se_east_value, centercard,
                                                                                       north_candidate,
                                                                                       west_candidate, south_candidate,
                                                                                       east_candidate, nw_candidate,
                                                                                       sw_candidate, fillercard,
                                                                                       fillercard)  # cards in northwest from west
                                                    #print("doggie ", se_holder_east)
                                                    southeast_holder = corner_compare(se_holder_east, se_east_value,
                                                                                      se_holder_south,
                                                                                      se_south_value)
                                                    for se_candidate in southeast_holder:
                                                        if se_candidate == fillercard:
                                                            break
                                                        else:
                                                            ne_holder_north = cornercard(ne_north_value, centercard,
                                                                                         north_candidate,
                                                                                         west_candidate,
                                                                                         south_candidate,
                                                                                         east_candidate, nw_candidate,
                                                                                         sw_candidate, se_candidate,
                                                                                         fillercard)
                                                            print("wrench ", ne_holder_north, ne_north_value)
                                                            if len(ne_holder_north) <= 2:
                                                                break

                                                            else:
                                                                ne_holder_east = cornercard(ne_north_value, centercard,
                                                                                        north_candidate,
                                                                                        west_candidate, south_candidate,
                                                                                        east_candidate, nw_candidate,
                                                                                        sw_candidate, se_candidate,
                                                                                        fillercard)  # cards in northwest from west
                                                            print("screwdriver ", ne_holder_east, ne_east_value)
                                                                #print(ne_holder_north, ne_north_value, ne_holder_east, ne_east_value)
                                                            if len(ne_holder_east) <= 2:
                                                                break
                                                            else:
                                                                print("cent is ", centercard, "southeast is ", se_candidate, "north is ", north_candidate, "east is ", east_candidate, "ne north holdere is ", ne_holder_north, "ne holder east is ", ne_holder_east)
                                                                northeast_holder = corner_compare(ne_holder_north, ne_north_value, ne_holder_east, ne_east_value)
                                                                for ne_candidate in northeast_holder:
                                                                    if ne_candidate == fillercard:
                                                                        break
                                                                    else:

                                                                        print(Fore.YELLOW)
                                                                        print("NE is ", ne_candidate)
                                                                        print("SE is ", se_candidate)

                                                                        print("East is ", east_candidate)
                                                                        print("centercard is ", centercard)
                                                                        print("north is ", north_candidate)
                                                                        print("west is ", west_candidate)
                                                                        print("South is ", south_candidate)
                                                                        print("NW is ", nw_candidate)
                                                                        print("SW is ", sw_candidate)
                                                                        print(Style.RESET_ALL)
                                                                        break





