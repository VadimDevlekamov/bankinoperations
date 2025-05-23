from .masks import get_mask_account, get_mask_card_number


def mask_account_card(mask_account: str) -> str:
    """Выводит на экран название карты и замаскированный номерб
    выводит Счет и замаскированный номер счёта"""
    if "счет" in mask_account.lower():
        parts = mask_account.split()
        if len(parts) < 2: # Проверяем на корректность ввода номера счета
            raise ValueError("Неверный формат номера счета")
        account_number = parts[1]
        return f"Счет {get_mask_account(account_number)}"
    else:
        parts = mask_account.split()
        if len(parts) < 2:
            raise ValueError("Неверный формат номера карты")

        card_name = " ".join(parts[:-1])
        card_number = parts[-1]
        masked_number = get_mask_card_number(card_number)
        return f"{card_name} {masked_number}"


mask_card = mask_account_card("Maestro 7000792289606361")
print(mask_card)
# mask_account = mask_account_card("Счет 73654108430135874305")
# print(mask_account)
