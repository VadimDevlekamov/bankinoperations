import pytest
from typing import Any
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "invalid_input, expected_msg",
    [
        ("Maestro 15968378687051991", "Номер карты должен состоять из 16 цифр"),
        ("Счет 646864736788947795891", "Номер счета должен состоять из 20 цифр"),
        ("MastearCard 7158300734726758", "Неизвестный тип карты"),
        ("Счет 3538303347444789556", "Номер счета должен состоять из 20 цифр"),
        ("Visa Classic 683198247673765", "Номер карты должен состоять из 16 цифр"),
        ("Visa Platinum 899092211а3665229", "Номер карты должен состоять из 16 цифр"),
        ("CardWithoutNumber", "Неверный формат: должно быть название и номер"),
        ("", "Неверный формат входных данных"),
        ("   ", "Неверный формат входных данных"),
        (None, "Неверный формат входных данных"),
        (12345, "Неверный формат входных данных"),
    ],
)
def test_mask_account_card_invalid(invalid_input: Any, expected_msg: str) -> None:
    """Тестирование обработки неверных форматов"""
    with pytest.raises(ValueError, match=expected_msg):
        mask_account_card(invalid_input)


@pytest.mark.parametrize(
    "invalid_date, expected_msg",
    [
        ("invalid-date", "Неверный формат даты"),
        ("2020-13-01", "Неверная дата: месяц или день вне допустимого диапазона"),
        ("2020-00-01", "Неверная дата: месяц или день вне допустимого диапазона"),
        ("2020-01-32", "Неверная дата: месяц или день вне допустимого диапазона"),
        ("2020/01/01", "Неверный формат даты"),
        ("1234567890", "Неверный формат даты"),
        ("", "Неверный формат даты"),
        (None, "Неверный формат даты"),
        (20200101, "Неверный формат даты"),
    ],
)
def test_get_date_invalid(invalid_date: Any, expected_msg: str) -> None:
    """Тестирование обработки неверных форматов даты"""
    with pytest.raises(ValueError, match=expected_msg):
        get_date(invalid_date)


def test_mask_account_card_edge_cases() -> None:
    """Тестирование крайних случаев маскирования"""
    # Проверка на ввод только пробелов
    with pytest.raises(ValueError, match="Неверный формат входных данных"):
        mask_account_card("   ")

    # Проверка на ввод None
    with pytest.raises(ValueError, match="Неверный формат входных данных"):
        mask_account_card(None)

    # Проверка на ввод числа
    with pytest.raises(ValueError, match="Неверный формат входных данных"):
        mask_account_card(12345)




def test_get_date_edge_cases() -> None:
    """Тестирование крайних случаев преобразования даты"""
    # Проверка на ввод None
    with pytest.raises(ValueError, match="Неверный формат даты"):
        get_date(None)

    # Проверка на ввод числа
    with pytest.raises(ValueError, match="Неверный формат даты"):
        get_date(20200101)

    # Проверка на неполную дату (только год)
    with pytest.raises(ValueError, match="Неверный формат даты"):
        get_date("2020")


def test_mask_account_card_returns() -> None:
    """Тестирование возвращаемых значений для счетов"""
    result = mask_account_card("Счет 12345678901234567890")
    assert result == "Счет **7890"  # Проверяем возвращаемую строку


def test_mask_account_card_returns_for_cards() -> None:
    """Тестирование возвращаемых значений для карт"""
    result = mask_account_card("Visa Classic 1234567890123456")
    assert result == "Visa Classic 1234 56** **** 3456"  # Проверяем возвращаемую строку


def test_get_date_returns() -> None:
    """Тестирование возвращаемого формата даты"""
    result = get_date("2023-12-31T00:00:00.000000")
    assert result == "31.12.2023"

