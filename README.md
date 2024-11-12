<h1> Automatização de Preenchimento de Formulário com Playwright e PyAutoGUI </h1>

Este projeto utiliza a biblioteca Playwright para automação de navegação em páginas da web e PyAutoGUI para simular ações de mouse. O código acessa um site de treinamento online, preenche um formulário e tira screenshots em várias etapas do processo.

<h2>Requisitos</h2>
Antes de executar o script, você precisa garantir que tenha as seguintes bibliotecas instaladas:

<ul>Playwright: Biblioteca para automação de navegação em páginas da web.</ul>
<ul>PyAutoGUI: Biblioteca para controlar o mouse e o teclado.</ul>
Você pode instalar as dependências executando:

bash
Copiar código
pip install playwright pyautogui
Além disso, o Playwright exige que você faça o download dos navegadores que ele utiliza. Para isso, execute o seguinte comando:

bash
Copiar código
python -m playwright install
Descrição do Código
O código realiza as seguintes ações:

Inicia o Navegador: O Playwright é usado para abrir o navegador Chromium em modo não-headless (com interface gráfica).
Acessa o site: O script acessa a página de um curso de Python na URL fornecida.
Interage com o Formulário:
O código preenche campos de texto como nome, email e telefone.
Ele utiliza o método locator do Playwright para interagir com elementos do formulário e o pyautogui para simular o movimento do mouse.
Tira Screenshots: O script tira capturas de tela em várias etapas para ilustrar o processo.
Submete o Formulário: Após preencher todos os campos, o formulário é submetido.
Como Usar
Execute o script: Após garantir que as dependências estão instaladas, você pode rodar o script com o seguinte comando:
bash
Copiar código
python script.py
Acompanhamento: O script irá abrir o navegador, preencher o formulário e tirar screenshots das etapas do processo. As imagens serão salvas no diretório onde o script está localizado com os seguintes nomes:
screenshot1.png
screenshot2.png
screenshot3.png
screenshot4.png
screenshot5.png
screenshot6.png
Exemplo de Execução
O navegador será aberto com a URL https://www.hashtagtreinamentos.com/curso-python.
O script irá clicar nos campos do formulário e preenchê-los com dados fictícios (nome: "Lira", email: "pythonimpressionador@gmail.com", telefone: "97788-5596").
A cada etapa, será gerada uma captura de tela mostrando o estado atual do formulário.
Ao final, o formulário será submetido.


Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.









