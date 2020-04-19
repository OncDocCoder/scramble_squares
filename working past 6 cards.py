import colorama
from colorama import Fore, Back, Style
colorama.init()

card= [[-2, 1, 4 , -3 , 'North', 'A'],[ -1 , 2, 3, -4, 'North', 'B'],[ -3,-2, -4, -1, 'North', 'C'],[1, 3, 4, -4, 'North', 'D'] , [ 2, -4, -1, 3, 'North', 'E'],[2, -2, -1, 4, 'North', 'F'], [ -3, 4, -1, 2, 'North', 'G'],[-1, 2, 3, 4, 'North', 'H'],[3, 2, 1, -4, 'North', 'I']]

def totheright(card_to_test, index):
    #this gets the value to the right of the matching card
        card_for_index= card_to_test


        # print("card for index ", card_for_index)
        if index < 3:
            num_cardright = card_for_index[index + 1]
        else:
            num_cardright = card_for_index[index - 3]
        #print("the value facing to the right of the match is ", num_cardright)
        matcher_right= num_cardright * -1

        return (matcher_right)

def totheleft(card_to_test, index):
    #This gets the value to the left of the matching card
    card_for_index = card_to_test


    # print("card for index ", card_for_index)
    if index > 0:
        num_cardleft = card_for_index[index - 1]
    else:
        num_cardleft = card_for_index[index + 3]
    #print("the value facing to the left of the match is ", num_cardleft)
    matcher_left = num_cardleft * -1

    return (matcher_left)

def findnorth(anti_center_north, center_north, centercard) -> object:
    #finds cards for center north
    print(Fore.BLUE)
    # print("center north is ", center_north)
    #print("anti center north is", anti_center_north)

    north_holder = []
    for i in range(len(card)):
        if anti_center_north in card[i]:
                north_holder.append(card[i])
                #index_anticenternorth= card[z].index(anti_center_north)

    if centercard in north_holder:
        y = 1
        north_holder.remove(centercard)
    #print("number of cards in north holder if there is a match is, " , len(north_holder), end='')

    return north_holder #the array of possible center_north cards

def findnorthwest_north(nw_north_value, north_candidate, candidate_c):
    # finds the cards for northwest_north
    #print(Fore.BLUE)
    # print("anticenternorthwestmatcher ", totherightofnorthcenter)
    northwest_holder_north = []
    # print (len(card))
    for i in range(len(card)):
        if nw_north_value in card[i]:
            northwest_holder_north.append(card[i])
    if candidate_c in northwest_holder_north:  # removes centercard from westholder
        northwest_holder_north.remove(candidate_c)
    if north_candidate in northwest_holder_north:  # removes northcard from westholder
        northwest_holder_north.remove(north_candidate)
    nwn_counter = len(northwest_holder_north)
    #print("northwest_holder north is" , northwest_holder_north)
    return northwest_holder_north, nwn_counter  # the array of possible northcenter_west cards

def findnorthwest_west(nw_west_value, north_candidate, candidate_c, west_candidate):
    # finds the cards for northwest_north
    print(Fore.CYAN)
    # print("anticenternorthwestmatcherwest ", totheleftofwestcenter)
    northwest_holder_west = []
    # print (len(card))
    for i in range(len(card)):
        if nw_west_value in card[i]:
            northwest_holder_west.append(card[i])
    if candidate_c in northwest_holder_west:  # removes centercard from westholder
        northwest_holder_west.remove(candidate_c)
    if west_candidate in northwest_holder_west:  # removes westcard from westholder
        northwest_holder_west.remove(west_candidate)
    if north_candidate in northwest_holder_west:
        northwest_holder_west.remove(north_candidate)
    print("northwest holder west is ", northwest_holder_west)
    return northwest_holder_west  # the array of possible northcenter_west cards

