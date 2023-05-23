print('_\u03321_|_\u03322_|_\u03323_')
print('_\u03324_|_\u03325_|_\u03326_')
print(' 7 | 8 | 9 ')
positions ={'1':'_', '2':'_', '3':'_', 
            '4':'_', '5':'_', '6':'_', 
            '7':' ', '8':' ', '9':' ', }
tries = 9

def is_invalid_input(input_value):  
    if not input_value.isnumeric() or int(input_value) < 1 or int(input_value) > 9:
        print("Wrong data, please enter a valid position: ")
    return True   
    if positions[input_value] =='X' or positions[input_value] =='O':
        print("Position already occupied, please select another: ")
    return True 

def print_board():
    print(f"_\u0332{positions['1']}_|_\u0332{positions['2']}_|_\u0332{positions['3']}_")
    print(f"_\u0332{positions['4']}_|_\u0332{positions['5']}_|_\u0332{positions['6']}_")
    print(f" {positions['7']} | {positions['8']} | {positions['9']} ")

def check_win(symbol):
    return ((positions['1'] == positions['2'] == positions['3'] == symbol) or
        (positions['4'] == positions['5'] == positions['6'] == symbol) or
        (positions['7'] == positions['8'] == positions['9'] == symbol) or
        (positions['1'] == positions['4'] == positions['7'] == symbol) or
        (positions['2'] == positions['5'] == positions['8'] == symbol) or
        (positions['3'] == positions['6'] == positions['9'] == symbol) or
        (positions['1'] == positions['5'] == positions['9'] == symbol) or
        (positions['3'] == positions['5'] == positions['7'] == symbol))

while tries >= 0:
    if tries == 0:
        print("It's a draw!")
        break
    player_number = 1 if tries % 2 == 1 else 2 
    input_value = input(f'Player {str(player_number)} enter position: ')
    if is_invalid_input(input_value):
        continue

    symbol = "X" if player_number == 1 else "O"

    positions[input_value] = symbol 
    tries -= 1
    print_board()
    #Check if the player won
    if check_win(symbol):    
        print(f'Player {str(player_number)} wins!')
        break  