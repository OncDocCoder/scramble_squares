

import colorama
from colorama import Fore, Back, Style
colorama.init()

card= [[-2, 1, 4 , -4 , 'North', 'A'],[ -3 , 1, -2, 4, 'North', 'B'],[ -1,-2, -3, -4, 'North', 'C'],
       [-2, 4, 3, -1, 'North', 'D'] , [ 3, 1, -2, 4, 'North', 'E'],[-3, -4, 2, 1, 'North', 'F'],
       [ 2, -1, 3, 4, 'North', 'G'],[-3, 4, -1, -2, 'North', 'H'],[2, 3, 1, -1, 'North', 'I']]


card2= [[-2, 1, 4 , -4 , 'North', 'A'],[ -3 , 1, -2, 4, 'North', 'B'],[ -1,-2, -3, -4, 'North', 'C'],
       [-2, 4, 3, -1, 'North', 'D'] , [ 3, 1, -2, 4, 'North', 'E'],[-3, -4, 2, 1, 'North', 'F'],
       [ 2, -1, 3, 4, 'North', 'G'],[-3, 4, -1, -2, 'North', 'H'],[2, 3, 1, -1, 'North', 'I']]


cardtuple = ([-2, 1, 4 , -4 , 'North', 'A'],[ -3 , 1, -2, 4, 'North', 'B'],[ -1,-2, -3, -4, 'North', 'C'],
       [-2, 4, 3, -1, 'North', 'D'] , [ 3, 1, -2, 4, 'North', 'E'],[-3, -4, 2, 1, 'North', 'F'],
       [ 2, -1, 3, 4, 'North', 'G'],[-3, 4, -1, -2, 'North', 'H'],[2, 3, 1, -1, 'North', 'I'])

def totheright(card_to_test, index):
    #this gets the value to the right of the matching card
        card_for_index= card_to_test

        print(Fore.CYAN)
        # print("card for index ", card_for_index)
        if index < 3:
            num_cardright = card_for_index[index + 1]
        else:
            num_cardright = card_for_index[index - 3]
        #print("the value facing to the right of the match is ", num_cardright)
        matcher_right= num_cardright * -1
        print(Style.RESET_ALL)
        return (num_cardright, matcher_right)


def totheleft(card_to_test, index):
    #This gets the value to the left of the matching card
    card_for_index = card_to_test

    print(Fore.MAGENTA)
    # print("card for index ", card_for_index)
    if index > 0:
        num_cardleft = card_for_index[index - 1]
    else:
        num_cardleft = card_for_index[index + 3]
    #print("the value facing to the left of the match is ", num_cardleft)
    matcher_left = num_cardleft * -1
    print(Style.RESET_ALL)
    return (num_cardleft, matcher_left)

def findnorth(anti_center_north, center_north, centercard) -> object:
    #finds cards for center north
    print(Fore.BLUE)
    # print("center north is ", center_north)
    #print("anti center north is", anti_center_north)
    z = 0
    north_holder = []
    while z < 8:
        if anti_center_north in card[z]:
                #index_anticenternorth= card[z].index(anti_center_north)
                north_holder.append(card[z])
                z += 1
        else:
            z += 1
    # print("number of cards in north holder if no match is, ", len(north_holder))
    if centercard in north_holder:
        north_holder.delete(centercard)
    # print("number of cards in north holder if there is a match is, " , len(north_holder))

    return north_holder #the array of possible center_north cards


def findnorthwest_north(totherightofnorthcenter):
    # finds the cards for northwest_north
    print(Fore.BLUE)
    # print("anticenternorthwestmatcher ", totherightofnorthcenter)
    q = int(totherightofnorthcenter)
    l = 0
    northwest_holder_north = []
    while l < 8:
        if q in card[l]:
                #index_anticenternorth= card[z].index(anti_center_north)
                northwest_holder_north.append(card[l])
                l += 1
        else:
            l += 1
    return northwest_holder_north #northwest_north cards

