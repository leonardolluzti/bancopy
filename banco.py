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
    
    def exbirSaldo(self, valor):
        consulta = 'SELECT saldo FROM conta WHERE numero LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))
        self.data = self.cursor.fetchone()
        print("R$ %s" % self.data)

    def depositar(self, valor1, valor2):
        consulta1 = 'SELECT saldo FROM conta WHERE numero LIKE ?'
        self.cursor.execute(consulta1, (f'%{valor1}%',))
        self.data = self.cursor.fetchone()
        print("Saldo anterior R$ %s" % self.data)
        numero = valor1
        saldo = float(self.data[0]) + float(valor2)
        consulta2 = 'UPDATE OR IGNORE conta SET saldo=? WHERE numero=?'
        self.cursor.execute(consulta2, (saldo, numero))
        self.conn.commit()
        consulta3 = 'SELECT saldo FROM conta WHERE numero LIKE ?'
        self.cursor.execute(consulta3, (f'%{valor1}%',))
        self.data = self.cursor.fetchone()
        print("Saldo atual R$ %s" % self.data)        

    def sacar(self, valor1, valor2):
        consulta1 = 'SELECT saldo FROM conta WHERE numero LIKE ?'
        self.cursor.execute(consulta1, (f'%{valor1}%',))
        self.data = self.cursor.fetchone()
        print("Saldo anterior R$ %s" % self.data)
        numero = valor1
        s1 = float(self.data[0])
        s2 = float(valor2)
        if (s1>=s2 and s2>0):
            saldo = s1 - s2
            consulta2 = 'UPDATE OR IGNORE conta SET saldo=? WHERE numero=?'
            self.cursor.execute(consulta2, (saldo, numero))
            self.conn.commit()
            consulta3 = 'SELECT saldo FROM conta WHERE numero LIKE ?'
            self.cursor.execute(consulta3, (f'%{valor1}%',))
            self.data = self.cursor.fetchone()
            print("Saldo atual R$ %s" % self.data)   
        else:
            print("Valor informado não é válido!")
    def transferir(self, agencia, conta2, tipo, valor):
        print("Transferência realizada com sucesso!")
        print("Dados da transferência:")
        print("Agência : " + agencia)
        print("Conta : " + conta2)
        if(tipo=='1'):
            print("Tipo : 1 - Conta Corrente")
        elif(tipo=='2'):
            print("Tipo : 2 - Conta Poupança")
        elif(tipo=='3'):
            print("Tipo : 3 - Conta Salário")
        else: 
            print("Tipo de conta não encontrado")

    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    banco = BancoDB('banco.db')
    menu = '0'
    while menu != '15':
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
        print ("| 11 - Exibir Saldo    |")
        print ("| 12 - Depositar       |")
        print ("| 13 - Sacar           |")
        print ("| 14 - Transferir      |")
        print ("========================")
        print ("| 15 - Sair do Banco   |")
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
            print("1 - Conta Corrente")
            print("2 - Conta Poupança")
            print("3 - Conta Salário")
            tipo = input("Digite o tipo de conta:  ")
            saldo = input("Digite o saldo: ")
            banco.inserirConta(agencia, numero, tipo, saldo, idCliente)
        elif menu == '9': 
            banco.listarConta()
            id = input("Digite o id: ")
            agencia = input("Digite a agencia: ")
            numero = input("Digite o numero da conta: ")
            print("Tipos de conta:")
            print("1 - Conta Corrente")
            print("2 - Conta Poupança")
            print("3 - Conta Salário")
            tipo = input("Digite o tipo de conta:  ")
            saldo = input("Digite o saldo: ")
            banco.editarConta(agencia, numero, tipo, saldo, id)
        elif menu == '10': 
            banco.listarConta()
            id = input("Digite o id da conta que deseja excluir: ")
            banco.excluirConta(id)
        elif menu == '11': 
            print("Saldo")
            print("=====")
            numero = input("Digite o numero da conta: ")
            banco.exbirSaldo(numero)
        # Depósito #
        elif menu == '12': 
            print("Depósito")
            print("========")
            numero = input("Digite o numero da conta: ")
            valor = input("Digite o valor do depósito: R$ ")
            banco.depositar(numero, valor)
        # Saque #
        elif menu == '13': 
            print("Saque")
            print("=====")
            numero = input("Digite o numero da conta: ")
            valor = input("Digite o valor do saque: R$ ")
            banco.sacar(numero, valor)
        # Transferêcia #
        elif menu == '14': 
            print("Transferêcia")
            print("============")
            conta1 = input("Digite o numero da conta de origem: ")
            agencia = input("Digite a agência da conta de destino: ")
            conta2 = input("Digite o numero da conta de destino: ")
            print("Tipos de conta:")
            print("1 - Conta Corrente")
            print("2 - Conta Poupança")
            print("3 - Conta Salário")
            tipo = input("Digite o tipo da conta de destino: ")
            valor = input("Digite o valor da transferência: R$ ")
            banco.sacar(conta1, valor)
            banco.depositar(conta2, valor)
            banco.transferir(agencia, conta2, tipo, valor)
        elif menu == '15': 
            banco.fechar()
            print ("Saiu do Banco - Volte Sempre!")