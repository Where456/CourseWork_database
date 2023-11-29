from pprint import pprint

import requests


class HhApi:
    def __init__(self):
        self.base_url = "https://api.hh.ru"

    def get_companies_and_vacancies(self, params):
        endpoint = "/vacancies"
        url = f"{self.base_url}{endpoint}"

        data = requests.get(url, params=params).json()
        formatted_companies_and_vacancies = []

        for vacancy in data['items']:
            company_name = vacancy.get("employer", {}).get("name", "Не указано")
            formatted_vacancy = {
                "name": vacancy.get("name", "Не указано"),
                "salary": vacancy.get("salary", "Не указано"),
                "url": vacancy.get("alternate_url", "Не указано"),
                "company_name": company_name
            }

            existing_company = next(
                (comp for comp in formatted_companies_and_vacancies if comp["company_name"] == company_name), None)
            if existing_company:
                existing_company["vacancies"].append(formatted_vacancy)
            else:
                formatted_companies_and_vacancies.append({
                    "company_name": company_name,
                    "vacancies": [formatted_vacancy]
                })

        return formatted_companies_and_vacancies


if __name__ == "__main__":
    pprint(HhApi().get_companies_and_vacancies(''))



 # {'company_name': 'Яндекс Команда для бизнеса',
 #  'vacancies': [{'company_name': 'Яндекс Команда для бизнеса',
 #                 'name': 'Удаленный специалист службы поддержки (в Яндекс)',
 #                 'platform': 'HeadHunter',
 #                 'salary': {'currency': 'RUR',
 #                            'from': 30000,
 #                            'gross': True,
 #                            'to': 44000},
 #                 'url': 'https://hh.ru/vacancy/90019928'}

 # {'company_name': 'Яндекс Команда для бизнеса',
 #  'vacancies': [{'company_name': 'Яндекс Команда для бизнеса',
 #                 'name': 'Удаленный специалист службы поддержки (в Яндекс)',