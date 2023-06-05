class Vacancy:
    """
    Класс для работы с вакансиями
    """
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


    def __eq__(self, other) -> bool:
        """
        Сравнение вакансий по зарплате:
        объект 1 = 2
        """
        return self.salary == other.salary


    def __lt__(self, other) -> bool:
        """
        Сравнение вакансий по зарплате:
        объект 1 < 2
        """
        return self.salary < other.salary


    def __gt__(self, other) -> bool:
        """
        Сравнение вакансий по зарплате:
        объект 1 > 2
        """
        return self.salary > other.salary


    def validate_salary(self) -> bool:
        """
        Валидация зарплаты
        :return: bool
        """
        if not self.salary:
            return False
        if not isinstance(self.salary, str):
            return False
        if '-' in self.salary:
            salary_range = self.salary.split('-')
            if len(salary_range) != 2:
                return False
            if not salary_range[0].isdigit() or not salary_range[1].isdigit():
                return False
        elif not self.salary.isdigit():
            return False
        return True


    def validate_link(self):
        """
        Валидация ссылки
        :return: bool
        """
        if not self.link:
            return False
        if not isinstance(self.link, str):
            return False
        if not self.link.startswith('http'):
            return False
        return True


    def validate(self):
        """
        Валидация названия, ссылки, зарплаты,
        требований, города
        :return: bool
        """
        if not self.title or not isinstance(self.title, str):
            return False
        if not self.requirements or not isinstance(self.requirements, str):
            return False
        if not self.town or not isinstance(self.town, str):
            return False
        if not self.validate_link():
            return False
        if not self.validate_salary():
            return False
        return True
