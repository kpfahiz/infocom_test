import random

def owner_profit(value) -> float:
    '''
    Calculate the owner profit.
    owner profit calculate 10% of the position value.
    '''
    owner_profit = 0.1*value
    return owner_profit


def winning_percentage_90(value: int) -> float:
    '''
    Calculate the winning percentage 90.
    '''
    percentage_90 = 0.9*value
    return percentage_90

def winning_position_amount(value: int) -> int:
    '''
    Calculate the winning positions.
    It 9 times the value of the position.
    '''
    winning_position = 9*value
    return winning_position   

def generate_winning_position(position_values: list, sum_of_position_values: int) -> list:
    '''
    This function generates a random winning position for the players.
    It returns the winning position and it's value.
    '''
    positions_list, winning_positions_list, winning_amounts = [], [], []
    sum_of_the_values = sum_of_position_values
    percentage_90 = winning_percentage_90(sum_of_the_values)
    
    while True:
        value_for_the_position = random.choice(position_values)
        winning_amount = winning_position_amount(value_for_the_position)
        if winning_amount < percentage_90:
            #the win amount should less than 90% of the total bet value of the given List.
        
            positions_list.append(winning_amount)
            if sum(positions_list)<= percentage_90:
                #sum of the total winning amount should not exceed 90% of the total bet value of the given.
                
                winning_positions_list.append(value_for_the_position)
                winning_amounts.append(winning_amount)
            else:
                break
            
    return winning_positions_list, winning_amounts

if __name__ == "__main__":

    position_values = [100,50,500,10,30,700,250,390,880,777]
    sum_of_position_values = sum(position_values)
    winning_positions_list, winning_amounts = generate_winning_position(position_values, sum_of_position_values)
    print('Winning positions:', winning_positions_list)
    print('Winning Amounts:', winning_amounts)
    commission = owner_profit(sum_of_position_values)
    print('Owner Profit:', commission)
