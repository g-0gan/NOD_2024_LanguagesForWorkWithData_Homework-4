# #9_bank_account.py

class NoMoneyToWithdrawError(Exception):
    """Ошибка, вызываемая при недостаточности средств для снятия."""

    def __init__(self, message):
        super().__init__(message)


class PaymentError(Exception):
    """Ошибка, вызываемая при неверных платежах."""

    def __init__(self, message):
        super().__init__(message)


def print_accounts(account_dict):
    """
    Печатает список клиентов и их балансы.

    :param account_dict: Словарь, содержащий имена клиентов и их балансы.
    """
    print("Список клиентов ({}):".format(len(account_dict)))
    for i, (name, value) in enumerate(account_dict.items(), start=1):
        print("{}. {} {}".format(i, name, value))


def transfer_money(account_dict, account_from, account_to, value):
    """
    Переводит деньги между счетами.

    :param account_dict: Словарь, содержащий имена клиентов и их балансы.
    :param account_from: Имя клиента, с которого переводятся деньги.
    :param account_to: Имя клиента, которому переводятся деньги.
    :param value: Сумма для перевода.
    :raises PaymentError: Если один из аккаунтов не найден.
    :raises NoMoneyToWithdrawError: Если на счете недостаточно средств для перевода.
    """
    if account_dict.get(account_from) is None or account_dict.get(account_to) is None:
        raise PaymentError("Account not found.")
    if account_dict[account_from] < value:
        raise NoMoneyToWithdrawError("Insufficient funds.")

    account_dict[account_from] -= value
    account_dict[account_to] += value


# Пример использования
if __name__ == "__main__":
    accounts = {
        "Василий Иванов": 100,
        "Екатерина Белых": 1500,
        "Михаил Лермонтов": 400
    }

    print_accounts(accounts)

    payment_info = {
        "account_from": "Екатерина Белых",
        "account_to": "Василий Иванов"
    }

    try:
        payment_info["value"] = 200  # Сумма для перевода
        transfer_money(accounts, **payment_info)
        print("Transfer successful!")
    except (NoMoneyToWithdrawError, PaymentError) as e:
        print("Error:", e)

    print_accounts(accounts)
