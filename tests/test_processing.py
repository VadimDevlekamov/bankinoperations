from typing import Dict, List, Union

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_transactions() -> List[Dict[str, Union[str, int, bool]]]:
    """Фикстура с тестовыми данными транзакций"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-15T10:30:00.000000"},
        {"id": 2, "state": "CANCELED", "date": "2023-01-14T11:45:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-16T09:15:00.000000"},
        {"id": 4, "state": "PENDING", "date": "2023-01-13T14:20:00.000000"},
        {"id": 5, "state": "EXECUTED", "date": "2023-01-12T16:10:00.000000"},
    ]


# Тесты для filter_by_state
@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3, 5]),
        ("CANCELED", [2]),
        ("PENDING", [4]),
        ("UNKNOWN", []),
    ],
)
def test_filter_by_state(
    sample_transactions: List[Dict[str, Union[str, int, bool]]], state: str, expected_ids: List[int]
) -> None:
    """Тестирование фильтрации по различным состояниям"""
    result = filter_by_state(sample_transactions, state)
    assert [item["id"] for item in result] == expected_ids


def test_filter_default_state(sample_transactions: List[Dict[str, Union[str, int, bool]]]) -> None:
    """Тестирование фильтрации со значением по умолчанию"""
    result = filter_by_state(sample_transactions)
    assert [item["id"] for item in result] == [1, 3, 5]


# Тесты для sort_by_date
@pytest.mark.parametrize(
    "reverse, expected_order",
    [
        (True, [3, 1, 2, 4, 5]),  # Сортировка по убыванию (новые сначала)
        (False, [5, 4, 2, 1, 3]),  # Сортировка по возрастанию (старые сначала)
    ],
)
def test_sort_by_date(
    sample_transactions: List[Dict[str, Union[str, int, bool]]], reverse: bool, expected_order: List[int]
) -> None:
    """Тестирование сортировки по дате"""
    result = sort_by_date(sample_transactions, reverse)
    assert [item["id"] for item in result] == expected_order


def test_sort_default_order(sample_transactions: List[Dict[str, Union[str, int, bool]]]) -> None:
    """Тестирование сортировки со значением по умолчанию"""
    result = sort_by_date(sample_transactions)
    assert [item["id"] for item in result] == [3, 1, 2, 4, 5]


def test_sort_empty_list() -> None:
    """Проверка нормального поведения с пустым списком"""
    result = sort_by_date([])
    assert result == []


@pytest.mark.parametrize(
    "invalid_data",
    [
        [{"missing_date": "value"}],  # Отсутствие ключевого поля 'date'
        [{"date": "invalid_date_format"}],  # Некорректный формат даты
    ],
)
def test_sort_invalid_data(invalid_data: List[Dict[str, object]]) -> None:
    """Тестирование обработки невалидных данных"""
    with pytest.raises((KeyError, ValueError)):
        sort_by_date(invalid_data)
