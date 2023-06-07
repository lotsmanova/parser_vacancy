from abc import ABC, abstractmethod
from src.vacancy import Vacancy
import json
import csv
from src.error import DeleteError, GetError

class FileSaver(ABC):
    """
    Абстрактный класс для работы с вакансиями
    """
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Добавление вакансии в файл
        """
        pass


    @abstractmethod
    def get_vacancy(self, parameter: str) -> [dict]:
        """
        Получение информации о вакансии по критериям
        """
        pass


    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """
        Удаление вакансии
        """
        pass


class JSONSaver(FileSaver):
    """
    Класс для работы с вакансиями в формате JSON
    """

    def __init__(self, path='../src/vacancy.json') -> None:
        """
        Инициализация объекта класса
        :param path: путь к файлу JSON
        """
        self.path = path
        # пустой список, в который записываем вакансии
        self.list_vacancy = []
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                self.list_vacancy = json.load(f)
        except FileNotFoundError:
            print('Неверный путь к файлу')


    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Добавление вакансии в файл JSON
        """
        self.list_vacancy.append({
            'title': vacancy.title,
            'link': vacancy.link,
            'salary': vacancy.salary,
            'requirements': vacancy.requirements,
            'town': vacancy.town
        })
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self.list_vacancy, f, indent=4, ensure_ascii=False)


    def get_vacancy(self, parameter: str) -> [dict]:
        """
        Получение информации о вакансии по критерию
        """
        result = []
        for vacancy in self.list_vacancy:
            if parameter in [vacancy['title'],
                             vacancy['link'],
                             vacancy['salary'],
                             vacancy['requirements'],
                             vacancy['town']]:
                result.append(vacancy)
        if not result:
            raise GetError('Вакансий с таким ключевым параметром нет в файле')
        return result


    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """
        Удаление вакансии
        """
        deleted = False
        for i, v in enumerate(self.list_vacancy):
            # если есть полное совпадение передаваемого объекта со словарем в файле, происходит его удаление
            if v['title'] == vacancy.title and v['link'] == vacancy.link \
                    and v['salary'] == vacancy.salary and v['requirements'] == vacancy.requirements \
                    and v['town'] == vacancy.town:
                del self.list_vacancy[i]
                deleted = True
                with open(self.path, 'w', encoding='utf-8') as f:
                    json.dump(self.list_vacancy, f, indent=4, ensure_ascii=False)
        if not deleted:
            raise DeleteError('Нельзя удалить, этой вакансии нет в файле')

class CSVSaver(FileSaver):
    """
    Класс для работы с вакансиями в формате CSV
    """

    def __init__(self, path='../src/vacancy.csv') -> None:
        """
        Инициализация объекта класса
        :param path: путь к файлу JSON
        """

        self.path = path


    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Добавление вакансии в файл CSV
        """

        with open(self.path, mode='a', encoding='utf-8') as f:
            file_writer = csv.writer(f, delimiter=',', lineterminator='\r')
            if f.tell() == 0:
                file_writer.writerow(['title', 'link', 'salary', 'requirements', 'town'])
            file_writer.writerow([vacancy.title, vacancy.link,
                                  vacancy.salary, vacancy.requirements, vacancy.town])


    def get_vacancy(self, parameter: str) -> [dict]:
        """
        Получение информации о вакансии по критерию
        """
        result = []
        with open(self.path, mode='r', encoding='utf-8') as f:
            file_reader = csv.DictReader(f, delimiter=",")
            for vacancy in file_reader:
                if parameter in [vacancy['title'],
                                vacancy['link'],
                                vacancy['salary'],
                                vacancy['requirements'],
                                vacancy['town']]:
                    result.append(vacancy)
            if not result:
                raise GetError('Вакансий с таким ключевым параметром нет в файле')
            return result


    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """
        Удаление вакансии
        """
        data = []
        deleted = False
        # поиск удаляемой вакансии
        with open(self.path, mode='r', encoding='utf-8') as f:
            file_reader = csv.DictReader(f, delimiter=",")
            for v in file_reader:
                # если есть полное совпадение передаваемого объекта
                # со словарем в файле не происходит его добавление в файл
                if v['title'] == vacancy.title and v['link'] == vacancy.link \
                        and v['salary'] == vacancy.salary and v['requirements'] == vacancy.requirements \
                        and v['town'] == vacancy.town:
                    deleted = True
                else:
                    data.append(v)
            if deleted:
                # добавление всех вакансий, кроме удаляемой в файл
                with open(self.path, mode='w', encoding='utf-8', newline='') as f:
                    if f.tell() == 0:
                        fieldnames = ['title', 'link', 'salary', 'requirements', 'town']
                        file_writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',', lineterminator='\r')
                        file_writer.writeheader()
                        file_writer.writerows(data)
            raise DeleteError('Нельзя удалить, этой вакансии нет в файле ')



