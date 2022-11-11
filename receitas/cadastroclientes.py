class Menu:
    def __init__(self, resposta):
         return self.resposta
class Cliente:
    def __init__(self):
        self.usuarios = {}

    def cadastro_cliente(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.usuarios(nome = [cpf, idade])
        new_var = self.usuarios
        return print(new_var)
    
    def descadastro_cliente(self, nome_excluir): 
        self.nome_excluir = nome_excluir
        if self.nome_excluir in self.usuarios.keys():
            self.usuarios.pop(self.nome_excluir)
            old_var = self.usuarios
            print(old_var)
        elif self.nome_excluir not in self.usuarios:
            return print('O cliente que você busca ainda não foi cadastrado')
           
            

    def pesquisar_ciente(self, nome_pesquisa):
        self.nome_pesquisa = nome_pesquisa
        if self.nome_pesquisa not in self.usuarios:
            print('O cliente que você busca ainda não foi cadastrado')
        else:
            self.usuarios.get(self.nome_pesquisa)
            mostrar_cpf = self.usuarios[self.nome_pesquisa][0]
            mostar_idade = self.usuarios[self.nome_pesquisa][1]
            print(f'O CPF de cliente do {self.nome_pesquisa} é {mostrar_cpf} e a idade dele é { mostar_idade}')
        
        
        
id =  1
print('Bem vidndo ao seu programa de cadastro e edição de usuários')
print()
finalizar = False
while not finalizar:        
    print('Quais das opções você deseja:')
    x = int(input('[1] CADASTRAR NOVO CLIENTE /n [2] PESQUISAR ALGUM CLIENTE /n [3] EXCLUIR /n [4] ENCERRAR O PROGRAMA'))
    if x == 4:
        finalizar = True
    elif x  == 1:
        dados_nome = input('Digite o seu Nome : ').upper()
        dados_cpf = input('Digite o seu CPF : ')
        dados_idade = input('Digite a sua idade: ')
        novo_cliente = Cliente
        novo_cliente.cadastro_cliente(dados_nome, dados_cpf, dados_idade)
        print('Clientee cadastrado com sucesso.')
    elif x  == 2:
        novo_nome_pesquisa = input('Digite o nome que você desejapesquisar').upper()
        var = Cliente
        var.pesquisar_ciente(novo_nome_pesquisa)
    elif x == 3:
        novo_nome_excluir = input('Digite o nome do cliente que você deseja excluir: ').upper()
        a_excluir = Cliente
        a_excluir.descadastro_cliente(novo_nome_excluir)