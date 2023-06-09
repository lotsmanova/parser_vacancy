class AddError(Exception):
    """
    Класс исключения добавления в файл
    """
    def __init__(self, text='Вакансия уже есть в файле'):
        super().__init__(text)


class DeleteError(Exception):
    """
    Класс исключения удаления
    """
    def __init__(self, text='Вакансии нет в файле'):
        super().__init__(text)


class GetError(Exception):
    """
    Класс исключения получения данных
    """
    def __init__(self, text='Нет такого параметра'):
        super().__init__(text)