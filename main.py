import sys
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

count = 0
# Strips the newline character 
for number_line in number_lines:
    already_processed = False
    
    processed = open("processed.txt", "a+")
    processed_lines = numbers.readlines() 
    for processed_line in processed_lines: 
        if number_line.strip() == processed_line.strip():
            already_processed = True

    if not already_processed:
        # goTo
        process_num = number_line.strip()
        cache = 'AoWZ&hdnRefId=59c123f6b15a945e56d932a09b009cce'
        url = 'https://www2.trf4.jus.br/trf4/controlador.php?acao=consulta_processual_resultado_pesquisa&txtPalavraGerada=' + cache + '&selForma=NU&txtValor=' + process_num + '&chkMostrarBaixados=&todasfases=&todosvalores=&todaspartes=&txtDataFase=&selOrigem=TRF&sistema=&codigoparte=&txtChave=&paginaSubmeteuPesquisa=letras'
        browser.get(url)
        content = browser.find_element_by_id('divConteudo')
        response = process_num
        if 'Lei 13.463/2017' in browser.page_source:
            response += ' OK!'
            content = browser.find_element_by_id('divConteudo').text

            lines = ['Originário:', 'Originário:', 'Data de autuação:', 'Relator:', 'Órgão Julgador:', 'Órgão Atual:' , 'Situação:', 'Competência:', 'REQUERENTE:', 'Advogado:', 'REQUERIDO:']
            text = process_num + ';'
            for content_line in content.splitlines():
                for line in lines:
                    if line in content_line:
                        text += content_line.strip() + ';'                        
                        
            founded = open("found.txt", "a+")
            founded.write(text + '\n')
            founded.close()

        print(response)

        if 'Digite as letras no campo abaixo e clique em ' in browser.page_source:
            print('Stoped by captcha!')
            print(url)
            processed.close()        
            numbers.close()
            processed.close()
            sys.exit()
    
    processed.write(process_num + '\n')
    processed.close()

numbers.close()
processed.close()