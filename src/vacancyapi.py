from abc import ABC, abstractmethod
import requests
import os
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

    def __init__(self, url='https://api.hh.ru/vacancies') -> None:
        """
        Инициализация объекта класса
        """

        self.__base_url = url


    @property
    def url(self) -> str:
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

    def __init__(self, url='https://api.superjob.ru/2.0/vacancies') -> None:
        """
        Инициализация объекта класса
        """

        self.api_key = os.environ.get('API_KEY_SUPERJOB')
        self.__base_url = url
        self.__headers = {'X-Api-App-Id': self.api_key}


    @property
    def url(self) -> str:
        return self.__base_url


    @property
    def headers(self) -> dict:
        return self.__headers


    def get_vacancies(self, keyword: str) -> None:
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
