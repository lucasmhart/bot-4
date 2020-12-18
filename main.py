from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

# web driver
webdriver_path = 'driver/Linux/chromedriver'
chrome_options = Options()
profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], # Disable Chrome's PDF Viewer
               "download.default_directory": '/tmp/' , "download.extensions_to_open": "applications/pdf"}
chrome_options.add_experimental_option("prefs", profile)
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-browser-side-navigation')
browser = webdriver.Chrome(executable_path=webdriver_path, options=chrome_options)

# check numbers
numbers = open('numbers.txt', 'r') 
number_lines = numbers.readlines() 
  
processed = open("processed.txt", "w+")
processed_lines = numbers.readlines() 

founded = open("found.txt", "w+")
count = 0
# Strips the newline character 
for number_line in number_lines:
    already_processed = False
    for processed_line in processed_lines: 
        if number_line.strip() == processed_line.strip():
            already_processed = True

    if not already_processed:
        process_num = number_line.strip()
        processed.write(process_num + '\n')

        # goTo
        browser.get('https://www2.trf4.jus.br/trf4/controlador.php?acao=consulta_processual_resultado_pesquisa&selForma=NU&txtValor=' + process_num + '&chkMostrarBaixados=&todasfases=&todosvalores=&todaspartes=&txtDataFase=01/01/1970&selOrigem=TRF&sistema=&hdnRefId=&txtPalavraGerada=&txtChave=&seq=')
        content = browser.find_element_by_id('divConteudo')
        response = process_num
        if 'Lei 13.463/2017' in browser.page_source:
            response += ' OK!'
            founded.write(process_num + ';\n')

        print(response)

numbers.close()
processed.close()