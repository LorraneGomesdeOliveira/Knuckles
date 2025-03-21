import os
restaurantes=[{'nome': 'Knuckles secreto', 'categoria': 'Secreto', 'ativo':True},
              {'nome': 'Tails Fox', 'categoria': 'Doce', 'ativo':False},
              {'nome': 'Shadow chá', 'categoria': 'Chá', 'ativo':False}
              ]
def exibir_nome_do_programa():
    print ("""""
█▀ █▀█ █▄░█ █ █▀▀ ▀ █▀   █▀▀ ▄▀█ █▀█ █▀▄ █▀▀ █▄░█ █▀
▄█ █▄█ █░▀█ █ █▄▄ ░ ▄█   █▄█ █▀█ █▀▄ █▄▀ ██▄ █░▀█ ▄█\n""")

def exibir_opções():
    print('1- Cadastrar restaurante')
    print('2- Listar restaurante')
    print('3- Ativar restaurante')
    print('4- Sair\n')

def Encerrando_programa():
    exibir_subtitulo('Encerrando o programa')
    voltar_ao_menu_principal()
    
def voltar_ao_menu_principal():
  input('\nDigite uma tecla para voltar ao menu principal ')
  main()

def opcao_invalida():
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()
    
def exibir_subtitulo(texto):
  os.system('cls')
  print(texto)
  print()

def cadastrar_novo_restaurante():
  exibir_subtitulo('Cadastro de novos restaurantes')
  nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:')
  restaurantes.append(nome_do_restaurante)
  print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
  voltar_ao_menu_principal()
  
def listar_restaurantes():
  exibir_subtitulo('Listando os restaurantes') 
  
  for restaurante in restaurantes:
      nome_restaurante = restaurante['nome']
      print(f' - {nome_restaurante}')
  voltar_ao_menu_principal()
    
def escolher_opcao():
    try:
      opcao_escolhida= int(input('Escolha uma opção: '))
      print (f'Você escolheu a opção: {opcao_escolhida}\n')

      if opcao_escolhida == 1:
        cadastrar_novo_restaurante()
      elif opcao_escolhida == 2:
        listar_restaurantes()
      elif opcao_escolhida == 3:
        print('Ativar restaurantes')
      elif opcao_escolhida == 4:
        Encerrando_programa()
      else:
       opcao_invalida()
    except:
        opcao_invalida()
        
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opções()
    escolher_opcao()

if __name__ == '__main__':
    main()
    