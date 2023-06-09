

def top_vacancies(vacancy, num: int) -> [dict]:
    """
    Топ вакансий
    """
    return vacancy[:num]


def filtered_vacancies(vacancy, list_param) -> [dict]:
    """
    Фильтрация вакансий по ключевым словам
    """
    res = []
    for v in vacancy:
        for p in list_param:
            if p in [v['title'],
                     v['link'],
                     v['salary'],
                     v['requirements'],
                     v['town']]:
                res.append(v)
        else:
            print('Совпадений не найдено')
    return res


def sorted_vacancies(vacancy) -> [dict]:
    """
    Сортировка вакансий по ЗП
    :param vacancy
    :return:
    """
    v_sorted = sorted(vacancy, key=lambda d: d['salary'])
    return v_sorted


def print_vacancies(res) -> str:
    """
    Вывод вакансий в читабельном для пользователя виде
    :param res: список вакансий
    :return: str
    """
    pass
