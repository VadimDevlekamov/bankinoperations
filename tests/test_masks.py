from typing import List, Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def valid_card_numbers() -> List[Union[str, int]]:
    """Фикстура для правильных номеров карт"""
    return ["1234567890123456", 1234567890123456, "1111222233334444"]


@pytest.fixture
def invalid_card_numbers() -> List[Union[str, None]]:
    """Фикстура для неправильных номеров карт"""
    return [
        "123456789012345",  # 15 цифр
        "12345678901234567",  # 17 цифр
        "1234abc890123456",  # содержит буквы
        "1234 5678 9012 3456",  # содержит пробелы
        "",  # пустая строка
    ]


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("1111222233334444", "1111 22** **** 4444"),
        ("9999888877776666", "9999 88** **** 6666"),
    ],
)
def test_get_mask_card_number_valid(card_number: str, expected: str) -> None:
    """Тестирование маскирования верных номеров карт"""
    masked: str = get_mask_card_number(card_number)
    assert masked == expected
    assert masked.count("*") == 6
    assert len(masked) == 19


def test_get_mask_card_number_with_fixture(valid_card_numbers: List[Union[str, int]]) -> None:
    """Тестирование маскирования верных номеров из фикстуры"""
    for card_number in valid_card_numbers:
        masked: str = get_mask_card_number(str(card_number))
        assert len(masked) == 19  # 16 цифр + 3 пробела
        assert "****" in masked
        assert masked.count("*") == 6
        assert len(masked.replace(" ", "")) == 16  # Проверка, что все цифры на месте


@pytest.mark.parametrize(
    "card_number",
    [
        "123456789012345",  # 15 цифр
        "12345678901234567",  # 17 цифр
        "1234abc890123456",  # содержит буквы
        "1234 5678 9012 3456",  # содержит пробелы
        "",  # пустая строка
    ],
)
def test_get_mask_card_number_invalid(card_number: str) -> None:
    """Тестирование обработки неправильных номеров карт"""
    with pytest.raises(ValueError, match="Номер карты должен состоять из 16 цифр"):
        get_mask_card_number(card_number)


def test_get_mask_card_number_invalid_with_fixture(invalid_card_numbers: List[Union[str, None]]) -> None:
    """Тестирование обработки неправильных номеров из фикстуры"""
    for card_number in invalid_card_numbers:
        # Проверяем, что card_number не None, его значение уже было убрано из фикстуры
        if card_number == "":
            with pytest.raises(ValueError):
                get_mask_card_number(card_number)
        elif isinstance(card_number, str):  # Проверяем, что это строка
            with pytest.raises(ValueError, match="Номер карты должен состоять из 16 цифр"):
                get_mask_card_number(card_number)


def test_get_mask_card_number_return_type(valid_card_numbers: List[Union[str, int]]) -> None:
    """Тестирование типа возвращаемого значения"""
    for card_number in valid_card_numbers:
        result: str = get_mask_card_number(str(card_number))
        assert isinstance(result, str)


def test_get_mask_card_number_none() -> None:
    """Тестирование обработки None значения"""
    with pytest.raises(ValueError):
        get_mask_card_number(None)  # Явно обрабатываем None


@pytest.fixture
def valid_account_numbers() -> List[str]:
    """Фикстура для правильных номеров счета"""
    return ["04944770040022409041", "07524754139846439921", "82173589689442693669"]


@pytest.fixture
def invalid_account_numbers() -> List[Union[str, None]]:
    """Фикстура для неправильных номеров счета"""
    return [
        "0494477004002240904",  # 19 цифр
        "075247541398464399211",  # 21 цифр
        "1234abc890123456",  # содержит буквы
        "8217358 96894 4269 3669",  # содержит пробелы
        "",  # пустая строка
    ]


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("04944770040022409041", "**9041"),
        ("07524754139846439921", "**9921"),
        ("82173589689442693669", "**3669"),
    ],
)
def test_get_mask_account_valid(account_number: str, expected: str) -> None:
    """Тестирование маскирования верных номеров счетов"""
    masked: str = get_mask_account(account_number)
    assert masked == expected
    assert masked.count("*") == 2
    assert len(masked) == 6
    assert masked[2:] == account_number[-4:]


def test_get_mask_account_invalid(invalid_account_numbers: List[Union[str, None]]) -> None:
    """Тестирование обработки неправильных номеров счетов"""
    for account_number in invalid_account_numbers:
        if account_number == "":
            with pytest.raises(ValueError):
                get_mask_account(account_number)
        elif isinstance(account_number, str):  # Проверяем, что это строка
            with pytest.raises(ValueError, match="Номер счёта должен состоять из 20 цифр"):
                get_mask_account(account_number)


def test_get_mask_account_with_fixture(valid_account_numbers: List[str]) -> None:
    """Тестирование маскирования правильных номеров из фикстуры"""
    for account_number in valid_account_numbers:
        masked: str = get_mask_account(account_number)
        assert masked.startswith("**")
        assert len(masked) == 6
        assert masked[2:].isdigit()
        assert len(masked[2:]) == 4
        assert masked[2:] == account_number[-4:]


def test_get_mask_account_type_check() -> None:
    """Тестирование обработки неверного типа ввода"""
    with pytest.raises(ValueError):
        get_mask_account(12345)
