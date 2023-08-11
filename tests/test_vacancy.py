import pytest
from src.vacancy import Vacancy

@pytest.mark.parametrize("vacancy, res",
                         [
                          (Vacancy('', 'https://hh.ru/vacancy/123456', '100000-150000', 'Опыт от 3х лет...', 'Москва'), ''),
                          (Vacancy('Python-developer', 'https://hh.ru/vacancy/123456', '100000-150000', 'Опыт от 3х лет...', 'Москва'), 'Python-developer'),
                          (Vacancy('Java-developer', 'https://hh.ru/vacancy/123456', '100000-150000руб.', 'Опыт от 3х лет...', 'Москва'), 'Java-developer')
                         ])
def test_validate(vacancy, res):
    # TestCase#1 Проверка валидности данных
    assert vacancy.title == res


def test_comparison_by_salary():
    # TestCase#2 Проверка сравнения вакансий по ЗП
    v1 = Vacancy('Python-developer', 'https://hh.ru/vacancy/123456', 100000, 'Опыт от 3х лет...', 'Москва')
    v2 = Vacancy('Python-developer', 'https://hh.ru/vacancy/123456', 200000, 'Опыт от 3х лет...', 'Москва')
    lt = v1 < v2
    gt = v1 > v2
    assert lt is True
    assert gt is False