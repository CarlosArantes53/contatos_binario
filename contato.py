import pickle

class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

def salvar_contatos(contatos, arquivo):
    with open(arquivo, 'wb') as f:
        pickle.dump(contatos, f)

def carregar_contatos(arquivo):
    try:
        with open(arquivo, 'rb') as f:
            contatos = pickle.load(f)
    except FileNotFoundError:
        contatos = []
    return contatos

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    return Contato(nome, telefone, email)

def mostrar_contatos(contatos):
    Nome: {contato.nome}, Telefone: {contato.telefone}, E-mail: {contato.email}"

def main():
    arquivo_contatos = 'contatos.bin'
    contatos = carregar_contatos(arquivo_contatos)

    novo_contato = adicionar_contato()
    contatos.append(novo_contato)
    mostrar_contatos(contatos)

if __name__ == "__main__":
    main()
