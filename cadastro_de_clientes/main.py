def cadastrar_cliente(nome, telefone, endereco):
    with open("leads.txt", "a") as arquivo:
        arquivo.write(f"{nome}, {telefone}, {endereco}\n")
    print("Cliente cadastrado com sucesso!")

def listar_clientes():
    try:
        with open("leads.txt", "r") as arquivo:
            clientes = arquivo.readlines()
            if not clientes:
                print("Nenhum cliente encontrado.")
            else:
                print("Lista de Clientes Cadastrados:")
                for cliente in clientes:
                    nome, telefone, endereco = cliente.strip().split(", ")
                    print(f"Nome: {nome}, Telefone: {telefone}, Endereco: {endereco}")
    except FileNotFoundError:
        print("Nenhum cliente cadastrado.")
        
def salvar_arquivo(dados, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        for dado in dados:
            arquivo.write(f"{dado}\n")
            
def ler_de_arquivo(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            return arquivo.readlines()
    except FileNotFoundError:
        return[]
        
        