def findsouthwest_west(card, sw_west_value, candidate_c, north_candidate, west_candidate, nw_candidate, south_candidate):
    # finds the cards for southwest_west

    southwest_holder_west = []
    for i in range(len(card)):
        if sw_west_value in card[i]:
            southwest_holder_west.append(card[i])
    if candidate_c in southwest_holder_south:  # removes centercard from westholder
        southwest_holder_west.remove(candidate_c)
    if west_candidate in southwest_holder_south:  # removes westcard from westholder
        southwest_holder_west.remove(west_candidate)
    if north_candidate in southwest_holder_south:
        southwest_holder_west.remove(north_candidate)
    if south_candidate in southwest_holder_south:
        southwest_holder_west.remove(south_candidate)
    if nw_candidate in southwest_holder_south:
        southwest_holder_west.remove(nw_candidate)
    sw_holder_west_counter = len(southwest_holder_west)
    return southwest_holder_west, sw_holder_south_counter  # southwest_west cards from south

def findsouthwest_south(card, sw_south_value, candidate_c, north_candidate, west_candidate, nw_candidate, south_candidate):
    # finds the cards for southwest_south
    print(Fore.CYAN)
    # print("anticentersouthwestmatchersouth ", totheleftofsouthcenter)
    southwest_holder_south = []
    for i in range(len(card)):
        if sw_south_value in card[i]:
            southwest_holder_south.append(card[i])
    if candidate_c in southwest_holder_south:  # removes centercard from westholder
        southwest_holder_south.remove(candidate_c)
    if west_candidate in southwest_holder_south:  # removes westcard from westholder
        southwest_holder_south.remove(west_candidate)
    if north_candidate in southwest_holder_south:
        southwest_holder_south.remove(north_candidate)
    if south_candidate in southwest_holder_south:
        southwest_holder_south.remove(south_candidate)
    if nw_candidate in southwest_holder_south:
        southwest_holder_south.remove(nw_candidate)
    sw_holder_south_counter = len(southwest_holder_south)
    return southwest_holder_south, sw_holder_south_counter #southwest_west cards from south

def findsoutheast_east(card, se_east_value, candidate_c, north_candidate, west_candidate, nw_candidate, south_candidate, sw_candidate, east_candidate):
    # finds the cards for southeast_east
    southeast_holder_east = []
    for i in range(len(card)):
        if se_east_value in card[i]:
            southeast_holder_east.append(card[i])
    if candidate_c in southeast_holder_east:  # removes centercard from westholder
        southeast_holder_east.remove(candidate_c)
    if west_candidate in southeast_holder_east:  # removes westcard from westholder
        southeast_holder_east.remove(west_candidate)
    if north_candidate in southeast_holder_east:
        southeast_holder_east.remove(north_candidate)
    if south_candidate in southeast_holder_east:
        southeast_holder_east.remove(south_candidate)
    if nw_candidate in southeast_holder_east:
        southeast_holder_east.remove(nw_candidate)
    if east_candidate in southeast_holder_east:
        southeast_holder_east.remove((east_candidate))
    if sw_candidate in southeast_holder_east:
        southeast_holder_east.remove(sw_candidate)
    se_holder_east_counter = len(southeast_holder_east)
    return southeast_holder_east, se_holder_east_counter  # southeast_east cards from east