def findnorthwest_west(totheleftofwestcenter, cards_left_to_check):
    # finds the cards for northwest_north
    print(Fore.CYAN)
    # print("anticenternorthwestmatcherwest ", totheleftofwestcenter)
    q = int(totheleftofwestcenter)
    # print("the number to the leftofwestcenter is, ", q)
    counter = len(cards_left_to_check)
    # print("cards left to check are", cards_left_to_check)
    northwest_holder_west = []
    # print("num cards left to check is ", counter)
    n = 0
    while n < counter:
        if q in cards_left_to_check[n]:
                # index_anticenterwest= card[z].index(anti_center_west)
                northwest_holder_west.append(card[n])
                n += 1
        else:
            n += 1
    if len(northwest_holder_west) == 0:
        print("no cards match for northwest_holder_west")
    # print("northwestholderwest is", northwest_holder_west)
    return northwest_holder_west #northwest_west cards

def findsouthwest_west(totherightofwestcenter):
    # finds the cards for southwest_west
    print(Fore.CYAN)
    # print("anticentersouthwestmatcherwest ", totherightofwestcenter)
    q = int(totherightofwestcenter)
    l = 0
    southwest_holder_west = []
    while l < 9:
        if q in card[l]:
                #index_anticenterwest= card[z].index(anti_center_west)
                southwest_holder_west.append(card[l])
                l += 1
        else:
            l += 1
    return southwest_holder_west #southwest_west cards

def findsouthwest_south(totheleftofsouthcenter):
    # finds the cards for southwest_south
    print(Fore.CYAN)
    # print("anticentersouthwestmatchersouth ", totheleftofsouthcenter)
    q = int(totheleftofsouthcenter)
    l = 0
    southwest_holder_south = []
    while l < 8:
        if q in card[l]:
                #index_anticentersouth= card[z].index(anti_center_south)
                southwest_holder_south.append(card[l])
                l += 1
        else:
            l += 1
    return southwest_holder_south #southwest_west cards from south


def findwest(anti_center_west, cards_left_to_check):
    # finds cards for center_west
    print(Fore.BLUE)
    # print("center west is ", center_west)
    #print("anti center west is", anti_center_west)
    z = 0
    count_of_remaining_cards = len(cards_left_to_check)
    west_holder = []
    while z < count_of_remaining_cards:
        if anti_center_west in card[z]:
                west_holder.append(card[z])
                z += 1
        else:
            z += 1
    print("Westholder is: ", west_holder)

    return west_holder #the array of possible center_west cards

def findeast(anti_center_east, center_east, centercard):
    # finds cards for center_east
    print(Fore.BLUE)
    z = 0
    east_holder = []
    while z < 8:
        if anti_center_east in card[z]:
                east_holder.append(card[z])
                z += 1
        else:
            z += 1
    if centercard in east_holder:
        east_holder.delete(centercard)
    return east_holder #the array of possible center_east cards

def findsouth(anti_center_south, center_south,centercard):
    # finds cards for center_south
    print(Fore.BLUE)
    z = 0
    south_holder = []
    while z < 8:
        if anti_center_south in card[z]:
            south_holder.append(card[z])
            z += 1
        else:
            z += 1
    if centercard in south_holder:
        south_holder.delete(centercard)

    return south_holder #the array of possible center_south cards

def corner_compare(side_1, side_2): #need north and west or west and south or south and east or east and north
    result = []
    for element in side_1:
        if element in side_2:
            result.append(element)
    return result


def cards_in_play(eliminator):
    # print("the center card is ", eliminator)
    card.remove(eliminator)
    cards_left_to_check = card
    #print(card)
    return cards_left_to_check
    print(Fore.LIGHTCYAN_EX)

def cards_for_center(candidate_c):
    center_north = card[centercard][0]
    center_west = card[centercard][3]
    center_south = card[centercard][2]
    center_east = card[centercard][1]
    anti_center_north = center_north * -1
    anti_center_east = center_east * -1
    anti_center_south = center_south * -1
    anti_center_west = center_west * -1
    return (center_north, anti_center_north, center_east, anti_center_east, center_south, anti_center_south, center_west, anti_center_west)


