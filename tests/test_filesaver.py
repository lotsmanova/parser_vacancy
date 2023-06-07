import pytest
from src.filesaver import JSONSaver, CSVSaver
from src.vacancy import Vacancy
from src.error import DeleteError, GetError

def test_vacancy_jsonsaver():
    # TestCase#1 проверка методов JSONSaver()
    jssaver = JSONSaver('../src/vacancy.json')
    vacancy = Vacancy('test_title', 'test_link', 'test_salary', 'test_requirements', 'test_town')
    jssaver.add_vacancy(vacancy)
    assert jssaver.get_vacancy('test_link') == [{'link': 'test_link',
                                                  'requirements': 'test_requirements',
                                                  'salary': 'test_salary',
                                                  'title': 'test_title',
                                                  'town': 'test_town'}]
    jssaver.delete_vacancy(vacancy)
    with pytest.raises(DeleteError):
        jssaver.delete_vacancy(vacancy)


def test_vacancy_csvsaver():
    # TestCase#2 проверка методов CSVSaver()
    csvsaver = CSVSaver('../src/vacancy.csv')
    vacancy = Vacancy('test_title', 'test_link', 'test_salary', 'test_requirements', 'test_town')
    csvsaver.add_vacancy(vacancy)
    assert csvsaver.get_vacancy('test_link') == [{'link': 'test_link',
                                                  'requirements': 'test_requirements',
                                                  'salary': 'test_salary',
                                                  'title': 'test_title',
                                                  'town': 'test_town'}]
    with pytest.raises(DeleteError):
        csvsaver.delete_vacancy(vacancy)