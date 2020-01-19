def max_number(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return  max



def lbs_to_kg(weight):
    return weight * 0.45

def kg_to_lbs(weight):
    return  weight / 0.45