def findsoutheast_south(card, se_south_value, candidate_c, north_candidate, west_candidate, nw_candidate, south_candidate, sw_candidate, east_candidate):
    # finds the cards for southeast_east
    southeast_holder_south = []
    for i in range(len(card)):
        if se_south_value in card[i]:
            southeast_holder_south.append(card[i])
    if candidate_c in southeast_holder_south:  # removes centercard from westholder
        southeast_holder_south.remove(candidate_c)
    if west_candidate in southeast_holder_south:  # removes westcard from westholder
        southeast_holder_south.remove(west_candidate)
    if north_candidate in southeast_holder_south:
        southeast_holder_south.remove(north_candidate)
    if south_candidate in southeast_holder_south:
        southeast_holder_south.remove(south_candidate)
    if nw_candidate in southeast_holder_south:
        southeast_holder_south.remove(nw_candidate)
    if east_candidate in southeast_holder_south:
        southeast_holder_south.remove((east_candidate))
    if sw_candidate in southeast_holder_south:
        southeast_holder_south.remove((sw_candidate))
    se_holder_south_counter = len(southeast_holder_south)
    print("centercard is ", candidate_c, ". north is ", north_candidate, ".  nw is", nw_candidate, ".  west is ", west_candidate, ". sw is ", sw_candidate, ". South is ", south_candidate)
    return southeast_holder_south, se_holder_south_counter  # southeast_south cards from east

def findwest(anti_center_west, candidate_c, north_candidate, card):
    # finds cards for center_west
    print(Fore.BLUE)
    # print("center west is ", center_west)
    #print("anti center west is", anti_center_west)

    #count_of_remaining_cards = len(cards_left_to_check)
    west_holder = []
    # print (len(card))
    for i in range(len(card)):
        # print(i)
        if anti_center_west in card[i]:
            west_holder.append(card[i])
    if candidate_c in west_holder: #removes centercard from westholder
        west_holder.remove(candidate_c)
    if north_candidate in west_holder: #removes northcard from westholder
        west_holder.remove(north_candidate)

    #print("Westholder is: ", west_holder)

    return west_holder #the array of possible center_west cards

def findeast(anti_center_east, candidate_c, north_candidate, west_candidate,nw_candidate, south_candidate, sw_candidate,card):
    # finds cards for center_east
    print(Fore.BLUE)
    east_holder = []
    print("candidate c is ", candidate_c[5])
    print("west is ", west_candidate[5] )
    print("north is ", north_candidate[5])
    print("South is ", south_candidate[5])
    print("northwest is ", nw_candidate[5])
    print("southwest is ", sw_candidate[5])
    for i in range(len(card)):
        if anti_center_east in card[i]:
            east_holder.append(card[i])
    if candidate_c in east_holder:  # removes centercard from westholder
        east_holder.remove(candidate_c)
    if west_candidate in east_holder:  # removes westcard from westholder
        east_holder.remove(west_candidate)
    if north_candidate in east_holder:
        east_holder.remove(north_candidate)
    if south_candidate in east_holder:
        east_holder.remove(south_candidate)
    if nw_candidate in east_holder:
        east_holder.remove(nw_candidate)
    if sw_candidate in east_holder:
        east_holder.remove(sw_candidate)
    east_holder_counter = len(east_holder)
    print(Fore.LIGHTRED_EX)
    print("East holder is ", east_holder)
    return east_holder, east_holder_counter #the array of possible center_east cards

def findsouth(anti_center_south, candidate_c, north_candidate, west_candidate, nw_candidate, card):
    # finds cards for center_south
    print(Fore.BLUE)
    z = 0
    south_holder = []
    for i in range(len(card)):
        if anti_center_south in card[i]:
            south_holder.append(card[i])
    if candidate_c in south_holder:
        south_holder.remove(candidate_c)
    if north_candidate in south_holder:
        south_holder.remove(north_candidate)
    if west_candidate in south_holder:
        south_holder.remove(west_candidate)
    if nw_candidate in south_holder:
        south_holder.remove(nw_candidate)
    south_count = len(south_holder)
    return south_holder, south_count #the array of possible center_south cards

