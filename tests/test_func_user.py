import pytest
from src.func_user import get_vacancies_sj, get_vacancies_hh, top_vacancies, filtered_vacancies, sorted_vacancies, print_vacancies
from src.vacancy import Vacancy
@pytest.fixture
def list_vacancy():
    return [
    {
        "title": "Python разработчик (Junior)",
        "link": "https://hh.ru/vacancy/80456354",
        "salary": 100000,
        "requirements": "Знание <highlighttext>Python</highlighttext> 3 и базовых библиотек. * Опыт работы с реляционными БД, знание SQL, желательно – SQLAlchemy. * Опыт работы с веб фреймворками...",
        "town": "Москва"
    },
    {
        "title": "Разработчик python",
        "link": "https://hh.ru/vacancy/81706422",
        "salary": 2500,
        "requirements": "Rest/Fast/GraphQL Api + умение пользоваться док-ей, SQL (My / Lite), Selenium, Bs4, Qt5. Django/Flask, Умение...",
        "town": "Минск"
    },
    {
        "title": "Программист-стажер (Удаленно)",
        "link": "https://hh.ru/vacancy/81766684",
        "salary": 300,
        "requirements": "Будет плюсом: Опыт работы с OpenWrt/RDK-B. Опыт работы со скриптовыми языками программирования: bash, shell, <highlighttext>python</highlighttext>. Ключевые навыки: C...",
        "town": "Костанай"
    }
    ]


@pytest.fixture
def vacancy(list_vacancy):
    vacancies = [Vacancy(
                title=v['title'],
                link=v['link'],
                salary=v['salary'] if v.get('salary') else 0,
                requirements=v['requirements'],
                town=v['town'])
                for v in list_vacancy]
    return vacancies


def test_top_vacancies(list_vacancy):
    # TestCase#1 вывод топа вакансий
    assert top_vacancies(list_vacancy, 1) == [
                                                {
                                                    "title": "Python разработчик (Junior)",
                                                    "link": "https://hh.ru/vacancy/80456354",
                                                    "salary": 100000,
                                                    "requirements": "Знание <highlighttext>Python</highlighttext> 3 и базовых библиотек. * Опыт работы с реляционными БД, знание SQL, желательно – SQLAlchemy. * Опыт работы с веб фреймворками...",
                                                    "town": "Москва"
                                                }]


def test_filtered_vacancies(vacancy):
    # TestCase#2 фильтрация вакансий
    res = filtered_vacancies(vacancy, ['Минск'])
    assert res[0].town == 'Минск'


def test_sorted_vacancies(vacancy):
    # TestCase#3 сортировка вакансий
    res = sorted_vacancies(vacancy)
    assert res[0].salary == 100000
