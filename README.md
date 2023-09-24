# Login de usuário usando a biblioteca PySimpleGUI

Este código utiliza a biblioteca PySimpleGUI para criar uma interface gráfica de usuário (GUI) simples para uma tela de login. Vou explicar o código em detalhes, dividindo-o em detalhados e explicando os principais elementos e conceitos envolvidos.

## Importação da Biblioteca:

~~~Python
import PySimpleGUI
~~~
Aqui, estamos importando a biblioteca `PySimpleGUI`  para criar a interface gráfica do programa.

(O PySimpleGUI é uma biblioteca Python que permite a criação de interfaces gráficas de forma simples e intuitiva. Com ele, você pode desenvolver aplicativos com interfaces amigáveis, facilitando a interação do usuário com o software.)

## Definição do Tema :
~~~Python
PySimpleGUI.theme('Reddit')
~~~
Esta linha define o tema visual da interface gráfica como `Reddit`. PySimpleGUI oferece uma variedade de temas predefinidos para personalizar a aparência da GUI.

## Layout da Interface:
O layout da interface é definido como uma list, onde cada list interna representa uma linha de elementos da interface. Neste caso, temos quatro elementos principais:

- Um campo de texto para "Usuário" (com um campo de entrada associado).
- Um campo de texto para "Senha" (com um campo de entrada associado que exibe asteriscos para ocultar a senha).
- Uma caixa de seleção para "Salvar o login?".
- Um botão "Entrar".

## Criação da Janela: 
~~~Python
janela = PySimpleGUI.Window('Login', layout)
~~~
Aqui, estamos criando uma janela com o título `"Login"` e usando o layout definido anteriormente. Esta janela é a janela principal da aplicação.

## Ciclo de Eventos: 
~~~Python
while True:
    eventos, valores = janela.read()
~~~
Este while mantém a aplicação em execução e aguarda eventos da interface gráfica. Ele utiliza o método `read()` para obter os eventos e os valores dos elementos da interface.

## Tratamento de Eventos :
- Se o evento for `WINDOW_CLOSED`, isso significa que o usuário fechou a janela, então o loop é interrompido, encerrando a aplicação.
~~~Python
    if eventos == PySimpleGUI.PySimpleGUI.WINDOW_CLOSED:
        break    
~~~
- Se o evento para `Entrar`, o código verifica se os valores inseridos nos campos `'usuário'` e `'senha'` indicam `"Minfermis"` e `"123456"`, respectivamente. Se responderem, uma mensagem de boas-vindas é impressa.
~~~Python
    if eventos == 'Entrar':
        if valores['usuario'] == 'Minfermis' and valores ['senha'] == '123456':
            print('Bem-vindo!')
~~~

## Imagem da janela de Login:

![Alt LOgin](<Tela Login.jpg>)

## Resumo
Em resumo, este código cria uma interface gráfica de login simples usando a biblioteca PySimpleGUI e verifica se as credenciais fornecidas são de um usuário e senha em especifico. Se loga, exibe uma mensagem de boas-vindas. Caso contrário, a interface permanece aberta para mais tentativas.
