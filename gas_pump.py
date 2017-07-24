#create a log.txt that adds a new line of data after each sale

def get_gas_price(gas_kind):
    """This was made by Maegan in Base Camp
    """
    if gas_kind == '1':
        return 1.99
    elif gas_kind == '2':
        return 2.07
    elif gas_kind == '3':
        return 2.20

    print('Try again.')
    return None 

def cal_pay_after(gas_kind):
    """
    """
    gallons = float(input('\nHow many gallons will you be purchasing?\n'))
    price = get_gas_price(gas_kind)
    dollars = gallons * price
    print('\nYour total is: $', round(dollars, 2), sep='')
    return [dollars, gallons, gas_kind]
    
def prepay(gas_kind):
    """
    """
    money = float(input('\nHow much money will you be spending?\n'))
    price = get_gas_price(gas_kind)
    gallons = money / price
    print('\nTotal amount of gallons purchased:\n', round(gallons, 2))
    return [money, gallons, gas_kind]

def log_txt(gas_kind, gallons, dollars):
    if gas_kind == '1'or gas_kind.lower() == 'one':
        gas_kind = 'regular' 

    if gas_kind == '2'or gas_kind.lower() == 'two':  
        gas_kind = 'midgrade'

    elif gas_kind == '3' or gas_kind.lower() == 'three':
        gas_kind = 'premium'
    message = '{}, {}, {}\n'.format(gas_kind, dollars, gallons)

    with open('log.txt', 'a') as file:
        file.write(message)
    return gas_kind

def tank_inven():
#open the file 
    inventory = []
    with open('tank.txt','r') as file:
        file.readline()
        str_inventory = file.readlines()

    for item in str_inventory:
        sub_list = item.strip().split(', ')
        inventory.append([sub_list[0], sub_list[1], float(sub_list[2]), float(sub_list[3])])
    return inventory 

def take_away(gas_kind, gallons):
    str_l = ['code, type, amount_in_inventory, price']
    inventory = tank_inven()
    for item in inventory:
        if item[0] == gas_kind:
            if gallons > item[2]:
                print("Sorry, we dont have no more gas.")
                return False
            else:
                item[2] = item[2] - gallons
        str_l.append('{}, {}, {}, {}'.format(item[0], item[1], item[2], item[3]))
        message = '\n'.join(str_l)
    with open('tank.txt','w') as file:
        file.write(message)
    return True 

def refuel():
    str_l = ['code, type, amount_in_inventory, price']
    inventory = tank_inven()
    for item in inventory:
        if item[2] <= 2500.0:
            item[2] = 5000.0
        item[2] = str(item[2])
        item[3] = str(item[3])
        str_l.append(', '.join(item))
    message = '\n'.join(str_l)        
    with open('tank.txt','w') as file:
        file.write(message)
    return message 
    # everytime the amount_in_inventory gets down to 2500.0 it should update
    # back to 5000.0 gallons in tank.txt

def revenue():
    inventory = in_the_log()
    price = 0 
    for item in inventory:
        item[2] = float(item[2]) + float(item[2])
        price += item[2]
    return price