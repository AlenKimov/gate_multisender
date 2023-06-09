from .paths import ADDRESSES_TXT_FILEPATH
from .config import HOST
from .gate_custom_withdraw import withdraw_many
from .ask import ask_api_settings, ask_script_settings

from gate_api import Configuration, ApiClient, WithdrawalApi


def multisend():
    print('Gate.io multisender by @AlenKimov')
    api_settings = ask_api_settings()
    script_settings = ask_script_settings()

    gate_api_config = Configuration(key=api_settings.key, secret=api_settings.secret, host=HOST)
    api_client = ApiClient(gate_api_config)
    withdrawal_api = WithdrawalApi(api_client)

    with open(ADDRESSES_TXT_FILEPATH, 'r') as file:
        addresses = [address.strip() for address in file.readlines()]
        if addresses:
            withdraw_many(
                withdrawal_api,
                script_settings.min_amount,
                script_settings.max_amount,
                addresses,
                script_settings.currency,
                script_settings.chain,
            )
        else:
            print('There are no addresses to multisend!\n'
                  f'Copy your addresses into {ADDRESSES_TXT_FILEPATH.name}\n'
                  'Make sure you make the addresses trusted here:\n'
                  'https://www.gate.io/myaccount/add_withdraw_address_list')
