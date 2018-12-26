from codebug_tether.sprites import StringSprite
import requests
from datetime import date, timedelta
import codebug_tether
from codebug_tether import (IO_DIGITAL_OUTPUT,
                            IO_DIGITAL_INPUT,
                            IO_PWM_OUTPUT,)

item = None

codebug = codebug_tether.CodeBug()
codebug.set_leg_io(0, IO_DIGITAL_INPUT);
codebug.set_leg_io(1, IO_DIGITAL_INPUT);
codebug.set_leg_io(2, IO_DIGITAL_INPUT);
codebug.set_leg_io(3, IO_DIGITAL_INPUT);
codebug.set_leg_io(4, IO_DIGITAL_INPUT);
codebug.set_leg_io(5, IO_DIGITAL_INPUT);
codebug.set_leg_io(6, IO_DIGITAL_INPUT);
codebug.set_leg_io(7, IO_DIGITAL_INPUT);

coindeskApi = "http://api.coindesk.com/v1/bpi/currentprice/USD.json"


def get_currencies():
    coindesk_currencies = requests.get(coindeskApi + "supported-currencies.json").json()
    currency_list = []
    for currency in coindesk_currencies:
        currency_list.append(currency["currency"])
    return currency_list


def get_current_price(currency):
    return float(requests.get(coindeskApi + "currentprice/" + currency + ".json").json()["bpi"][currency]["rate"]
                 .replace(",", ""))


def get_historical_price(
        currency,
        start=date.today()-timedelta(days=31),
        end=date.today()
        ):
    start_string = f"{start.year:#02d}-{start.month:#02d}-{start.day:#02d}"
    end_string = f"{end.year:#02d}-{end.month:#02d}-{end.day:#02d}"
    return requests.get(f"{coindeskApi}historical/close.json?"
                        f"currency={currency}&start={start_string}&end={end_string}") \
.json()["bpi"]



while True:
    codebug.scroll_sprite(StringSprite(get_current_price('USD'), 'R'), 300/1000, 'L')
   
