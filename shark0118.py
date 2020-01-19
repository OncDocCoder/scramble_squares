

import coloramapython -m pip install --upgrade pip
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
        print("card for index ", card_for_index)
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
    print("card for index ", card_for_index)
    if index > 0:
        num_cardleft = card_for_index[index - 1]
    else:
        num_cardleft = card_for_index[index + 3]
    #print("the value facing to the left of the match is ", num_cardleft)
    matcher_left = num_cardleft * -1
    print(Style.RESET_ALL)
    return (num_cardleft, matcher_left)

def findnorth(anti_center_north, center_north) -> object:

    print(Fore.BLUE)
    print("center north is ", center_north)
    print("anti center north is", anti_center_north)
    z = 0
    north_holder = []
    while z < 9:
        if anti_center_north in card[z]:
                #index_anticenternorth= card[z].index(anti_center_north)
                north_holder.append(card[z])
                z += 1
        else:
            z += 1
    return north_holder
def findnorthwest(totherightofnorthcenter):

    print(Fore.BLUE)
    print("anticenternorthwestmatcher ", totherightofnorthcenter)
    q = int(totherightofnorthcenter)
    l = 0
    northwest_holder_a = []
    while l < 9:
        if q in card[l]:
                #index_anticenternorth= card[z].index(anti_center_north)
                northwest_holder_a.append(card[l])
                l += 1
        else:
            l += 1
    return northwest_holder_a

def findwest(anti_center_north, center_north):

    print(Fore.BLUE)
    print("center west is ", center_west)
    print("anti center west is", anti_center_west)
    z = 0
    west_holder = []
    while z < 9:
        if anti_center_west in card[z]:
                west_holder.append(card[z])
                z += 1
        else:
            z += 1
    return west_holder

def findeast(anti_center_east, center_east):

    print(Fore.BLUE)
    print("center east is ", center_east)
    print("anti center east is", anti_center_east)
    z = 0
    east_holder = []
    while z < 9:
        if anti_center_east in card[z]:
                east_holder.append(card[z])
                z += 1
        else:
            z += 1
    return east_holder

def findsouth(anti_center_south, center_south):

    print(Fore.BLUE)
    print("center south is ", center_south)
    print("anti center south is", anti_center_south)
    z = 0
    south_holder = []
    while z < 9:
        if anti_center_south in card[z]:
            south_holder.append(card[z])
            z += 1
        else:
            z += 1
    return south_holder


#main program
centercard = 0
while centercard < 9:
    print(Fore.GREEN)
    print("the candidate card for center is ", card[centercard])
    print(Style.RESET_ALL)
    center_north = card[centercard][0]
    center_west = card[centercard][3]
    center_south = card[centercard][2]
    center_east = card[centercard][1]
    anti_center_north = center_north * -1
    anti_center_east = center_east * -1
    anti_center_south = center_south * -1
    anti_center_west = center_west * -1
    north_holder = findnorth(anti_center_north, center_north)
    west_holder = findwest(anti_center_west, center_west)
    east_holder = findeast(anti_center_east, center_east)
    south_holder = findsouth(anti_center_south, center_south)

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
            if b < west_count:
                print(Fore.LIGHTCYAN_EX)
                print("west count", west_count)
            # print("west possibles are ", west_holder)
                if west_holder[b] == card[centercard]:
                    g = b+1
                    print("west candidate today", west_holder[g])
                    west_candidate = west_holder[g]
                    b += 2

                    print(Style.RESET_ALL)
                    index_anticenterwest = west_holder[b+1].index(anti_center_west)
                else:
                    g = b
                    print("west candidate", west_holder[g])
                    print(Style.RESET_ALL)
                    west_candidate = west_holder[g]
                    index_anticenterwest = west_holder[g].index(anti_center_west)
                    b += 1

                test_w = [west_holder[g][0], west_holder[g][1], west_holder[g][2], west_holder[g][3], west_holder[g][4], west_holder[g][5]]
                print(g, west_holder[g][5])

             # print("the index of anticenterwest is ", index_anticenterwest)
                leftw, antileftw = totheleft(test_w, index_anticenterwest)
                print(Fore.LIGHTCYAN_EX)
                print("The index of anticenterwest is ", index_anticenterwest, "leftwest is, ", leftw, "and antileftwest is ", antileftw)
                print(Style.RESET_ALL)
            print(Fore.LIGHTYELLOW_EX)
            print("count is ", n+1)
            print(Style.RESET_ALL)
            print("northholder is ", north_holder[0])
            test_n = [north_holder[n][0],north_holder[n][1],north_holder[n][2], north_holder[n][3], north_holder[n][4], north_holder[n][5]]
            print("test_n is ", test_n)
            index_anticenternorth= north_holder[n].index(anti_center_north)
            # print("the index of anticenternorth is ", index_anticenternorth)
            right, antiright = totheright(test_n, index_anticenternorth)
            print(Fore.CYAN)
            print("index is ", index_anticenternorth, "Num to right is ", right, "antinum to right is", antiright)
            northwest_holder_a = findnorthwest(antiright)
            #need to remove centernorth and center
            print("prepossible cards for northwest are", northwest_holder_a)
            if card[centercard] in northwest_holder_a:
                try:
                    northwest_holder_a.remove(card[centercard])
                except:
                    pass

            if north_holder[0] in northwest_holder_a:
                try:
                    northwest_holder_a.remove(north_holder[0])
                except:
                    pass

            northwest_holder = northwest_holder_a
            print("possible cards for northwest are ", northwest_holder)
            print(Fore.LIGHTBLACK_EX)
            left, antileft = totheleft(test_n, index_anticenternorth)
            print("num to left is ", left, "antinum to left is ", antileft)
            n += 1
        print(Style.RESET_ALL)
        print(" ")

    centercard += 1

"I am adding a string"