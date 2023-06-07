class DeleteError(Exception):
    def __init__(self, text='Такой вакансии в файле нет'):
        super().__init__(text)


class GetError(Exception):
    def __init__(self, text='Нет такого параметра'):
        super().__init__(text)