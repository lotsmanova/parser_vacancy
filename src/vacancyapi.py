from abc import ABC, abstractmethod
import requests

class VacancyAPI(ABC):
    """
    Абстрактный класс для
    работы с API сайтов с вакансиями
    """
    @abstractmethod
    def get_vacancies(self, keyword: str) -> None:
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
        self.__base_url = url


    @property
    def url(self):
        return self.__base_url


    def get_vacancies(self, keyword: str) -> None:
        """
        Получение информации о вакансиях через API
        :return: None
        """

        # запрос к API
        url = f'{self.__base_url}?text={keyword}'
        response = requests.get(url)

        if response.status_code == 200:
            # получение вакансий
            vacancies = response.json()['items']
            return vacancies
        else:
            print(f'Ошибка при выполнении запроса: {response.status_code}')


class SuperJobAPI(VacancyAPI):
    """
    Класс для работы с API superjob.ru
    """

    def __init__(self, url='https://api.superjob.ru/2.0/vacancies'):
        """
        Инициализация объекта класса
        """
        self.__base_url = url
        self.__headers = {
        'X-Api-App-Id': 'v3.r.137595387.3b45cea28efc091e14131b2b7a5dd6b79ba08e14.e9f7b295caf7527e945323cee11e7bb4e80eb9f3'
        }


    @property
    def url(self):
        return self.__base_url


    @property
    def headers(self):
        return self.__headers


    def get_vacancies(self, keyword) -> None:
        """
        Получение информации о вакансиях через API
        :return: None
        """
        # делаем запрос к API
        url = f'{self.__base_url}?keyword={keyword}'
        response = requests.get(url, headers=self.__headers)
        if response.status_code == 200:
            vacancies = response.json()['objects']
            return vacancies
        else:
            print(f'Ошибка при выполнении запроса: {response.status_code}')
