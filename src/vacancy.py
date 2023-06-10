class Vacancy:
    """
    Класс для работы с вакансиями
    """
    __slots__ = ('__title', '__link', '__salary', '__requirements', '__town')

    def __init__(self, title, link, salary, requirements, town):
        # название вакансии
        self.title = title
        # ссылка на вакансию
        self.link = link
        # зарплата
        self.salary = salary
        # требования
        self.requirements = requirements
        # город
        self.town = town


    def __lt__(self, other) -> bool:
        """
        Сравнение вакансий по зарплате:
        объект 1 < 2
        """
        if other.salary is None:
            return False
        if self.salary is None:
            return True
        return self.salary < other.salary


    def __gt__(self, other) -> bool:
        """
        Сравнение вакансий по зарплате:
        объект 1 > 2
        """
        return self.salary > other.salary


    @property
    def title(self):
        return self.__title


    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self.__title = value


    @property
    def link(self):
        return self.__link


    @link.setter
    def link(self, value):
        if isinstance(value, str) and value.startswith('http'):
            self.__link = value


    @property
    def salary(self):
        return self.__salary


    @salary.setter
    def salary(self, value):
        if isinstance(value, int):
            self.__salary = value
        if value == 'null' or value == '0':
            self.__salary = 0


    @property
    def requirements(self):
        return self.__requirements


    @requirements.setter
    def requirements(self, value):
        if isinstance(value, str):
            self.__requirements = value


    @property
    def town(self):
        return self.__town


    @town.setter
    def town(self, value):
        if isinstance(value, str):
            self.__town = value
