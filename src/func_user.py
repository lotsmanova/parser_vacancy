from src.vacancy import Vacancy


def get_vacancies_hh(vacancy: list[dict]) -> list[dict]:
    """
    Форматирование объектов hh.ru
    """
    obj_vacancy = [{
        'title': item['name'],
        'link': item['alternate_url'],
        'salary': item['salary']['from'] if item.get('salary') else '0',
        'requirements': item['snippet']['requirement'],
        'town': item['area']['name']
    } for item in vacancy]
    return obj_vacancy


def get_vacancies_sj(vacancy: list[dict]) -> list[dict]:
    """
    Форматирование объектов SuperJob
    """
    obj_vacancy = [{
        'title': item['profession'],
        'link': item['link'],
        'salary': item['payment_from'],
        'requirements': item['candidat'],
        'town': item['town']['title']
    } for item in vacancy]
    return obj_vacancy


def top_vacancies(vacancy: list[Vacancy], num: int) -> list[Vacancy]:
    """
    Топ вакансий
    """
    return vacancy[:num]


def filtered_vacancies(vacancy: list[Vacancy], list_param: list) -> list[Vacancy]:
    """
    Фильтрация вакансий по городу
    """
    res = []
    for v in vacancy:
        for p in list_param:
            if p in v.town:
                res.append(v)
    return res


def sorted_vacancies(vacancy: list[Vacancy]) -> list[Vacancy]:
    """
    Сортировка вакансий по ЗП
    """

    return sorted(vacancy, reverse=True)


def print_vacancies(res: list[Vacancy]) -> None:
    """
    Вывод вакансий в удобном для пользователя виде
    """

    for i, v in enumerate(res):
        print(f"{i+1}. Название: {v.title}, ссылка: {v.link}, зарплата от {v.salary}, город: {v.town}")
