from src.vacancy import Vacancy
from src.filesaver import JSONSaver
from src.vacancyapi import HeadHunterAPI, SuperJobAPI
from src.func_user import top_vacancies, filtered_vacancies, sorted_vacancies, print_vacancies, get_vacancies_hh, get_vacancies_sj
import json


def main():
    keyword = input('Введите поисковой запрос: ')

    # получение вакансий по запросу с API
    hh_api = HeadHunterAPI()
    sj_api = SuperJobAPI()
    hh_vacancies = hh_api.get_vacancies(keyword)
    sj_vacancies = sj_api.get_vacancies(keyword)

    # приведение к общим ключам вакансий с платформ
    vacancies_hh = get_vacancies_hh(hh_vacancies)
    vacancies_sj = get_vacancies_sj(sj_vacancies)

    # добавление вакансий в файл
    js_saver = JSONSaver()
    js_saver.add_vacancy(vacancies_hh)
    js_saver.add_vacancy(vacancies_sj)

    # открытие файла на чтение
    with open('../src/vacancy.json', 'r', encoding='utf-8') as f:
        list_vacancy = json.load(f)

    # создание списка с объектами класса
        vacancies = [Vacancy(
                title=v['title'],
                link=v['link'],
                salary=v['salary'] if v.get('salary') else 0,
                requirements=v['requirements'],
                town=v['town'])
                for v in list_vacancy]

    # взаимодействие с пользователем
        top_num = int(input('Введите количество вакансий для вывода в топ: '))
        filter_words = input('''Введите название города для поиска вакансии: ''').split()
        filter_vacancies = filtered_vacancies(vacancies, filter_words)
        if not filter_vacancies:
            print("Нет вакансий, соответствующих заданным критериям")

    # вывод результата
        sort_vacancies = sorted_vacancies(filter_vacancies)
        top_vacancy = top_vacancies(sort_vacancies, top_num)
        printing = print_vacancies(top_vacancy)

    # очистка файла
    # js_saver.clear_data()


main()