from quotexapi.stable_api import Quotex
import time
Email = "bereacode@gmail.com";
Password = Kelvin11468;

API = Quotex(Email, Password)
check_connect, message = API.connect()

API.change_balance("PRACTICE")
print(f'Demo Balance {API.get_balance()}')

if check_connect:
    while True:
        try:
            API.buy('USDJPY', '5', 'put', 120)
            print(f'Demo Balance: {API.get_balance()}') 
            time.sleep(1)
        except Exception as e:
            print(e)
