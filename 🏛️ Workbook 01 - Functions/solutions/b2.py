users: list[dict] = [{
    'username': 'Val',
    'password': 'val',
    'pin': '0000',
    'bal': 12.34,
    'is_logged_in': False
}]

def LiteWallet():
    payload = auth()
    if payload['user'] is None:
        print(payload['status'])
        return
    user = payload['user']
    getDashboard(user)

def getDashboard(user):
    while user is not None:
        print(f'Hello, {user['username']}!')
        opt = input('1. Check Balance\n2. Withdraw\n3. Deposit\n4. Log out\nSelect an option: ')
        if opt == '1':
            payload = getBalance(user)
            if payload['user'] is None:
                print(payload['status'])
                return
    
def getBalance(user):
    err_count = 3
    pin = input('Please input your Pin: ')
    while err_count > 1:
        if pin == user['pin']:
            print(f'Hello {user['username']}!\nYour balance is: {user['bal']}')
            opt = input('1. Return')
            return {
                'status': 'Success',
                'user': user
            }
        else:
            err_count -= 1
            input(f'Invalid Pin. {err_count} chance(s) left.\nInput Pin: ')
    return {
        'status': 'Err: Too many invalid attempts.\nLogging out...',
        'user': None
        }
    

def auth():
    auth_opt = input('1. Login\n2. Register\nSelect an option: ')
    err_count = 3
    while err_count > 1 and auth_opt not in ('1','2'):
        err_count -= 1
        auth_opt = input(f'Valid tries left: {err_count}.\nPlease try again: ')
    if auth_opt == '1':
        return loginUser()
    if auth_opt == '2':
        return registerUser()
    return {
        'status': 'Err: Too manu invalid tries.\nGoodbye.',
        'user': None
    }

def loginUser():
    print('Login.\nInput your details...')
    u = input('Username: ')
    p = input('Password: ')
    for user in users:
        if user['username'] == u and user['password'] == p:
            user['is_logged_in'] = True
            return {
                'status': 'Success',
                'user': user
            }
    return {
        'status': 'Invalid credentials',
        'user': None
    }

def registerUser():
    print('User Sign Up.\nInput your details...')
    username = input('Username: ') 
    password = input('Password: ') 
    pin = input('Pin: ') 
    ini_dep = input('Initial Deposit: ')
    if username != '' and password != '' and pin != '' and ini_dep != '':
        users.append({
            'username': username,
            'password': password,
            'pin': pin,
            'bal': ini_dep,
            'is_logged_in': False
        })
        return loginUser()
    return {
        'status': 'Err: Couldn\'t register user',
        'user': None
    }
    
LiteWallet()