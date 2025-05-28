from datetime import datetime
# src/widget.py
from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(mask_account: Union[str, None, int]) -> str:
    """
    Маскирует номер карты или счета.

    Args:
        mask_account: Может быть строкой, None или числом

    Returns:
        Строка с замаскированным номером

    Raises:
        ValueError: Если входные данные неверного формата
    """
    VALID_CARD_TYPES = ["Visa", "MasterCard", "Maestro", "Mir"]  # Допустимые типы карт

    if mask_account is None:
        raise ValueError("Неверный формат: получен None")

    if isinstance(mask_account, int):
        mask_account = str(mask_account)

    if not isinstance(mask_account, str) or not mask_account.strip():
        raise ValueError("Неверный формат: пустые данные")

    parts = mask_account.split()
    if len(parts) < 2:
        raise ValueError("Неверный формат: должно быть название и номер")

    if "счет" in mask_account.lower():
        if len(parts) != 2 or not parts[1].isdigit() or len(parts[1]) != 20:
            raise ValueError("Неверный номер счета: должно быть 20 цифр")
        return f"Счет {get_mask_account(parts[1])}"
    else:
        # Проверяем допустимые типы карт
        card_type = parts[0]
        if card_type not in VALID_CARD_TYPES:
            raise ValueError("Неверный тип карты: допустимые - Visa, MasterCard, Maestro, Mir")

        if not parts[-1].isdigit() or len(parts[-1]) != 16:
            raise ValueError("Неверный номер карты: должно быть 16 цифр")
        return f"{' '.join(parts[:-1])} {get_mask_card_number(parts[-1])}"


def get_date(date: Union[str, None, int]) -> str:
    """
    Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ.

    Args:
        date: Может быть строкой, None или числом

    Returns:
        Строка с датой в формате ДД.ММ.ГГГГ

    Raises:
        ValueError: Если входные данные неверного формата
    """
    if date is None:
        raise ValueError("Неверный формат даты: получен None")

    if isinstance(date, int):
        date = str(date)

    if not isinstance(date, str) or len(date) < 10 or date[4] != "-" or date[7] != "-":
        raise ValueError("Неверный формат даты: ожидается YYYY-MM-DD")

    try:
        datetime.strptime(date[:10], "%Y-%m-%d")
        return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
    except ValueError:
        raise ValueError("Неверная дата: некорректные значения")


mask_card = mask_account_card("Visa Gold 5999414228426353")
print(mask_card)
mask_account = mask_account_card("Счет 73654108430135874305")
print(mask_account)
date_today = get_date("2024-03-11T02:26:18.671407")
print(date_today)
# mask_card = mask_account_card("Maestro 7000792289606361")
# print(mask_card)
# # mask_account = mask_account_card("Счет 73654108430135874305")
# # print(mask_account)
# date_today = get_date("2024-03-11T02:26:18.671407")
# print(date_today)
