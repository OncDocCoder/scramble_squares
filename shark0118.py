

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

def findnorth(anti_center_north, center_north, candidate_c) -> object:
    #finds cards for center north
    print(Fore.BLUE)
    # print("center north is ", center_north)
    print("anti center north is", anti_center_north)
    z = 0
    north_holder = []
    while z < 9:
        if anti_center_north in card[z]:
            if card[z] != candidate_c:
                #index_anticenternorth= card[z].index(anti_center_north)
                north_holder.append(card[z])
                z += 1
        else:
            z += 1
    return north_holder #the array of possible center_north cards


def findnorthwest_north(totherightofnorthcenter):
    # finds the cards for northwest_north
    print(Fore.BLUE)
    # print("anticenternorthwestmatcher ", totherightofnorthcenter)
    q = int(totherightofnorthcenter)
    l = 0
    northwest_holder_north = []
    while l < 9:
        if q in card[l]:
                #index_anticenternorth= card[z].index(anti_center_north)
                northwest_holder_north.append(card[l])
                l += 1
        else:
            l += 1
    return northwest_holder_north #northwest_north cards

def findnorthwest_west(totheleftofwestcenter):
    # finds the cards for northwest_north
    print(Fore.CYAN)
    # print("anticenternorthwestmatcherwest ", totheleftofwestcenter)
    q = int(totheleftofwestcenter)
    l = 0
    northwest_holder_west = []
    while l < 9:
        if q in card[l]:
                #index_anticenterwest= card[z].index(anti_center_west)
                northwest_holder_west.append(card[l])
                l += 1
        else:
            l += 1
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
    while l < 9:
        if q in card[l]:
                #index_anticentersouth= card[z].index(anti_center_south)
                southwest_holder_south.append(card[l])
                l += 1
        else:
            l += 1
    return southwest_holder_south #southwest_west cards from south


def findwest(anti_center_north, center_north, candidate_c):
    # finds cards for center_west
    print(Fore.BLUE)
    # print("center west is ", center_west)
    print("anti center west is", anti_center_west)
    z = 0
    west_holder = []
    while z < 9:
        if anti_center_west in card[z]:
            if card[z] != candidate_c:
                west_holder.append(card[z])
                z += 1
        else:
            z += 1
    return west_holder #the array of possible center_west cards

def findeast(anti_center_east, center_east, candidate_c):
    # finds cards for center_east
    print(Fore.BLUE)
    z = 0
    east_holder = []
    while z < 9:
        if card[z] == candidate_c:
            z += 1
        el if anti_center_east in card[z]:
                east_holder.append(card[z])
                z += 1
        else:
            z += 1
    return east_holder #the array of possible center_east cards

def findsouth(anti_center_south, center_south):
    # finds cards for center_south
    print(Fore.BLUE)
    z = 0
    south_holder = []
    while z < 9:
        if anti_center_south in card[z]:
            south_holder.append(card[z])
            z += 1
        else:
            z += 1
    return south_holder #the array of possible center_south cards

def corner_compare(side_1, side_2): #need north and west or west and south or south and east or east and north
    result = []
    for element in side_1:
        if element in side_2:
            result.append(element)
    return result


#main program
centercard = 0
while centercard < 9:
    print(Fore.GREEN)
    print("the candidate card for center is ", card[centercard])
    candidate_c = card[centercard]
    print(Style.RESET_ALL)
    center_north = card[centercard][0]
    center_west = card[centercard][3]
    center_south = card[centercard][2]
    center_east = card[centercard][1]
    anti_center_north = center_north * -1
    anti_center_east = center_east * -1
    anti_center_south = center_south * -1
    anti_center_west = center_west * -1
    north_holder = findnorth(anti_center_north, center_north, candidate_c)
    west_holder = findwest(anti_center_west, center_west, candidate_c)
    east_holder = findeast(anti_center_east, center_east, candidate_c)
    south_holder = findsouth(anti_center_south, center_south, candidate_c)

    print(Fore.RED)
    print("cards available for north are ", north_holder)
    north_count = len(north_holder)
    print("there are ", north_count, "possible north cards")
    print(Fore.LIGHTCYAN_EX)
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
    print(Style.RESET_ALL)

    #going for northwest!!!!

    for candidate in north_holder:
        n = 0
        while n < north_count:
            b = 0
            print(Fore.RED)
            print("the candidate card for north is ", north_holder[b])
            print(Style.RESET_ALL)


            if b < west_count:
                print(Fore.LIGHTCYAN_EX)
                # print("west count", west_count)
            # print("west possibles are ", west_holder)
                if west_holder[b] == card[centercard]:
                    g = b+1
                    print("west candidate number", g, "of", west_count, "is ", west_holder[g])
                    west_candidate = west_holder[g]
                    b += 2

                    print(Style.RESET_ALL)
                    index_anticenterwest = west_holder[b+1].index(anti_center_west)
                else:
                    g = b
                    print("west candidate number", g, "of ", west_count, "is ", west_holder[g])
                    print(Style.RESET_ALL)
                    west_candidate = west_holder[g]
                    index_anticenterwest = west_holder[g].index(anti_center_west)
                    b += 1

                west_card_possible = [west_holder[g][0], west_holder[g][1], west_holder[g][2], west_holder[g][3], west_holder[g][4], west_holder[g][5]]
               # print(g, west_holder[g][5])
                # print(" wcp is ", west_card_possible)

             # print("the index of anticenterwest is ", index_anticenterwest)
                # finds matching number to match west card for northwest and ...start of southwest
                west_northwest_number, anti_northwest_number = totheleft(west_card_possible, index_anticenterwest)
                print(Fore.LIGHTCYAN_EX)
                # print("The index of anticenterwest is ", i ndex_anticenterwest, "leftwest is, ", west_northwest_number, "and antileftwest is ", anti_northwest_number)
                print(Style.RESET_ALL)
                west_southwest_number, anti_southwest_number = totheright(west_card_possible, index_anticenterwest)
                # print("rightwest is ", west_southwest_number, "and antirigthtwest is ", anti_southwest_number)
                print(Fore.LIGHTYELLOW_EX)
                northwest_holder_west = findnorthwest_west(anti_northwest_number) #cards in northwest from west
                #print("cards that fit in northwest from west are,", northwest_holder_west)
            # print("count is ", n+1)
            print(Style.RESET_ALL)
            # print("northholderwest is ", north_holderwest[0])
            test_n = [north_holder[n][0],north_holder[n][1],north_holder[n][2], north_holder[n][3], north_holder[n][4], north_holder[n][5]]
            # print("test_n is ", test_n)
            index_anticenternorth= north_holder[n].index(anti_center_north)
            # print("the index of anticenternorth is ", index_anticenternorth)
            right, nw_north = totheright(test_n, index_anticenternorth)
            print(Fore.CYAN)
            # print("index is ", index_anticenternorth, "Num to northwest from north_center is ", right, "NW from north_center is", nw_north)
            northwest_holder_north = findnorthwest_north(nw_north)
            ''' print("cards that fit in northwest from north are, ", northwest_holder_north)'''

            #               you have northwest_holder_north and northwest_holder_west--are there any cards in common?
            print(Fore.LIGHTMAGENTA_EX)
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
            ''' print("cards that fit in northwest from north are, ", northwest_holder_north)'''
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

            n += 1
        print(Style.RESET_ALL)
        print(" ")

    centercard += 1

