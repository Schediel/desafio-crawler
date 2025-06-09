import schedule  # Biblioteca para agendamento
import time
from crawler import crawl_quotes  # Corrige o nome da função importada

# Função que executa o crawler e mostra o resultado


def job():
    URL = "https://quotes.toscrape.com"  # URL base do site
    citacoes = crawl_quotes(URL)  # Executa a raspagem
    print(f"Total de citações extraídas: {len(citacoes)}")  # Mostra o total
    print(citacoes[:3])  # Exibe as 3 primeiras citações para conferência


# Exemplo de uso utilitário para rodar o raspador diretamente
if __name__ == "__main__":
    # Agenda para rodar todo dia às 10:00
    schedule.every().day.at("15:30").do(job)
    print("Agendamento iniciado. Pressione Ctrl+C para sair.")
    while True:
        schedule.run_pending()
        time.sleep(1)
