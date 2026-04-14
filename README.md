# 🤖 WhatsApp Bot Python 

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Este é um assistente virtual automatizado. O bot monitora mensagens recebidas via WhatsApp Web e fornece um menu interativo de autoatendimento para colaboradores.

## 🚀 Funcionalidades

- **Triagem Automática:** Menu numérico para consulta de holerites, ponto e avisos.
- **Direcionamento Humano:** Encaminha o colaborador diretamente para o link do WhatsApp dos especialistas de cada setor.
- **Suporte a Emojis:** Interface amigável com uso de ícones e formatação em negrito.
- **Anti-Conflito:** O bot ignora conversas arquivadas e foca apenas na lista de chats ativos.
- **Injeção de Texto Seguro:** Utiliza JavaScript para garantir que caracteres especiais e emojis sejam enviados corretamente sem travar o motor do navegador.

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/) - Linguagem principal.
- [Selenium WebDriver](https://www.selenium.dev/) - Automação do navegador.
- [Webdriver Manager](https://pypi.org/project/webdriver-manager/) - Gerenciamento automático do ChromeDriver.
- [JSON](https://www.json.org/json-en.html) - Armazenamento de configurações e fluxos de conversa.

## 📋 Pré-requisitos

Antes de rodar o projeto ou gerar o executável, você precisará:

1. Ter o **Google Chrome** instalado.
2. Ter o **Python 3.9+** instalado.
3. Instalar as dependências do projeto:
   ```bash
   pip install selenium webdriver-manager

⚙️ Configuração (config.json)
O comportamento do bot é totalmente editável através do arquivo config.json. Exemplo de estrutura:

JSON
{
  "nome_da_empresa": "TESTE",
  "atendentes_humanos": [
    { "nome": "Beatriz", "numero": "5511912345678", "setor": "DP" }
  ],
  "menu_principal": {
    "1": "📄 Consultar Holerites",
    "2": "⏰ Marcação de Ponto"
  },
  "respostas": {
    "boas_vindas": "Bem-vindo ao RH!",
    "erro": "⚠️ Opção inválida."
  }
}

💻 Como Rodar
Clone o repositório:

Bash
git clone [https://github.com/seu-usuario/rh-whatsapp-bot.git](https://github.com/seu-usuario/rh-whatsapp-bot.git)
Coloque o arquivo config.json na raiz da pasta.

Execute o script principal:

Bash
python bot.py
Escaneie o QR Code que aparecerá no navegador Chrome.

📦 Gerando o Executável (.EXE)
Para transformar o script em um programa para Windows que não dependa do Python instalado:

Instale o PyInstaller:

Bash
pip install pyinstaller
Gere o executável:

Bash
pyinstaller --onefile --console --collect-all selenium bot.py
O arquivo final estará na pasta dist/. Lembre-se de manter o config.json na mesma pasta do .exe.

⚠️ Observações Importantes
Modo de Exibição: O WhatsApp Web deve estar preferencialmente no Modo Claro e o zoom em 100%.

Segurança: Este bot foi desenvolvido para fins didáticos e produtividade interna. O uso excessivo pode violar os termos de serviço do WhatsApp. Use com responsabilidade.

Desenvolvido por [Jackson.Menezes]

---
