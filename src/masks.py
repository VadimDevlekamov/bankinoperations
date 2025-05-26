def get_mask_card_number(card_number: str | int) -> str:
    """Маскирует номер карты"""
    card_number = str(card_number)
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр")

    masked = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[12:]
    return masked


def get_mask_account(mask: str | int) -> str:
    """Маскирует номер счёта"""
    mask = str(mask)
    if not mask.isdigit() or len(mask) != 20:
        raise ValueError("Номер счёта должен состоять из 20 цифр")

    return "**" + mask[-4:]


# get_mask_card = get_mask_card_number(2042888836664441)
# print(get_mask_card)
mask_account = get_mask_account("73654108430135874305")
print(mask_account)
