import requests
from bs4 import BeautifulSoup

# Определяем список ключевых слов
KEYWORDS = ['дизайн', 'фото', 'web', 'python']


def get_articles():
    url = 'https://habr.com/ru/articles/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    


    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')

    matching_articles = []

    for article in articles:
        title = article.find('h2').text.strip()
        date = article.find('time')['datetime'].split('T')[0]
        link = article.find('h2').find('a')['href']
        preview_text = article.find('div', class_='tm-article-snippet').text.strip()

        for keyword in KEYWORDS:
            if keyword.lower() in title.lower() or keyword.lower() in preview_text.lower():
                matching_articles.append(f"{date} – {title} – {link}")
                break

    return matching_articles


if __name__ == "__main__":
    articles = get_articles()
    if articles:
        for article in articles:
            print(article)
    else:
        print("Не найдено подходящих статей.")