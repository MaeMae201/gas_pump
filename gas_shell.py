import gas_pump
import time, sys
typing_speed = 17 
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(typing_speed / 970.0)
    return input()
def main():
    print('\nWelcome to Rascals\n')
    purchase = slow_type('\nWould you like to pre-pay with a card or pay after?\n')
    
    gas_kind = slow_type('\n(1) Regular $1.98, (2) Mid-Grade $2.06, (3) Premium $2.20\n')
    
    if purchase == 'refuel':
        print(gas_pump.refuel())
        return None 
    if purchase == 'revenue':
        print('Your total revenue is ${:.2f}'.format(gas_pump.revenue()))
        return None

    if purchase == 'pre-pay':
      (dollars, gallons, gas_kind) = gas_pump.prepay(gas_kind)
    
    elif purchase == 'pay after': 
        (dollars, gallons, gas_kind) = gas_pump.prepay(gas_kind)
        gas_pump.log_txt(gas_kind, dollars, gallons)
    if gas_pump.take_away(gas_kind, gallons):
        print('Please Come Again')

if __name__ == '__main__':
    main()