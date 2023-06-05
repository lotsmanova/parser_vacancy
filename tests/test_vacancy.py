import pytest
from src.vacancy import Vacancy

@pytest.mark.parametrize("vacancy, res_bool",
                         [
                          (Vacancy('', 'https://hh.ru/vacancy/123456', '100000-150000', 'Опыт от 3х лет...', 'Москва'), False),
                          (Vacancy('Python-developer', 'https://hh.ru/vacancy/123456', '100000-150000', 'Опыт от 3х лет...', 'Москва'), True),
                          (Vacancy('Python-developer', 'https://hh.ru/vacancy/123456', '100000-150000руб.', 'Опыт от 3х лет...', 'Москва'), False)
                         ])
def test_validate(vacancy, res_bool):
    # TestCase#1 Проверка валидности данных
    assert vacancy.validate() == res_bool


def test_comparison_by_salary():
    # TestCase#2 Проверка сравнения вакансий по ЗП
    v1 = Vacancy('Python-developer', 'https://hh.ru/vacancy/123456', '100000-150000', 'Опыт от 3х лет...', 'Москва')
    v2 = Vacancy('Python-developer', 'https://hh.ru/vacancy/123456', '200000-250000', 'Опыт от 3х лет...', 'Москва')
    eq = v1 == v2
    lt = v1 < v2
    gt = v1 > v2
    assert eq == False
    assert lt == True
    assert gt == False