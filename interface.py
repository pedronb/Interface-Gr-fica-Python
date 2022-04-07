import PySimpleGUI as sg
import os

#sg.theme_previewer()
sg.theme('DarkBlue12')

layout = [
    [sg.Text('Criando a primeira janela')],
    [sg.Text('Nome completo:', size = (15,1)), sg.Input(key = 'Nome')],
    [sg.Text('Idade:', size = (15,1)), sg.Input(key = 'Idade')],
    [sg.Button('Cadastrar'), sg.Button('Cancelar')],
    [sg.Output(size = (50,15))]
]

janela = sg.Window('Cadastrando Usuários', layout)

while True:
    evento, valores = janela.read()
    nome = valores['Nome']
    idade = valores['Idade']
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break
    print('Cadastrado com Sucesso!')
    print(f'Nome: {nome}')
    print(f'Idade: {idade}')
    
    if not os.path.exists('usuarios_cadastrados.txt'):
        with open('usuarios_cadastrados.txt', 'w') as arquivo:
            arquivo.write(f'{"*"*7} USUARIOS CADASTRADOS {"*"*7}\n\n')
            arquivo.write(f'Nome: {nome}\n')
            arquivo.write(f'Idade: {idade}\n')
            arquivo.write('=========================\n')
    else:
        with open('usuarios_cadastrados.txt', 'a') as arquivo:
            arquivo.write(f'Nome: {nome}\n')
            arquivo.write(f'Idade: {idade}\n')
            arquivo.write('=========================\n')

janela.close()
