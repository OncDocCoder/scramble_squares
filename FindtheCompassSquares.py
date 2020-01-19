
card= [[-2, 1, 4 , -4 , 'North', 'A'] ,[ -3 , 1, -2, 4, 'North', 'B'] ,[ -1 ,-2, -3, -4, 'North', 'C'],
       [-2, 4, 3, -1, 'North', 'D'] , [ 3, 1, -2, 4, 'North', 'E'] ,[-3, -4, 2, 1, 'North', 'F'],
       [ 2, -1, 3, 4, 'North', 'G'] ,[-3, 4, -1, -2, 'North', 'H'] ,[2, 3, 1, -1, 'North', 'I']]


card2= [[-2, 1, 4 , -4 , 'North', 'A'] ,[ -3 , 1, -2, 4, 'North', 'B'] ,[ -1 ,-2, -3, -4, 'North', 'C'],
        [-2, 4, 3, -1, 'North', 'D'] , [ 3, 1, -2, 4, 'North', 'E'] ,[-3, -4, 2, 1, 'North', 'F'],
        [ 2, -1, 3, 4, 'North', 'G'] ,[-3, 4, -1, -2, 'North', 'H'] ,[2, 3, 1, -1, 'North', 'I']]

'''north_holder = []
for item in range(len(card)):
    matcher_north = (card[item][0]) *-1
    print(matcher_north)
    for y in range(len(card)):
        if matcher_north in card[y]:
            north_holder.append(card[y])
    print(north_holder)

west_holder = []
for item in range(len(card)):
    matcher_west = (card[item][3]) *-1
    print(matcher_west)
    for y in range(len(card)):
        if matcher_west in card[y]:
            west_holder.append(card[y])
    print(west_holder)
'''

north_holder = []
west_holder = []
northwest_holder = []
for item in range(len(card)):
    matcher_north = (card[item][0]) *-1
    print("matcher north",  matcher_north)
    for y in range(len(card)):
        if matcher_north in card[y]:
            index_matchernorth = card[y].index(matcher_north)
            print("index right", index_matchernorth)
            if index_matchernorth < 3:
                matcher_northwest = card[y][index_matchernorth + 1]
            else:
                matcher_northwest = card[y][index_matchernorth - 3]
            northwest_candidate = int(matcher_northwest * -1)
            print("Northwest candidate", northwest_candidate)
            print(card[y][index_matchernorth+1])
            north_holder.append(card[y])
            for y in range(len(card)):
                if matcher_northwest in card[y]:
                    index_matchernorthwest = card[y].index(matcher_northwest)
                    print("index right", index_matchernorthwest)
                    if index_matchernorthwest < 3:
                        matcher_northwest = card[y][index_matchernorth + 1]
                    else:
                        matcher_northwest = card[y][index_matchernorth - 3]
                    northwest_candidate = int(matcher_northwest * -1)
                    print("Northwest candidate", northwest_candidate)
                    print(card[y][index_matchernorth + 1])
                    north_holder.append(card[y])

    print("North Holder" , north_holder)

    matcher_west = (card[item][3]) *-1
    print(matcher_west)
    for y in range(len(card)):
        if matcher_west in card[y]:
            west_holder.append(card[y])
    print("West Holder", west_holder)


''''
    for k in range(len(north_holder)):
            print(card[x])
            place_in_card = north_holder[x].index(z)
            print(place_in_card)
            if place_in_card < 3:
                print("The number to the right is ", card[x][place_in_card + 1])
            else:
                print("The number to the right is ", card[x][place_in_card -3])
        else:
            print("There is no ", z , "in card ", card[x][5])
        x += 1


# tester for finding "North" cards and "not North" cards
# print("NORTH for ", card[card_number][5])
#print("North holder", north_holder)
#card_number += 1
# print("not NORTH for ", card[card_number][5])
# print(not_north_holder)
'''
''''# this finds all the cards on left
matcher_west = int(card[card_number][3] * -1)
print("matcher_west is :", matcher_west)

w = 0
west_holder = []
available_for_northwest = []
for element in not_north_holder:

    if (matcher_west in not_north_holder[w]):
        west_holder.append(not_north_holder[w])
    else:
        available_for_northwest.append(not_north_holder[w])
    w += 1
print("WEST")
print(west_holder)
print("still available")
print(available_for_northwest)
print("\n ")
card_number += 1

candidate_Center = []
candidate_North = []
candidate_West = []
candidate_NorthWest = []
candidate_South = []
candidate_SouthWest = []
candidate_East = []
candidate_SouthEast = []
candidate_NorthEast = []
'''

'''
#this finds all the cards on left
matcher_west = int(card[card_number][3] * -1)
print("matcher_west is :", matcher_west)

w = 0
west_holder = []
available_for_northwest = []
for element in not_north_holder:

       if (matcher_west in not_north_holder[w]):
              west_holder.append(not_north_holder[w])
       else:
          available_for_northwest.append(not_north_holder[w])
       w += 1
print("WEST")
print(west_holder)
print("still available")
print(available_for_northwest)
print("\n ")
card_number += 1



#this finds all the cards on right


e = 1
east_holder = []
while e <= 8:

       if (-1 in card[e]):
              east_holder.append(card[e][5])

       e += 1
print("EAST")
print(east_holder)

#this finds all the cards on bottom
s = 1
south_holder = []
while s <= 8:
       if (-4 in card[s]):
             south_holder.append(card[s][5])

       s += 1
print("SOUTH")
print(south_holder)

'''

'''
def rotate_east(card_number):
       print(card[card_number])
       temp_card= [card[card_number][1], card[card_number][2], card[card_number][3], card[card_number][0], "East" ]
       print(temp_card)
rotate_east(0)

def rotate_south(card_number):
       print(card[card_number])
       temp_card= [card[card_number][2], card[card_number][3], card[card_number][0], card[card_number][1], "South" ]
       print(temp_card)
rotate_south(0)

def rotate_west(card_number):
       print(card[card_number])
       temp_card= [card[card_number][3], card[card_number][0], card[card_number][1], card[card_number][2], "West" ]
       print(temp_card)
rotate_west(0)

'''

