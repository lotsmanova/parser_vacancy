class Vacancy:
    """
    Класс для работы с вакансиями
    """
    def __init__(self, title, link, salary, requirements, town):
        # название вакансии
        self.__title = title
        # ссылка на вакансию
        self.__link = link
        # зарплата
        self.__salary = salary
        # требования
        self.__requirements = requirements
        # город
        self.__town = town


    @property
    def title(self):
        return self.__title


    @property
    def link(self):
        return self.__link


    @property
    def salary(self):
        return self.__salary


    @property
    def requirements(self):
        return self.__requirements


    @property
    def town(self):
        return self.__town


    def __eq__(self, other) -> bool:
        """
        Сравнение вакансий по зарплате:
        объект 1 = 2
        """
        return self.__salary == other.__salary


    def __lt__(self, other) -> bool:
        """
        Сравнение вакансий по зарплате:
        объект 1 < 2
        """
        return self.__salary < other.__salary


    def __gt__(self, other) -> bool:
        """
        Сравнение вакансий по зарплате:
        объект 1 > 2
        """
        return self.__salary > other.__salary


    def validate_salary(self) -> bool:
        """
        Валидация зарплаты
        :return: bool
        """
        if not self.__salary:
            return False
        if not isinstance(self.__salary, str):
            return False
        if '-' in self.__salary:
            salary_range = self.__salary.split('-')
            if len(salary_range) != 2:
                return False
            if not salary_range[0].isdigit() or not salary_range[1].isdigit():
                return False
        elif not self.__salary.isdigit():
            return False
        return True


    def validate_link(self):
        """
        Валидация ссылки
        :return: bool
        """
        if not self.__link:
            return False
        if not isinstance(self.__link, str):
            return False
        if not self.__link.startswith('http'):
            return False
        return True


    def validate(self):
        """
        Валидация названия, ссылки, зарплаты,
        требований, города
        :return: bool
        """
        if not self.__title or not isinstance(self.__title, str):
            return False
        if not self.__requirements or not isinstance(self.__requirements, str):
            return False
        if not self.__town or not isinstance(self.__town, str):
            return False
        if not self.validate_link():
            return False
        if not self.validate_salary():
            return False
        return True
