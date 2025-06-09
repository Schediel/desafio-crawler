import requests  # Biblioteca para requisições HTTP
from bs4 import BeautifulSoup  # Biblioteca para parsing de HTML


def crawl_quotes(base_url="http://quotes.toscrape.com"):
    """
    Raspador de citações do site quotes.toscrape.com.
    Percorre todas as páginas e retorna uma lista de dicionários com texto, autor e tags.
    """
    quotes_data = []  # Lista para armazenar as citações
    page = 1  # Página inicial

    while True:
        url = f"{base_url}/page/{page}/"  # Monta a URL da página
        response = requests.get(url)  # Faz a requisição HTTP
        if "No quotes found!" in response.text:
            break  # Sai do loop se não houver mais citações

        # Faz o parsing(analisa a estrutura de um texto) do HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.select(".quote")  # Seleciona todos os blocos de citação

        for quote in quotes:
            text = quote.select_one(".text").get_text() # Extrai o texto da citação
            author = quote.select_one(".author").get_text() # Extrai o autor
            tags = [tag.get_text()
                    for tag in quote.select(".tags .tag")] # Extrai as tags
            quotes_data.append({"text": text, "author": author, "tags": tags})

        page += 1 # Vai para a próxima página

    return quotes_data  # Retorna a lista de citações
