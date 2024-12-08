import requests
from bs4 import BeautifulSoup
from Algoritm import get_number, get_number_array

class Parser:
    cache = {}
    def __init__(self):
        pass
    def parse_all_data_from_public_user(self, username: str) -> dict:
        if username in self.cache:
            return self.cache[username]
        url = "https://robocontest.uz/profile/" + username
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        response = {}
        response["username"] = username
        response["full_name"] = soup.find("h3", {"class": "card-title text-center"}).b.text
        response['photo'] = soup.find("img", {"class": "rounded"}).get('src')
        response['register_date'] = soup.find("h6", {"class": "card-title text-center"}).text.split()[2]
        info_table = soup.find("table", {"class": "table table-borderless"}).find_all('td')
        response['bio'] = info_table[0].text.strip('\n').strip()
        response['murabbiy'] = info_table[1].text.strip('\n').strip()
        response["talim_muassasi"] = info_table[2].text.strip('\n').strip()
        response["viloyat"] = info_table[3].text.strip('\n').strip()
        response["tuman"] = info_table[4].text.strip('\n').strip()
        response['roborank'] = soup.find("h1", {"class":"mb-3"}).text.strip()
        response['roborating'] = soup.find_all("h1", {"class":"mb-3"})[1].text.strip()
        response["max_roborating"] = get_number(soup.find("small", {"class":"position-absolute"}).text.strip().strip('\n').strip())
        response["tasks_count"] = soup.find('div', {"class":"d-flex flex-column align-items-center"}).h3.text.strip()
        response['tasks_stars'] = soup.find("div", {"class":"progress"}).text.strip('\n').strip()
        info = soup.find_all("div", class_="px-4 py-2 col-12 col-md-6")
        for i in info:
            name = i.img.get('alt').replace('logo', '').strip()
            value = i.a.get('href')
            response[name] = value
        info = soup.find('td', {"class":"pr-3 align-middle text-right"}).text.strip('\n').strip()
        response['attempts'] = get_number_array(info)

        info = soup.find_all('a', {'data-toggle':"tooltip"})
        a,b,c = 0,0,0
        for i in info:
            if "bg-success" in i.get('class'):
                a += 1
            elif "bg-danger" in i.get('class'):
                b += 1
            else:
                c += 1
        response['solved_tasks'] = a
        response['unsolved_tasks'] = b
        response['not_attempted_tasks'] = c
        self.cache[username] = response
        return response