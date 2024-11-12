<h1 align="center">Automatização de Preenchimento de Formulário com Playwright e PyAutoGUI</h1>

<p align="center">
    Este projeto utiliza a biblioteca <strong>Playwright</strong> para automação de navegação em páginas da web e <strong>PyAutoGUI</strong> para simular ações de mouse. O código acessa um site de treinamento online, preenche um formulário e tira screenshots em várias etapas do processo.
</p>

<h2>Requisitos</h2>

<p>Antes de executar o script, você precisa garantir que tenha as seguintes bibliotecas instaladas:</p>

<ul>
    <li><strong>Playwright</strong>: Biblioteca para automação de navegação em páginas da web.</li>
    <li><strong>PyAutoGUI</strong>: Biblioteca para controlar o mouse e o teclado.</li>
</ul>

<p>Você pode instalar as dependências executando:</p>

<pre>
<code>pip install playwright pyautogui</code>
</pre>

<p>Além disso, o Playwright exige que você faça o download dos navegadores que ele utiliza. Para isso, execute o seguinte comando:</p>

<pre>
<code>python -m playwright install</code>
</pre>

<h2>Descrição do Código</h2>

<p>O código realiza as seguintes ações:</p>

<ol>
    <li><strong>Inicia o Navegador</strong>: O Playwright é usado para abrir o navegador Chromium em modo não-headless (com interface gráfica).</li>
    <li><strong>Acessa o site</strong>: O script acessa a página de um curso de Python na URL fornecida.</li>
    <li><strong>Interage com o Formulário</strong>:
        <ul>
            <li>O código preenche campos de texto como nome, email e telefone.</li>
            <li>Ele utiliza o método <code>locator</code> do Playwright para interagir com elementos do formulário e o <code>pyautogui</code> para simular o movimento do mouse.</li>
        </ul>
    </li>
    <li><strong>Tira Screenshots</strong>: O script tira capturas de tela em várias etapas para ilustrar o processo.</li>
    <li><strong>Submete o Formulário</strong>: Após preencher todos os campos, o formulário é submetido.</li>
</ol>

<h2>Como Usar</h2>

<ol>
    <li><strong>Execute o script</strong>: Após garantir que as dependências estão instaladas, você pode rodar o script com o seguinte comando:</li>
</ol>

<pre>
<code>python script.py</code>
</pre>

<ol start="2">
    <li><strong>Acompanhamento</strong>: O script irá abrir o navegador, preencher o formulário e tirar screenshots das etapas do processo. As imagens serão salvas no diretório onde o script está localizado com os seguintes nomes:</li>
</ol>

<ul>
    <li><code>screenshot1.png</code></li>
    <li><code>screenshot2.png</code></li>
    <li><code>screenshot3.png</code></li>
    <li><code>screenshot4.png</code></li>
    <li><code>screenshot5.png</code></li>
    <li><code>screenshot6.png</code></li>
</ul>

<h2>Exemplo de Execução</h2>

<p>- O navegador será aberto com a URL <code>https://www.hashtagtreinamentos.com/curso-python</code>.</p>
<p>- O script irá clicar nos campos do formulário e preenchê-los com dados fictícios (nome: "Lira", email: "pythonimpressionador@gmail.com", telefone: "97788-5596").</p>
<p>- A cada etapa, será gerada uma captura de tela mostrando o estado atual do formulário.</p>
<p>- Ao final, o formulário será submetido.</p>













