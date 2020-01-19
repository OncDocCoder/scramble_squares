card= [[-2, 1, 4 , -4 , 'North', 'A'],[ -3 , 1, -2, 4, 'North', 'B'],[ -1,-2, -3, -4, 'North', 'C'],
       [-2, 4, 3, -1, 'North', 'D'] , [ 3, 1, -2, 4, 'North', 'E'],[-3, -4, 2, 1, 'North', 'F'],
       [ 2, -1, 3, 4, 'North', 'G'],[-3, 4, -1, -2, 'North', 'H'],[2, 3, 1, -1, 'North', 'I']]



#a = len(card)
#print(a)


#print(a)
#b = a * -1
#north_holder =[]
#d = 1
#c = card[0][0+d]
#print(c)

#this finds all the cards on top card[0] =[-2, 1, 4 , -4 , 'North', 'A']

n = 1
north_holder = []
while  n <= 8:

       if (2 in card[n]):
              north_holder.append(card[n][5])
       n +=1
print("NORTH")
print(north_holder)

#this finds all the cards on left
w = 1
west_holder = []
while w <= 8:

       if (4 in card[w]):
              west_holder.append(card[w][5])
       w += 1
print("WEST")
print(west_holder)
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

#find position of value that matches and then find position of value next to it to get northwest possibles
# this finds the value to the right of the matching value
print(card[0]) #print card[0]
position_a= card[0].index(-4) #index of card for value needed
print(position_a) #print the value of the index needed
if position_a < 3:
        print(card[0][position_a+1])
else:
    print(card[0][position_a-3])

# this finds the value to the left of the matching value

print(card[0]) #print card[0]
position_a= card[0].index(1) #index of card for value needed
print(position_a) #print the value of the index needed
if position_a <1:
        print(card[0][position_a+3])
else:
        print(card[0][position_a-1])


#Things to do
#find value at north, east, south and west and make them variables
#find if card has doubles
# vowels list
vowels = [-2, 1, 4, -4, 'North', 'A']

# count element 'i'
count = vowels.count('North')

# print count
print('The count of North is:', count)

# count element 'p'
count = vowels.count(-2)

# print count
print('The count of -2 is:', count)