'''if b < west_count:
                                        index_anticenterwest = west_holder[g].index(anti_center_west)
                                    # print("west count", west_count)
                                # print("west possibles are ", west_holder)
                                    if west_holder[b] == card[centercard]:
                                        g = b+1
                                        print("west candidate number", g, "of", west_count, "is ", west_holder[g])
                                        west_candidate = west_holder[g]
                                        b += 2
                                        index_anticenterwest = west_holder[b+1].index(anti_center_west)

                                        print(Style.RESET_ALL)
                                    else:
                                        g = b
                                        print("west candidate number", g, "of ", west_count, "is ", west_holder[g])
                                        print(Style.RESET_ALL)
                                        west_candidate = west_holder[g]
                                        b += 1

                                    west_card_possible = [west_holder[g][0], west_holder[g][1], west_holder[g][2], west_holder[g][3], west_holder[g][4], west_holder[g][5]]
                                   # print(g, west_holder[g][5])
                                    # print(" wcp is ", west_card_possible)'''

3
#main program
centercard = 0
puzzle = True
while puzzle == True:
    for card_center in card:
        print(Fore.LIGHTBLUE_EX)
        print("Card in center ", card[centercard][5])
        print(Style.RESET_ALL)
        candidate_c = card[centercard]
        cards_left_to_check = cards_in_play(candidate_c)
        # print("the cards left to check are: ", cards_left_to_check)
        center_north, anti_center_north, center_east, anti_center_east, center_south, anti_center_south, center_west, anti_center_west = cards_for_center(candidate_c)
        # print(anti_center_north, center_north)
        north_holder = findnorth(anti_center_north, center_north, candidate_c)
        north_holder_counter = 0
        while north_holder_counter < len(north_holder):
            north_candidate = north_holder[north_holder_counter]
            cards_left_to_check = cards_in_play(north_candidate)
            print("Cards left to check after taking up a card for north are: ", cards_left_to_check)
            west_holder = findwest(anti_center_west, cards_left_to_check)
            west_holder_counter = 0
            while west_holder_counter < len(west_holder):
                index_anticenterwest = west_holder[west_holder_counter].index(anti_center_west)
                west_card_possible = west_holder[west_holder_counter]
                west_northwest_number, anti_northwest_number = totheleft(west_card_possible, index_anticenterwest)
                northwest_holder_west = findnorthwest_west(anti_northwest_number, cards_left_to_check) #cards in northwest from west
                west_holder_counter += 1
            north_holder_counter += 1
            #test_n = [north_holder[n][0],north_holder[n][1],north_holder[n][2], north_holder[n][3], north_holder[n][4], north_holder[n][5]]
            # print("test_n is ", test_n)
            index_anticenternorth= north_holder[north_holder_counter].index(anti_center_north)
            right, nw_north = totheright(north_holder[north_holder_counter], index_anticenternorth)
            northwest_holder_north = findnorthwest_north(nw_north)
       # east_holder = findeast(anti_center_east, center_east, candidate_c)
        #south_holder = findsouth(anti_center_south, center_south,candidate_c)

        '''print(Fore.RED)
        print("cards available for north are ", north_holder)
        # north_count = len(north_holder)
        # print("there are ", north_count, "possible north cards")'''
        '''print(Fore.LIGHTCYAN_EX)
        print("cards available for west are ", west_holder)
        west_count = len(west_holder)
        print("there are ", west_count, "possible west cards")
        print(Fore.MAGENTA)
        print("cards available for east are ", east_holder)
        east_count = len(east_holder)
        print("there are ", east_count, "possible east cards")
        print(Fore.LIGHTBLUE_EX)
        print("cards available for south are ", south_holder)
        south_count = len(south_holder)
        print("there are ", south_count, "possible south cards")
        print(Style.RESET_ALL)'''

        #going for northwest!!!!

        '''for candidate_n in north_holder:
            n = 0
            while n < north_count:
                pass
            b = 0
            print(Fore.RED)
            # print("the candidate card for north is ", north_holder[b])
            print(Style.RESET_ALL)'''



        '''# print("the index of anticenterwest is ", index_anticenterwest)
            # finds matching number to match west card for northwest and ...start of southwest
            print(Fore.LIGHTCYAN_EX)
            # print("The index of anticenterwest is ", i ndex_anticenterwest, "leftwest is, ", west_northwest_number, "and antileftwest is ", anti_northwest_number)
            print(Style.RESET_ALL)
            west_southwest_number, anti_southwest_number = totheright(west_card_possible, index_anticenterwest)
            # print("rightwest is ", west_southwest_number, "and antirigthtwest is ", anti_southwest_number)
            print(Fore.LIGHTYELLOW_EX)
            #print("cards that fit in northwest from west are,", northwest_holder_west)
            # print("count is ", n+1)
            print(Style.RESET_ALL)
            # print("northholderwest is ", north_holderwest[0])
            # print("the index of anticenternorth is ", index_anticenternorth)'''
            # print(Fore.CYAN)
            # print("index is ", index_anticenternorth, "Num to northwest from north_center is ", right, "NW from north_center is", nw_north)
    ''' print("cards that fit in northwest from north are, ", northwest_holder_north)'''

            #               you have northwest_holder_north and northwest_holder_west--are there any cards in common?
    '''print(Fore.LIGHTMAGENTA_EX)
            print("northwest_holder_north is ", northwest_holder_north, " and northwest_holder_west is ", northwest_holder_west)
            print(Style.RESET_ALL)

            #see if any cards in northwest_holder_are possible matches with western candidate
            northwest_holder_almost = corner_compare(northwest_holder_north, northwest_holder_west)
            print(Fore.YELLOW)
            print("northwest holder almost = ", northwest_holder_almost)
            print(Style.RESET_ALL)
            test_s = [south_holder[0][0], south_holder[0][1], south_holder[0][2], south_holder[0][3],
                      south_holder[0][4], south_holder[0][5]]
            print("test_s is ", test_s)
            index_anticentersouth = south_holder[n].index(anti_center_south)
            print("the index of anticentersouth is ", index_anticentersouth)
            right_s, se_southmatcher = totheright(test_s, index_anticentersouth)
            print("the number to the right of anticentersouth matcher is ", right_s, ".", "the matcher to the right of anticentersouth matcher is ", se_southmatcher)
             print("cards that fit in northwest from north are, ", northwest_holder_north)
            left_s, sw_matcher = totheleft(test_s, index_anticentersouth)
            print("the number to the left of anticentersouth matcher is ", left_s, ".",
                  "the matcher to the left of anticentersouth matcher is ", sw_matcher)
            southwest_holder_south = findsouthwest_south(sw_matcher)

            test_w = [west_holder[0][0], west_holder[0][1], west_holder[0][2], west_holder[0][3],
                      west_holder[0][4], west_holder[0][5]]
            print("test_w is ", test_w)
            index_anticenterwest =  west_holder[n].index(anti_center_west)
            print("the index of anticenterwest is ", index_anticenterwest)
            right_w, se_westmatcher = totheright(test_w, index_anticenterwest)
            print("the number to the right of anticenterwest matcher is ", right_w, ".",
                  "the matcher to the right of anticenterwest matcher is ", se_westmatcher)

            #if card[centercard] in northwest_holder_a:
            #   try:
            #      northwest_holder_a.remove(card[centercard])
            # except:
            #    pass'''

            # if north_holder[0] in northwest_holder_a:
            #  try:
            #     northwest_holder_a.remove(north_holder[0])
            # except:
            #   pass

            # northwest_holder = northwest_holder_a
            #print("possible cards for northwest are ", northwest_holder)
            # print(Fore.LIGHTBLACK_EX)







