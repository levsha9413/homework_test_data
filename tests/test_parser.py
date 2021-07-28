import json


def test_structure():
    '''
    Проверка того, что итоговый результат парсится библиотекой json
    '''
    with open("../result.json", "r") as result:
        assert type(json.load(result)) == list
