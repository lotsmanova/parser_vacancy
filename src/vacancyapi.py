from abc import ABC, abstractmethod
import requests


class VacancyAPI(ABC):
    """
    Абстрактный класс для
    работы с API сайтов с вакансиями
    """
    @abstractmethod
    def getting_api(self, keyword: str, location: str) -> None:
        """
        Получение информации о вакансиях через API
        :return: None
        """
        pass


class HeadHunterAPI(VacancyAPI):
    """
    Класс для работы с API hh.ru
    """

    def __init__(self, url='https://api.hh.ru/vacancies'):
        """
        Инициализация объекта класса
        """
        self.url = url


    def getting_api(self, keyword: str, location: str) -> None:
        """
        Получение информации о вакансиях через API
        :return: None
        """
        params = {'keyword': keyword, 'town': location}
        # делаем запрос к API
        response = requests.get(self.url, params=params)
        if response.status_code == 200:
            # получение вакансий
            return response.json()
        else:
            print(f'Ошибка при выполнении запроса: {response.status_code}')


class SuperJob(VacancyAPI):
    """
    Класс для работы с API superjob.ru
    """

    def __init__(self, url='https://api.superjob.ru/2.0/vacancies'):
        """
        Инициализация объекта класса
        """
        self.url = url
        self.headers = {
        'X-Api-App-Id': 'v3.r.137595387.3b45cea28efc091e14131b2b7a5dd6b79ba08e14.e9f7b295caf7527e945323cee11e7bb4e80eb9f3'
        }


    def getting_api(self, keyword, location) -> None:
        """
        Получение информации о вакансиях через API
        :return: None
        """
        params = {'keyword': keyword, 'town': location}
        # делаем запрос к API
        response = requests.get(self.url, headers=self.headers, params=params)
        if response.status_code == 200:
            # получение вакансий
            return response.json()
        else:
            print(f'Ошибка при выполнении запроса: {response.status_code}')

