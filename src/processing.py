from typing import Dict, List, Union


def filter_by_state(
    list_dict: List[Dict[str, Union[str, int, bool]]], state: str = "EXECUTED"
) -> List[Dict[str, Union[str, int, bool]]]:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ 'state' соответствует указанному значению"""
    filter_list = []
    for item in list_dict:
        if item.get("state") == state:
            filter_list.append(item)
    return filter_list


def sort_by_date(
    data: List[Dict[str, Union[str, int, bool]]], reverse: bool = True
) -> List[Dict[str, Union[str, int, bool]]]:
    """Возвращает новый список, отсортированный по дате"""
    return sorted(data, key=lambda element: element["date"], reverse=reverse)


# # Пример использования
# transactions = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]
#
# filter_state = filter_by_state(transactions)
# print(filter_state)
#
# sort_date = sort_by_date(transactions)
# print(sort_date)
