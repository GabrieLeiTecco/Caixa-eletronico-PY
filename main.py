class CaixaEletronico: # Cria a classe do caixa eletronico
    def __init__(self): # Essa é a função que acontece sempre que o projeto é iniciado
        self.contas = ['Jose', 'Carlos', 'Ana'] # ela cria essas informações dentro da classe
        self.saldo = [1000, 1500, 2000] # "self" é pra falar que é uma caracterista da classe CaixaEletronico
        self.notas = [0, 0, 0, 0, 0, 0] # não só uma variavel normal

    def verifiConta(self): # Funcão que verifica se a conta já existe ou não
        nomeConta = input("Digite o seu nome: ")
        contaExiste = False
        for i in range(len(self.contas)): # for que vai de posição em posição do vetor/matriz contas que foi criado ali em cima
            if nomeConta == self.contas[i]: # e verifica se o nome que a pessa colocou consta como uma conta ja inserida no vetor
                self.operacao(nomeConta) # Se tem, ele executa a funcao operação para continuar o processo
                break
            else: # se nao, ele coloca a variavel boolean como "False"
                contaExiste = False
        if contaExiste == False: # e caso a variavel seja falsa, executa a func que cria uma conta
            print("Você não possui conta, vamos criar uma pra você")
            self.criarConta() # chama a funcao criarConta com o nome da conta sendo o parametro

    
    def operacao(self, conta): # funcao das operacoes como sacar depositar etc, tipo um menu inicial
            nomeConta = conta # "conta" vai ser fornecido por outra funcao
            oper = input("O que você quer fazer? (sacar, depositar, criar conta ou ver saldo) ").lower() #recebe a operação que usuario quer fazer
            if oper == "sacar":
                self.sacar(nomeConta) #chama a função sacar ("self" para mostrar que é uma funcao da classe CaixaEletronico)
            elif oper == "depositar":
                self.depositar(nomeConta) # envia como parametro o nome da conta da pessoa
            elif oper == "criar conta":
                self.criarConta()
            elif oper == "ver saldo":
                self.verSaldo(nomeConta)
            else: # caso a pessoa digite algo que não é uma das opções
                print("sacar, depositar, criar conta ou ver saldo.")
                self.operacao(nomeConta)

    def sacar(self, conta): # função sacar
        for i in range(len(self.contas)): # for que verifica qual a conta que o dinheiro  vai ser sacado
            if conta == self.contas[i]:
                saldo = self.saldo[i]
                valor = int(input("Quanto você quer sacar? ")) # recebe o valor do saque
                if valor <= saldo: # verifica se o saldo da pessoa é maior ou igual ao saque
                    self.saldo[i] = saldo - valor # se for, subtrai o valor do saque no saldo
                    print("Seu saldo ficou: ", self.saldo[i])
                    return self.fazerMais() # e retorna a função que pergunta se a pessoa quer fazer mais algo
                else: # se o saldo for menor que o valor
                    print("Você não tem saldo o suficiente.") # retorna a mensagem, e a função de fazer mais algo
                    return self.fazerMais()
            else:
                pass

    def depositar(self, conta): # função depositar
        for i in range(len(self.contas)): # for que blablabla
            if conta == self.contas[i]:
                conta = self.contas[i]
                saldo = self.saldo[i]
                valor = int(input("Quanto você quer depositar? "))
                self.saldo[i] = saldo + valor # adiciona o valor ao saldo da pessoa
                print("Seu saldo agora é: ", self.saldo[i])
                return self.fazerMais()
            else:
                pass

    def criarConta(self): # função criar conta
        nome = input("Insira seu nome para a criação da conta: ")
        self.contas.append(nome) # adiciona o nome na lista de contas
        self.saldo.append(0) # adiciona o saldo 0 na mesma posição da conta
        print("Sua conta foi criada, "+nome+"!")
        print("Seu saldo é de: ", 0)
        self.fazerMais()

    def verSaldo(self, conta): # Função ver saldo
        for i in range(len(self.contas)):
            if conta == self.contas[i]:
                print("Seu saldo atual é: ", self.saldo[i]) # mostra o saldo da posição igual ao do nome da conta
                self.fazerMais()
            else:
                pass

    def fazerMais(self): # função fazer mais algo
        resp = input("Quer fazer algo mais? ").lower()
        if resp == "sim": # se a resposta for "sim" ele chama a função inicial
            return self.verifiConta()
        elif resp == "nao": # se for não, ele fecha
            print("Okay, tchau!")
            quit()
        else: # se for outra, ele simplesmente repete
            return self.fazerMais()

caixa = CaixaEletronico().verifiConta()
