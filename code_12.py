def get_fibonacci_number(position):
    if position == 0:
        return 0 
    if position == 1:
        return 1
    
    return get_fibonacci_number(position - 1) + get_fibonacci_number(position - 2)


# Had to change this sequence to start at 1 rather than 0.
def get_fibonacci_number_sequence(number):
    if number == 0:
        return [0]
    elif number == 1:
        return [1]
    
    prev1 = 1 
    prev2 = 1  
    number_sequence = [1, 1]

    # Had to make a correction in my identation for return.
    for i in range(2, number):
        current = prev1 + prev2  
        prev1 = prev2  
        prev2 = current  
        number_sequence.append(current)

    return number_sequence
    
if __name__ == "__main__":
    position = 5
    print(f"The fibonacci number for position {position} is {get_fibonacci_number(position)}")
    
    number = 10
    print(f"The fibonacci sequence for {number} is {get_fibonacci_number_sequence(number)}")