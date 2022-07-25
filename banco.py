# Banco do Python
import sqlite3


class BancoDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserirCli(self, nome, cpf, email):
        consulta = 'INSERT OR IGNORE INTO cliente (nome, cpf, email) VALUES (?, ?, ?)'
        self.cursor.execute(consulta, (nome, cpf, email))
        self.conn.commit()

    def editarCli(self, nome, cpf, email, id):
        consulta = 'UPDATE OR IGNORE cliente SET nome=?, cpf=?, email=? WHERE id=?'
        self.cursor.execute(consulta, (nome, cpf, email, id))
        self.conn.commit()

    def excluirCli(self, id):
        consulta = 'DELETE FROM cliente WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listarCli(self):
        self.cursor.execute('SELECT * FROM cliente')

        for linha in self.cursor.fetchall():
            print(linha)

    def buscarCli(self, valor):
        consulta = 'SELECT * FROM cliente WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def inserirConta(self, agencia, numero, tipo, saldo, idCliente):
        consulta = 'INSERT OR IGNORE INTO conta (agencia, numero, tipo, saldo, idCliente) VALUES (?, ?, ?, ?, ?)'
        self.cursor.execute(consulta, (agencia, numero, tipo, saldo, idCliente))
        self.conn.commit()

    def editarConta(self, agencia, numero, tipo, saldo, id):
        consulta = 'UPDATE OR IGNORE conta SET agencia=?, numero=?, tipo=?, saldo=? WHERE id=?'
        self.cursor.execute(consulta, (agencia, numero, tipo, saldo, id))
        self.conn.commit()

    def excluirConta(self, id):
        consulta = 'DELETE FROM conta WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listarConta(self):
        self.cursor.execute('SELECT * FROM conta')

        for linha in self.cursor.fetchall():
            print(linha)

    def buscarConta(self, valor):
        consulta = 'SELECT * FROM conta WHERE numero LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    banco = BancoDB('banco.db')
    menu = '0'
    while menu != '11':
        print ("========================")        
        print ("| 1 - Mostrar Clientes |")
        print ("| 2 - Buscar Cliente   |")
        print ("| 3 - Inserir Cliente  |")
        print ("| 4 - Editar Cliente   |")
        print ("| 5 - Excluir Cliente  |")
        print ("========================")
        print ("| 6 - Mostrar Contas   |")
        print ("| 7 - Buscar Conta     |")
        print ("| 8 - Inserir Conta    |")
        print ("| 9 - Editar Conta     |")
        print ("| 10 - Excluir Conta   |")
        print ("========================")
        print ("| 11 - Sair do Banco   |")
        print ("========================")
        menu = input("Digite uma opção: ")
        # Operações com clientes: #
        if menu == '1': 
            banco.listarCli()
        elif menu == '2': 
            nome = input("Digite um nome: ")
            banco.buscarCli(nome)            
        elif menu == '3': 
            nome = input("Digite o nome: ")
            cpf = input("Digite o cpf: ")
            email = input("Digite o e-mail: ")
            banco.inserirCli(nome, cpf, email)
        elif menu == '4': 
            banco.listarCli()
            id = input("Digite o id: ")
            nome = input("Digite o nome: ")
            cpf = input("Digite o cpf: ")
            email = input("Digite o e-mail: ")
            banco.editarCli(nome, cpf, email, id)
        elif menu == '5': 
            banco.listarCli()
            id = input("Digite o id do cliente que deseja excluir: ")
            banco.excluirCli(id)
        # Operações com Contas: #
        elif menu == '6': 
            banco.listarConta()
        elif menu == '7': 
            numero = input("Digite o numero da conta: ")
            banco.buscarConta(numero)            
        elif menu == '8': 
            nome = input("Digite um nome: ")
            banco.buscarCli(nome)
            idCliente = input("Digite o id do cliente: ")
            agencia = input("Digite a agencia: ")
            numero = input("Digite o numero da conta: ")
            print("Tipos de conta:")
            print("1 - Conta Corrente:")
            print("2 - Conta Poupança:")
            print("3 - Conta Salário:")
            tipo = input("Digite o tipo de conta:  ")
            saldo = input("Digite o saldo: ")
            banco.inserirConta(agencia, numero, tipo, saldo, idCliente)
        elif menu == '9': 
            banco.listarConta()
            id = input("Digite o id: ")
            agencia = input("Digite a agencia: ")
            numero = input("Digite o numero da conta: ")
            print("Tipos de conta:")
            print("1 - Conta Corrente:")
            print("2 - Conta Poupança:")
            print("3 - Conta Salário:")
            tipo = input("Digite o tipo de conta:  ")
            saldo = input("Digite o saldo: ")
            banco.editarConta(agencia, numero, tipo, saldo, id)
        elif menu == '10': 
            banco.listarConta()
            id = input("Digite o id da conta que deseja excluir: ")
            banco.excluirConta(id)
        elif menu == '11': 
            banco.fechar()
            print ("Saiu do Banco - Volte Sempre!")