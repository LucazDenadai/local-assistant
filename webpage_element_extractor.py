from selenium import webdriver

driver = webdriver.Chrome()  # Atualize conforme o driver que você possui instalado

# Abrir uma página e pegar elementos
driver.get("https://example.com")
elementos = driver.find_elements_by_tag_name('p')
for elemento in elementos:
    print(elemento.text)