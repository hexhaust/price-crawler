from playwright.sync_api import sync_playwright
import datetime

URL = ""

def get_price():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ))

        page = context.new_page()
        page.goto(URL, timeout=60000)

        page.wait_for_selector("span.andes-money-amount__fraction")

        # captura tds os preços visiveis
        fractions = page.query_selector_all("span.andes-money-amount__fraction")
        cents = page.query_selector_all("span.andes-money-amount__cents")

        # garante q temos pelo menos 1 valor
        if not fractions:
            print("❌ Nenhum preço encontrado.")
            browser.close()
            return

        # monta os valores
        prices = []
        for i in range(len(fractions)):
            frac = fractions[i].inner_text()
            cent = cents[i].inner_text() if i < len(cents) else "00"
            prices.append(f"R$ {frac},{cent}")

        # printa td
        print(f"\n[{datetime.datetime.now()}] 📦 Preço do produto:")

        if len(prices) >= 2:
            print(f"💸 Preço original:         {prices[0]}")
            print(f"🔻 Preço com desconto:     {prices[1]}")
        # caso tenha um preço sem desconto
        else:
            print(f"💰 Preço unico:            {prices[0]}")

        browser.close()

get_price()
