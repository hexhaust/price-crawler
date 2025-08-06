# Price tracker para o site do Mercado Livre usando Playwright (headless, rápido e customizável)

## 💻 Plataforma recomendada

Este script foi desenvolvido e testado inicialmente em **Ubuntu 22.04 via WSL (Windows Subsystem for Linux)** rodando no Windows 10/11.

Embora funcione em outros sistemas, recomendamos **Linux x86_64** para melhor compatibilidade com o Playwright e as bibliotecas nativas utilizadas.

---

## ✅ Compatibilidade

| Plataforma         | Python compatível | Observações                                             |
|--------------------|-------------------|----------------------------------------------------------|
| Linux (x86_64)     | 3.8 – 3.12         | ✅ Recomendado, testado com WSL                          |
| Linux (ARM64)      | 3.8 – 3.12         | ⚠️ Pode exigir ajustes adicionais nos pacotes nativos    |
| macOS (Intel/ARM)  | 3.8 – 3.12         | ✅ Funciona com Homebrew instalado                       |
| Windows (x86_64)   | 3.8 – 3.12         | ⚠️ Requer terminal compatível com Playwright (CMD/Admin) |

> 📌 Recomendamos Python >= 3.10 para melhor compatibilidade e suporte ao Playwright.

---

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/price-crawler.git
cd price-crawler
```

### 2. Crie e ative um ambiente virtual (opcional mas recomendado)

WSL/Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:
```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instale o Playwright

```bash
pip install playwright
```

### 4. Instale as deps nativas (Linux/WSL)

```bash
sudo apt-get install -y libnspr4 libnss3 libatk1.0-0 libatk-bridge2.0-0 libatspi2.0-0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libxkbcommon0 libasound2
```

### 5. Instale os navegadores do Playwright

```bash
playwright install
```

> ℹ️ Alternativamente, você pode tentar:

```bash
playwright install-deps
```

Essa opção tenta instalar automaticamente as dependências nativas, mas pode falhar em ambientes como WSL. A instalação via `apt` é mais segura e controlada.

---

## 🔗 Qual URL devo usar?

No script, substitua o valor da variável `URL` por um **link de produto do Mercado Livre** que contenha o **ID do item no final da URL**.

### ✅ Exemplos de URLs válidas:

```
https://www.mercadolivre.com.br/iphone-16e-128-gb-preto-distribuidor-autorizado/p/MLB1046215784?pdp_filters=item_id:MLB3986439067
https://www.mercadolivre.com.br/monitor-gamer-lg-ultragear-27-full-hd-1ms-165hz-hdmi-displayport/p/MLB19115238
https://www.mercadolivre.com.br/microsoft-wireless-controller-series-xs-series-x-e-s-shock-blue-unidade-1/p/MLB16268159
```

Essas URLs terminam com um bloco `/p/{ID_DO_PRODUTO}` — isso é importante pois garante que a página mostrará os preços corretamente e de forma estável para o crawler.

> 🔎 Evite usar links com query strings de busca, filtros ou promoções temporárias (ex: `/oferta`, `/promotion`, `product_trigger` e etc).

Se quiser extrair o link direto de um item, clique no **título do produto** no Mercado Livre para pegar a URL limpa.


## Executando o script

Após a instalação, você pode rodar o script diretamente com:

```bash
python price-crawler.py
```

O terminal exibirá algo assim:

```
[2025-08-06 10:24:53.523908] 📦 Preço do produto:
💸 Preço original:         R$ x.xxx,xx
🔻 Preço com desconto:     R$ x.xxx,xx
```

---

## 📝 Licença

Este projeto está licenciado sob a Licença MIT — veja o arquivo LICENSE para mais detalhes.
