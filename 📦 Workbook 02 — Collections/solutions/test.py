squad = ['Val', 'Justice', 'Ezzy']

def squad_manager(l: list):
    opt = '0'
    while opt != '5':
        if opt == '0':
            opt = get_menu_opt()
        
        if opt == '1':
            add_player(l)
            opt = '0'  # Reset opt back to '0' to show the menu again
        elif opt == '2':
            remove_player(l)
            opt = '0'  # Reset opt back to '0'
        elif opt == '3':
            show_squad(l)
            opt = '0'
        elif opt == '4':
            count_players(l)
            opt = '0'

    print('\nExiting...')

def add_player(l: list) -> list:
    print('\nADD PLAYER:')
    val = input('Player Name: ')
    if val == '':
        print("Operation Failed: Couldn't add this player\nReturning to menu...\n")
        return l
    l.append(val)
    print('\nAdding player successful.\nReturning to menu...\n')
    return l

def remove_player(l: list) -> list:
    print('\nREMOVE PLAYER:')
    val = input('Player Name: ')
    if val == '':
        print("Operation Failed: Couldn't remove this player\nReturning to menu...\n")
        return l
    
    # Simple direct membership check instead of a loop
    if val in l:
        l.remove(val)
        print('\nPlayer removal successful.\nReturning to menu...\n')
    else:
        print(f'\nPlayer "{val}" not found in squad.\nReturning to menu...\n')
    return l

def show_squad(l: list):
    print('\nCURRENT SQUAD:')
    if not l:
        print('Squad is empty.')
    else:
        for idx, player in enumerate(l, 1):
            print(f'{idx}. {player}')
    print('\nReturning to menu...\n')

def count_players(l: list):
    print(f'\nTotal players in squad: {len(l)}')
    print('Returning to menu...\n')

def get_menu_opt() -> str:
    print('=================\n  SQUAD MANAGER  \n=================')
    attempts = 3
    
    while attempts > 0:
        opt = input('1. Add player\n2. Remove player\n3. Show squad\n4. Count players\n5. Exit\nSelect an option: ')
        if opt in ('1', '2', '3', '4', '5'):
            return opt
        
        attempts -= 1
        if attempts > 0:
            print(f'\nInvalid input, try again.\nAttempts remaining: {attempts}\n')
    
    print('\nToo many invalid attempts.')
    return '5'

squad_manager(squad)