def corner_compare(side_1, side_1_value, side_2, side_2_value): #need north and west or west and south or south and east or east and north
    result = []
    preresult = []
    #side1 is B side of the corner, side2 is A side of the corner. For NW, A side faces N. For SW, A side faces W, For SE, A side faces S. For NE, A side faces E.
    #print("corner compare" , side_1, "@", side_1_value, '@', side_2, '@', side_2_value)
    a = len(side_2)
    #print("side 2 value is ", side_2_value)
    b = 0
    #print ("length of side 2 is ", a)
    while b < a:
        if side_1_value in side_2[b]:
            preresult.append(side_2[b])
            b += 1
        else:
            b += 1
    #print("preresult is ", preresult)
    c = len(preresult)
    #print("length of preresult is ", c)
    d = 0
    while d < c: #need to find out if values are next to each other
        #is the index of element2  one greater than element 1 unless index of element 2 is
        #3 at which is the index of element2 equal to zero
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
    print (" possible corner squares are",  result)
    corner_counter = len(result)
    return result, corner_counter

def findnortheast_east(card, ne_east_value, candidate_c, north_candidate, west_candidate, nw_candidate, south_candidate, sw_candidate, east_candidate):
    # finds the cards for northeast_east
    northeast_holder_east = []
    for i in range(len(card)):
        if ne_east_value in card[i]:
            northeast_holder_east.append(card[i])
    if candidate_c in northeast_holder_east:  # removes centercard from westholder
        northeast_holder_east.remove(candidate_c)
    if west_candidate in northeast_holder_east:  # removes westcard from westholder
        northeast_holder_east.remove(west_candidate)
    if north_candidate in northeast_holder_east:
        northeast_holder_east.remove(north_candidate)
    if south_candidate in northeast_holder_east:
        northeast_holder_east.remove(south_candidate)
    if nw_candidate in northeast_holder_east:
        northeast_holder_east.remove(nw_candidate)
    if east_candidate in northeast_holder_east:
        northeast_holder_east.remove((east_candidate))
    if sw_candidate in northeast_holder_east:
        northeast_holder_east.remove((sw_candidate))
    if se_candidate in northeast_holder_east:
        northeast_holder_east.remove((se_candidate))
    ne_holder_east_counter = len(northeast_holder_east)
    return northeast_holder_east, ne_holder_east_counter  # northeast_east cards from east

def findnortheast_north(card, ne_north_value, candidate_c, north_candidate, west_candidate, nw_candidate, south_candidate, sw_candidate, east_candidate):
    # finds the cards for southeast_east
    northeast_holder_north = []
    for i in range(len(card)):
        if ne_north_value in card[i]:
            northeast_holder_north.append(card[i])
    if candidate_c in northeast_holder_north:  # removes centercard from westholder
        northeast_holder_north.remove(candidate_c)
    if west_candidate in northeast_holder_north:  # removes westcard from westholder
        northeast_holder_north.remove(west_candidate)
    if north_candidate in northeast_holder_north:
        northeast_holder_north.remove(north_candidate)
    if south_candidate in northeast_holder_north:
        northeast_holder_east.remove(south_candidate)
    if nw_candidate in northeast_holder_north:
        northeast_holder_north.remove(nw_candidate)
    if east_candidate in northeast_holder_north:
        northeast_holder_north.remove((east_candidate))
    if sw_candidate in northeast_holder_north:
        northeast_holder_north.remove((sw_candidate))
    if se_candidate in northeast_holder_north:
        northeast_holder_north.remove((se_candidate))
    ne_holder_north_counter = len(northeast_holder_north)
    return northeast_holder_north, ne_holder_north_counter  # northeast_north cards from north

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

