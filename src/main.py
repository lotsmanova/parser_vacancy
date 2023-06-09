from src.vacancy import Vacancy
from src.filesaver import JSONSaver, CSVSaver
from src.vacancyapi import HeadHunterAPI, SuperJobAPI
from src.func_user import top_vacancies, filtered_vacancies, sorted_vacancies, print_vacancies

def main():
    platform = input('Выберите платформу поиска вакансий. 1 - HeadHunter, 2 - SuperJob: ')
    # keyword = input('Введите ключевое слово для поиска, например, Python: ')
    if platform == '1':
        hh_api = HeadHunterAPI()
        hh_vacancies = hh_api.get_vacancies(keyword='Python')
        for item in hh_vacancies:
            title = item['name']
            link = f'https://nevinnomyssk.hh.ru/vacancy/{item["id"]}'
            requarements = item['snippet']['requirement']
            town = item['area']['name']
            if item['salary'] is not None:
                salary_from = item['salary']['from']
                salary_to = item['salary']['to']
                if salary_from is not None and salary_to is not None:
                    salary = f"{salary_from}-{salary_to}"
                else:
                    salary = None
                vacancy = Vacancy(title, link, salary, requarements, town)
                if vacancy.validate() is True:
                    js_saver = JSONSaver()
                    js_saver.add_vacancy(vacancy)
                    csv_saver = CSVSaver()
                    csv_saver.add_vacancy(vacancy)
                else:
                    print('Error')
    else:
        sj_api = SuperJobAPI()
        sj_vacancies = sj_api.get_vacancies(keyword='Python')
        for item in sj_vacancies:
            title = item['profession']
            link = item['link']
            requarements = item['candidat']
            town = item['town']['title']
            salary_from = item['payment_from']
            salary_to = item['payment_to']
            if salary_from is not None and salary_to is not None:
                salary = f"{salary_from}-{salary_to}"
            else:
                salary = None
            vacancy = Vacancy(title, link, salary, requarements, town)
            if vacancy.validate() is True:
                js_saver = JSONSaver()
                js_saver.add_vacancy(vacancy)
                csv_saver = CSVSaver()
                csv_saver.add_vacancy(vacancy)
            else:
                print('Error')






main()