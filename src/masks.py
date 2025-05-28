from typing import Union


def get_mask_card_number(card_number: Union[str, int, None]) -> str:
    """Маскирует номер карты"""
    if card_number is None:
        raise ValueError("Номер карты не может быть пустым")

    card_str = str(card_number)
    if len(card_str) != 16 or not card_str.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр")

    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[12:]}"


def get_mask_account(mask: str | int) -> str:
    """Маскирует номер счёта"""
    mask = str(mask)
    if not mask.isdigit() or len(mask) != 20:
        raise ValueError("Номер счёта должен состоять из 20 цифр")

    return "**" + mask[-4:]


# get_mask_card = get_mask_card_number(2042888836664441)
# print(get_mask_card)
# mask_account = get_mask_account("73654108430135874305")
# print(mask_account)
