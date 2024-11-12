from playwright.sync_api import sync_playwright
import time
import pyautogui

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False) 
    pagina = navegador.new_page()
    pagina.goto("https://www.hashtagtreinamentos.com/curso-python")
    pagina.screenshot(path="screenshot1.png")
   
    pagina.locator('id=firstname').click()
    pagina.screenshot(path="screenshot2.png")
    time.sleep(5)
    pyautogui.click(1286,139)
    pyautogui.move(0,139)
    pyautogui.drag(0,196)

    pagina.fill('xpath=//*[@id="firstname"]', "Lira")
    pagina.screenshot(path="screenshot3.png")
    time.sleep(5)
    pagina.fill('xpath=//*[@id="email"]', "pythonimpressionador@gmail.com")
    pagina.screenshot(path="screenshot4.png")
    time.sleep(5)
    pagina.fill('xpath=//*[@id="phone"]', "97788-5596")
    pagina.screenshot(path="screenshot5.png")
    time.sleep(5)
    pagina.locator('id=_form_2475_submit').click()
    time.sleep(5)
    pagina.screenshot(path="screenshot6.png")
    time.sleep(5)
    

