from abc import ABC, abstractmethod
from src.vacancy import Vacancy
import json
import csv
from src.error import DeleteError, GetError, AddError


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
        self.__path = path
        # пустой список, в который записываем вакансии
        self.list_vacancy = []
        try:
            with open(self.__path, 'r', encoding='utf-8') as f:
                self.list_vacancy = json.load(f)
        except FileNotFoundError:
            print('Неверный путь к файлу')


    @property
    def path(self):
        return self.__path


    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Добавление вакансии в файл JSON
        """
        obj_vacancy = {
                'title': vacancy.title,
                'link': vacancy.link,
                'salary': vacancy.salary,
                'requirements': vacancy.requirements,
                'town': vacancy.town
            }
        # если вакансии нет в файле, добавляем
        if obj_vacancy not in self.list_vacancy:
            self.list_vacancy.append(obj_vacancy)
            with open(self.__path, 'w', encoding='utf-8') as f:
                json.dump(self.list_vacancy, f, indent=4, ensure_ascii=False)
        raise AddError("Вакансия уже есть в файле")


    def get_vacancy(self, parameter: str) -> [dict]:
        """
        Получение информации о вакансии по критерию
        """
        result = []
        for vacancy in self.list_vacancy:
            # проверка существования параметра
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
            # если есть полное совпадение передаваемого объекта со словарем в файле,
            # происходит его удаление
            if v['title'] == vacancy.title and v['link'] == vacancy.link \
                    and v['salary'] == vacancy.salary and v['requirements'] == vacancy.requirements \
                    and v['town'] == vacancy.town:
                # удаление словаря с данными вакансии
                del self.list_vacancy[i]
                deleted = True
                with open(self.__path, 'w', encoding='utf-8') as f:
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

        self.__path = path


    @property
    def path(self):
        return self.__path


    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Добавление вакансии в файл CSV
        """
        obj_vacancy = {
            'title': vacancy.title,
            'link': vacancy.link,
            'salary': vacancy.salary,
            'requirements': vacancy.requirements,
            'town': vacancy.town
        }

        with open(self.__path, mode='r', encoding='utf-8') as f:
            file_reader = csv.DictReader(f, delimiter=",")
            rows = [row for row in file_reader]
            # проверка отсутствия вакансии в файле
            if obj_vacancy not in rows:
                with open(self.__path, mode='a', encoding='utf-8') as f_w:
                    file_writer = csv.writer(f_w, delimiter=',', lineterminator='\r')
                    if f_w.tell() == 0:
                        file_writer.writerow(['title', 'link', 'salary', 'requirements', 'town'])
                    file_writer.writerow([vacancy.title, vacancy.link,
                                          vacancy.salary, vacancy.requirements, vacancy.town])
            raise AddError("Такая вакансия уже есть в файле")


    def get_vacancy(self, parameter: str) -> [dict]:
        """
        Получение информации о вакансии по критерию
        """
        result = []
        with open(self.__path, mode='r', encoding='utf-8') as f:
            file_reader = csv.DictReader(f, delimiter=",")
            # проверка существования параметра
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
        deleted = False
        with open(self.__path, mode='r', encoding='utf-8') as f:
            file_reader = csv.DictReader(f, delimiter=",")
            rows = [row for row in file_reader]
        for row in rows:
            # если есть полное совпадение передаваемого объекта со словарем в файле,
            # происходит его удаление
            if row['title'] == vacancy.title and row['link'] == vacancy.link \
                    and row['salary'] == vacancy.salary \
                    and row['requirements'] == vacancy.requirements and row['town'] == vacancy.town:
                # удаление объекта
                rows.remove(row)
                deleted = True
                break
        if deleted:
            with open(self.__path, mode='w', encoding='utf-8', newline='') as f:
                if f.tell() == 0:
                    fieldnames = ['title', 'link', 'salary', 'requirements', 'town']
                file_writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',', lineterminator='\r')
                file_writer.writeheader()
                file_writer.writerows(rows)
        else:
            raise DeleteError('Нельзя удалить, этой вакансии нет в файле')
