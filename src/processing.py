from datetime import datetime
from typing import Any, Dict, List, Union, cast


def filter_by_state(transactions: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция возвращает новый список словарей, содержащих только те записи,
    у которых ключ 'state' соответствует указанному значению."""
    return [item for item in transactions if item.get("state") == state]


def parse_date(date_str: str) -> datetime:
    """Преобразует строку даты в объект datetime."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError as e:
        raise ValueError(f"Неверный формат даты '{date_str}'") from e


def sort_by_date(transactions: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Сортирует список транзакций по дате."""
    if not isinstance(transactions, list):
        raise TypeError("Переданный аргумент должен быть списком транзакций.")

    # Выполняем принудительное приведение типов (для mypy)
    transactions_casted = cast(List[Dict[str, Union[str, int, bool]]], transactions)

    # Применяем безопасную сортировку
    return sorted(transactions_casted, key=lambda tx: parse_date(tx["date"]), reverse=reverse)


# Пример использования
if __name__ == "__main__":
    transactions = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    print("Filter by EXECUTED:")
    print(filter_by_state(transactions))

    print("\nSort by date (descending):")
    print(sort_by_date(transactions))
#
#     print("\nSort by date (ascending):")
#     print(sort_by_date(transactions, False))
