import PySimpleGUI


# Layout 
PySimpleGUI.theme('Reddit')
layout = [
    [PySimpleGUI.PySimpleGUI.Text('Usuário'), PySimpleGUI.PySimpleGUI.Input(key='usuario')],
    [PySimpleGUI.PySimpleGUI.Text('Senha'), PySimpleGUI.PySimpleGUI.Input(key='senha', password_char='*')],
    [PySimpleGUI.PySimpleGUI.Checkbox('Salvar o login?')],
    [PySimpleGUI.PySimpleGUI.Button('Entrar')]
]
# Janaela
janela =PySimpleGUI.PySimpleGUI.Window('Login', layout)

# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == PySimpleGUI.PySimpleGUI.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Minfermis' and valores ['senha'] == '123456':
            print('Bem-vindo!')
