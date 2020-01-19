'''

def function1():
    print("ahhhh")
    print("ahhhhh 2")
print("this is outside of the function")
function1()

def function2(x):
    return 2*x

a = function2(10)
print(a)

def function3(x, y):
    return x + y

e = function3(1, 2)
print(e)

def function4(x):
    print(x)
    print("still in this function")
    return 3 * x

f =  function4(5)
print (f)

def bmi_calculator(name, height, weight):
    bmi = weight / (height ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " not overweight"
    else:
        return name + " is  overweight"

e = bmi_calculator("Mitch", 1.8, 98)
print(e)
'''
card= [[-2, 1, 4 , -4 , 'North', 'A'],[ -3 , 1, -2, 4, 'North', 'B'],[ -1,-2, -3, -4, 'North', 'C'],
       [-2, 4, 3, -1, 'North', 'D'] , [ 3, 1, -2, 4, 'North', 'E'],[-3, -4, 2, 1, 'North', 'F'],
       [ 2, -1, 3, 4, 'North', 'G'],[-3, 4, -1, -2, 'North', 'H'],[2, 3, 1, -1, 'North', 'I']]

#if a card has a -2, find the number to the right (or 1 unit over) of the -2

def find_the_matcher_right(z):

    x = 0
    while x < 8:
        if z in card[x]:
            print(card[x])
            place_in_card = card[x].index(z)
            print(place_in_card)
            if place_in_card < 3:
                print("The number to the right is ", card[x][place_in_card + 1])
            else:
                print("The number to the right is ", card[x][place_in_card -3])
        else:
            print("There is no ", z , "in card ", card[x][5])
        x += 1
find_the_matcher_right(-2)

#if a card has a -2, find the number to the left (or 1 unit over) of the -2

def find_the_matcher_left(z):

    x = 0
    while x < 8:
        if z in card[x]:
            print(card[x])
            place_in_card = card[x].index(z)
            print(place_in_card)
            if place_in_card < 0:
                print("The number to the left is ", card[x][place_in_card - 1])
            else:
                print("The number to the left is ", card[x][3])
        else:
            print("There is no ", z , "in card ", card[x][5])
        x += 1
find_the_matcher_left(-2)



'''
def function3(x, y):
    return x + y

e = function3(1, 2)
print(e)

'''

