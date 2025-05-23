def get_mask_card_number(card_number: str | int) -> str:
    """Маскириует номер карты"""
    card_number = str(card_number)
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр")
    else:
        result = []
        masked = card_number[0:6] + "******" + card_number[12:]  # Маскируем (123456******3456)
        for i in range(0, 16, 4):
            result.append(masked[i : i + 4])
    return " ".join(result)


def get_mask_account(mask: str | int) -> str:
    """Маскирует номер счёта"""
    mask = str(mask)
    if not mask.isdigit():
        raise ValueError("Номер счёта должен состоять только из цифр")
    return "**" + mask[-4:]


get_mask_card = get_mask_card_number(2042888836664441)
print(get_mask_card)
mask_account = get_mask_account(2134564758)
print(mask_account)
