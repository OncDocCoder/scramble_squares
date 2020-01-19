


card= [[-2, 1, 4 , -4 , 'North', 'A'],[ -3 , 1, -2, 4, 'North', 'B'],[ -1,-2, -3, -4, 'North', 'C'],
       [-2, 4, 3, -1, 'North', 'D'] , [ 3, 1, -2, 4, 'North', 'E'],[-3, -4, 2, 1, 'North', 'F'],
       [ 2, -1, 3, 4, 'North', 'G'],[-3, 4, -1, -2, 'North', 'H'],[2, 3, 1, -1, 'North', 'I']]


card2= [[-2, 1, 4 , -4 , 'North', 'A'],[ -3 , 1, -2, 4, 'North', 'B'],[ -1,-2, -3, -4, 'North', 'C'],
       [-2, 4, 3, -1, 'North', 'D'] , [ 3, 1, -2, 4, 'North', 'E'],[-3, -4, 2, 1, 'North', 'F'],
       [ 2, -1, 3, 4, 'North', 'G'],[-3, 4, -1, -2, 'North', 'H'],[2, 3, 1, -1, 'North', 'I']]

n = 1
matcher_north = int(card[card_number][0] * -1)
not_north_holder = []
north_holder = []
while n <= 8:

    if (matcher_north in card[n]):
        north_holder.append(card[n])
    n += 1
    num_North_possible = len(north_holder)

    # tester for finding "North" cards and "not North" cards
    #print("NORTH for ", card[card_number][5])
    #print(north_holder)
    #print("not NORTH for ", card[card_number][5])
    #print(not_north_holder)

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

candidate_Center = []
candidate_North = []
candidate_West = []
candidate_NorthWest = []
candidate_South = []
candidate_SouthWest = []
candidate_East = []
candidate_SouthEast = []
candidate_NorthEast = []

x = 0
y = 0
card_number = 0
for x in range(9):
    candidate_Center.append(card[x])
    #print(card[x])
    print(candidate_Center)
    candidate_Center.remove(card[x])
    for y in range(9):
       candidate_North.append(card[y])
    print(candidate_North)
print(candidate_Center)


# card_number += 1

#this finds all the card[0] =[-2, 1, 4 , -4 , 'North', 'A'] and the list that is not a north card
'''
#Way to repopulate pool of cards not being used
card_number = 0
y = 0
chair = 0
cards_available = []
not_available = []
available_counter = 0
list_test = [0, 1, 2, 3, 4, 5, 6, 7, 8]
list_test2= [0, 1, 2, 3, 4, 5, 6, 7, 8]

while y < 9:
    if y==0:
        print(list_test, y)
        list_test.insert(y, card[y])
        y += 1

while y < 9:
    list_test.pop(list_test[y])
    print(list_test, y)
    list_test.insert(y, list_test2[y])
    y += 1
    #print(" cards available, ", cards_available)
    #print("cards not available ", not_available)
'''

''' print (card[card_number])

    n = 1
    matcher_north = int(card[card_number][0] * -1)
    not_north_holder = []
    north_holder = []
    while  n <= 8:

           if (matcher_north in card[n]):
                  north_holder.append(card[n])
           else:
               not_north_holder.append(card[n])
           n +=1
    possible_west = len(not_north_holder)

    #tester for finding "North" cards and "not North" cards
    print("NORTH for ", card[card_number][5])
    print(north_holder)
    print("not NORTH for ", card[card_number][5])
    print(not_north_holder)
    cards_available = len(not_north_holder)
    cards_not_available = len(north_holder)
    print("cards available: ", cards_available)
    print("cards not available: ", cards_not_available)
    #card_number += 1
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
'''
'''


'''
'''#this finds all the cards on right


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

