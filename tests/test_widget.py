from typing import Any

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "invalid_input, expected_msg",
    [
        ("Maestro 15968378687051991", "Неверный номер карты: должно быть 16 цифр"),
        ("Счет 646864736788947795891", "Неверный номер счета: должно быть 20 цифр"),
        ("MastearCard 7158300734726758", "Неверный тип карты: допустимые - Visa, MasterCard, Maestro, Mir"),
        ("Счет 3538303347444789556", "Неверный номер счета: должно быть 20 цифр"),
        ("Visa Classic 683198247673765", "Неверный номер карты: должно быть 16 цифр"),
        ("Visa Platinum 899092211а3665229", "Неверный номер карты: должно быть 16 цифр"),
        ("CardWithoutNumber", "Неверный формат: должно быть название и номер"),
        ("", "Неверный формат: пустые данные"),
        ("   ", "Неверный формат: пустые данные"),
        (None, "Неверный формат: получен None"),
        (12345, "Неверный формат: должно быть название и номер"),
    ],
)
def test_mask_account_card_invalid(invalid_input: Any, expected_msg: str) -> None:
    """Тест обработки невалидных данных для маскировки карт/счетов."""
    with pytest.raises(ValueError, match=expected_msg):
        mask_account_card(invalid_input)


@pytest.mark.parametrize(
    "invalid_date, expected_msg",
    [
        ("invalid-date", "Неверный формат даты: ожидается YYYY-MM-DD"),
        ("2020-13-01", "Неверная дата: некорректные значения"),
        ("2020-00-01", "Неверная дата: некорректные значения"),
        ("2020-01-32", "Неверная дата: некорректные значения"),
        ("2020/01/01", "Неверный формат даты: ожидается YYYY-MM-DD"),
        ("1234567890", "Неверный формат даты: ожидается YYYY-MM-DD"),
        ("", "Неверный формат даты: ожидается YYYY-MM-DD"),
        (None, "Неверный формат даты: получен None"),
        (20200101, "Неверный формат даты: ожидается YYYY-MM-DD"),
    ],
)
def test_get_date_invalid(invalid_date: Any, expected_msg: str) -> None:
    """Тест обработки невалидных дат."""
    with pytest.raises(ValueError, match=expected_msg):
        get_date(invalid_date)
