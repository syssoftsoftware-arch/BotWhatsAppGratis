import json
import time
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def obter_diretorio_executavel():
    return os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(
        os.path.abspath(__file__))


class WhatsappBot:
    def __init__(self):
        self.diretorio = obter_diretorio_executavel()
        self.config_file = os.path.join(self.diretorio, 'config.json')

        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir={os.path.join(self.diretorio, 'perfil_bot')}")
        options.add_argument("--start-maximized")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        print("🚀 Iniciando sistema...")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("https://web.whatsapp.com")
        self.wait = WebDriverWait(self.driver, 60)

        print("📢 Aguardando login (Aponte o QR Code se necessário)...")
        self.wait.until(EC.presence_of_element_located((By.ID, "side")))
        print("✅ BOT ATIVO! Pronto para responder.")

    def responder_logica(self, texto, conf):
        texto = texto.lower().strip()
        if texto in conf['menu_principal']:
            if texto in ["3", "4"]:
                atendentes = "\n".join(
                    [f"👤 *{a['nome']}*: https://wa.me/{a['numero']}" for a in conf['atendentes_humanos']])
                return f"{conf['respostas']['aguarde']}\n\n{atendentes}"
            return f"Você selecionou: *{conf['menu_principal'][texto]}*. Aguarde um instante... ⏳"

        menu = "\n".join([f"*{k}* - {v}" for k, v in conf['menu_principal'].items()])
        return f"{conf['respostas']['boas_vindas']}\n\n{menu}\n\n{conf['respostas']['erro']}"

    def enviar(self, mensagem):
        try:
            # Localiza o campo de texto
            campo = self.wait.until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')))
            campo.click()
            time.sleep(0.5)

            # Copia o texto para o campo via JavaScript (suporta emojis e caracteres especiais)
            self.driver.execute_script("arguments[0].innerHTML = arguments[1];", campo, mensagem.replace('\n', '<br>'))

            # Pequena interação para o WhatsApp habilitar o botão de enviar
            campo.send_keys(Keys.SPACE)
            time.sleep(0.5)
            campo.send_keys(Keys.ENTER)
            print("📤 Resposta enviada!")
        except Exception as e:
            print(f"⚠️ Erro no envio: {e}")

    def monitorar(self):
        while True:
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    conf = json.load(f)

                # Busca bolinhas verdes APENAS na lista visível (IGNORA ARQUIVADOS)
                # O XPath abaixo é específico para a área de chats ativa
                notificacoes = self.driver.find_elements(By.XPATH,
                                                         '//div[@id="pane-side"]//span[contains(@aria-label, "não lida")]')

                if notificacoes:
                    print(f"🔔 Nova mensagem detectada!")
                    # Abre a conversa
                    notificacoes[0].click()
                    time.sleep(1.5)

                    # Tenta ler o texto da última mensagem recebida
                    baloes = self.driver.find_elements(By.CSS_SELECTOR, ".message-in")
                    if baloes:
                        texto_recebido = baloes[-1].find_element(By.CSS_SELECTOR, "span.selectable-text").text
                        print(f"📩 Mensagem: {texto_recebido}")

                        resposta = self.responder_logica(texto_recebido, conf)
                        self.enviar(resposta)

                    # Sai da conversa para não ficar "preso" e marcar como lida
                    webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                    time.sleep(1)

                time.sleep(2)
            except Exception:
                time.sleep(2)


if __name__ == "__main__":
    try:
        bot = WhatsappBot()
        bot.monitorar()
    except Exception as e:
        print(f"❌ Erro crítico: {e}")
        input("Pressione ENTER para sair...")