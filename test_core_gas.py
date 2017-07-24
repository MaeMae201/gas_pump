import gas_pump

def test_get_gas_price():
    assert gas_pump.get_gas_price('1')
    assert gas_pump.get_gas_price('2')
    assert gas_pump.get_gas_price('3')

# def __main__():
#      a = int(input('a=\n'))
#      b = int(input('b=\n'))
#      print('multiplication',gas_pump.cal_pay_after(a,b))

# def test_cal_pay_after():
#           assert gas_pump.cal_pay_after