centercard = 0
#puzzle = True
#while puzzle == True:
for centercard  in range (0, 9):
    print(Fore.YELLOW)
    print("Card in center ", card[centercard][5], end='')
    print(Style.RESET_ALL)
    candidate_c = card[centercard]
    print("candidate c is, ",  candidate_c)

    center_north, anti_center_north, center_east, anti_center_east, center_south, anti_center_south, center_west, anti_center_west = cards_for_center(
            candidate_c)
    north_holder = findnorth(anti_center_north, center_north, candidate_c)

    north_holder_counter = 0
    if len(north_holder) == 0:
        #print(Fore.RED)
        #print("there are no cards for north, move on.")
        #print(Style.RESET_ALL)
        break

    else:
        for north_holder_counter in range(0, len(north_holder)):
            north_candidate = north_holder[north_holder_counter]
            print(Fore.MAGENTA)
            print("Card to north is ", north_candidate[5], end='')
            print(Style.RESET_ALL)
            index_anticenternorth = north_holder[north_holder_counter].index(anti_center_north)
            nw_north_value = totheright(north_candidate, index_anticenternorth)
            ne_north_value = totheleft(north_holder[north_holder_counter], index_anticenternorth)
            northwest_holder_north, corner_counter = findnorthwest_north(nw_north_value, north_candidate,
                                                                         candidate_c)

            ####find west
            west_holder = findwest(anti_center_west, candidate_c, north_candidate, card)
            west_holder_counter = 0
            for west_holder_counter in range (0, len(west_holder)):
                index_anticenterwest = west_holder[west_holder_counter].index(anti_center_west)
                west_candidate = west_holder[west_holder_counter]
                print(Fore.BLUE)
                print("card to west is, ", west_candidate[5])
                print(Style.RESET_ALL)
                nw_west_value = totheleft(west_candidate, index_anticenterwest)
                sw_west_value = totheright(west_candidate, index_anticenterwest)
                northwest_holder_west = findnorthwest_west(nw_west_value, north_candidate, centercard,
                                                           west_candidate)  # cards in northwest from west
                northwest_holder, nw_counter = corner_compare(northwest_holder_west, nw_west_value,
                                                              northwest_holder_north, nw_north_value)
                if nw_counter == 0:
                    #print(Fore.RED)
                    #print("no values are possible for nw, move on")
                    #print(Style.RESET_ALL)
                    break

                else:
                    nw_holder_counter = 0
                    for nw_holder_counter in range (0, len(northwest_holder)):
                        nw_candidate = northwest_holder[nw_holder_counter]
                        print(Fore.LIGHTCYAN_EX)
                        print("northwest candidate is ", northwest_holder[nw_holder_counter][5])
                        print(Style.RESET_ALL)
                        #####find south
                        south_holder, south_count = findsouth(anti_center_south,candidate_c, north_candidate, west_candidate, nw_candidate, card)
                        print(Fore.LIGHTBLUE_EX)
                        print("South holder is ", south_holder)
                        print(Style.RESET_ALL)

                        if south_count == 0:
                            break
                        else:
                            southholder_counter = 0
                            print(Fore.BLUE)
                            print(south_count)
                            print(Style.RESET_ALL)
                            for southholder_counter in range(0, len(south_holder)):

                                south_candidate = south_holder[southholder_counter]
                                print(Fore.YELLOW)
                                print("south candidate is ", south_holder[southholder_counter][5])
                                print(Style.RESET_ALL)
                                index_anticentersouth = south_candidate.index(anti_center_south)
                                sw_south_value = totheleft(south_holder[southholder_counter], index_anticentersouth)
                                se_south_value = totheright(south_holder[southholder_counter],
                                                            index_anticentersouth)
                                print("southeast south value is ", se_south_value)
                                southwest_holder_south, sw_holder_south_counter = findsouthwest_south(card,
                                                                                                      sw_south_value,
                                                                                                      candidate_c,
                                                                                                      north_candidate,
                                                                                                      west_candidate,
                                                                                                      nw_candidate,
                                                                                                      south_candidate)
                                southwest_holder_west, sw_holder_west_counter = findsouthwest_west(card,
                                                                                                   sw_west_value,
                                                                                                   candidate_c,
                                                                                                   north_candidate,
                                                                                                   west_candidate,
                                                                                                   nw_candidate,
                                                                                                   south_candidate)
                                if sw_holder_west_counter == 0 or sw_holder_south_counter == 0:
                                    break
                                else:
                                    sw_holder, sw_counter = corner_compare(southwest_holder_south, sw_south_value, southwest_holder_west, sw_west_value)
                                    if sw_counter == 0:
                                        print(Fore.RED)
                                        #print("no values are possible for sw, move on")
                                        print(Style.RESET_ALL)
                                        #southholder_counter +=1

                                    else:
                                        #print("there are", sw_counter,  " southwest possibles ")
                                        #getting east
                                        swholder_counter = 0
                                        for swholder_counter in range(0,len(sw_holder)):
                                                sw_candidate = sw_holder[swholder_counter]
                                                ###Getting EAST
                                                east_holder, east_count = findeast(anti_center_east, candidate_c,north_candidate, west_candidate,nw_candidate, south_candidate, sw_candidate, card)
                                                if east_count == 0:
                                                    print(Fore.RED)
                                                    print("no cards are available for east, move on")
                                                    print(Style.RESET_ALL)
                                                    break


                                                else:
                                                    #print("cards available for east are, ", east_holder)
                                                    ###CYCLING THROUGH EAST
                                                    east_holdercounter = 0
                                                    for east_holdercounter in range(0, len(east_holder)):
                                                        #print(east_count)
                                                        east_candidate = east_holder[east_holdercounter]
                                                        #print("east candidate is ", east_holder[east_holdercounter][5])
                                                        index_anticentereast = east_candidate.index(
                                                            anti_center_east)
                                                        se_east_value = totheleft(east_holder[east_holdercounter],
                                                                                  index_anticentereast)
                                                        ne_east_value = totheleft(east_holder[east_holdercounter], index_anticentereast)
                                                        print("southeast east value is ", se_east_value)
                                                        se_holder_east, se_holder_east_counter = findsoutheast_east(
                                                            card, se_east_value, candidate_c, north_candidate,
                                                            west_candidate, nw_candidate, south_candidate, sw_candidate, east_candidate)
                                                        se_holder_south, se_holder_south_counter = findsoutheast_south(
                                                            card, se_south_value, candidate_c, north_candidate,
                                                            west_candidate, nw_candidate, south_candidate, sw_candidate, east_candidate)
                                                        if se_holder_east_counter == 0 or se_holder_south_counter == 0:
                                                            break
                                                        else:

                                                            se_holder, se_counter = corner_compare(se_holder_east, se_east_value,
                                                                                                   se_holder_south, se_south_value)
                                                            if se_counter == 0:
                                                                break
                                                            else:
                                                                ne_holdercounter = 0
                                                                east_candidate = east_holder[ne_holdercounter]
                                                                for ne_holdercounter in range(0, len(se_holder)):
                                                                    ne_holder_east, northeast_e_holder_count = findnortheast_east(card, ne_east_value, candidate_c, north_candidate, west_candidate, nw_candidate, south_candidate, sw_candidate, east_candidate)
                                                                    ne_holder_north, northeast_n_holder_count = findnortheast_north(card, ne_north_value, candidate_c, north_candidate, west_candidate, nw_candidate, south_candidate, sw_candidate, east_candidate)
                                                                    if northeast_n_holder_count==0 or northeast_e_holder_count==0:
                                                                        break
                                                                    else:
                                                                        ne_holder = corner_compare(ne_holdernorth, ne_north_value, ne_holder_east, ne_east_value)
                                                                        if len(ne_holder) == 0:
                                                                            break
                                                                        else:
                                                                            ne_candidate = ne_holder[0]
                                                                            print("candidate c is ", candidate_c[5])
                                                                            print("west is ", west_candidate[5] )
                                                                            print("north is ", north_candidate[5])
                                                                            print("South is ", south_candidate[5])
                                                                            print("northwest is ", nw_candidate[5])
                                                                            print("southwest is ", sw_candidate[5])
                                                                            print("southeast is ", s_candidate[5])
                                                                            print("southeast is ", east_candidate[5])
                                                                            print("northeast is ", ne_candidate[5] )

                                                            break


     #   puzzle == False'''