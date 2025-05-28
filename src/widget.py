from src.masks import get_mask_account, get_mask_card_number

from typing import Union
from datetime import datetime


def mask_account_card(mask_account: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от входных данных.
    mask_account: Строка формата "Visa Platinum 1234567890123456" или "Счет 12345678901234567890"
    """
    if not isinstance(mask_account, str) or not mask_account.strip():
        raise ValueError("Неверный формат входных данных")

    parts = mask_account.split()
    if len(parts) < 2:
        raise ValueError("Неверный формат: должно быть название и номер")

    if "счет" in mask_account.lower():
        if len(parts) != 2 or not parts[1].isdigit() or len(parts[1]) != 20:
            raise ValueError("Номер счета должен состоять из 20 цифр")
        return f"Счет {get_mask_account(parts[1])}"
    else:
        # Проверяем известные типы карт
        valid_card_types = ["Maestro", "MasterCard", "Visa", "Mir"]
        if parts[0] not in valid_card_types:
            raise ValueError(f"Неизвестный тип карты. Допустимые: {', '.join(valid_card_types)}")

        if not parts[-1].isdigit() or len(parts[-1]) != 16:
            raise ValueError("Номер карты должен состоять из 16 цифр")
        return f"{' '.join(parts[:-1])} {get_mask_card_number(parts[-1])}"


def get_date(date: str) -> str:
    """
    Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ.
    """
    if not isinstance(date, str) or len(date) < 10 or date[4] != "-" or date[7] != "-":
        raise ValueError("Неверный формат даты")

    try:
        # Проверяем валидность даты
        datetime.strptime(date[:10], "%Y-%m-%d")
        return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
    except ValueError:
        raise ValueError("Неверная дата: месяц или день вне допустимого диапазона")


# mask_card = mask_account_card("Visa Gold 5999414228426353")
# print(mask_card)
# mask_account = mask_account_card("Счет 73654108430135874305")
# print(mask_account)
# date_today = get_date("2024-03-11T02:26:18.671407")
# print(date_today)
