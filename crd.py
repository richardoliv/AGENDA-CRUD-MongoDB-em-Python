import pymongo
from bson.objectid import ObjectId

# Conectar ao MongoDB (localmente)
def conectar_banco():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["cruddb"]
    return db

# Operação para criar um novo contato
def criar_contato(db):
    nome = input("Digite o nome do contato: ")
    email = input("Digite o email do contato: ")
    telefone = input("Digite o telefone do contato: ")

    novo_contato = {"nome": nome, "email": email, "telefone": telefone}
    db.contatos.insert_one(novo_contato)
    print("Contato adicionado com sucesso!")

# Operação para listar todos os contatos
def listar_contatos(db):
    contatos = list(db.contatos.find())
    print("Lista de Contatos:")
    for contato in contatos:
        print(f"ID: {contato['_id']}, Nome: {contato['nome']}, Email: {contato['email']}, Telefone: {contato['telefone']}")

# Operação para atualizar um contato existente
def atualizar_contato(db):
    id_contato = input("Digite o ID do contato que deseja atualizar: ")
    nome = input("Digite o novo nome (ou deixe em branco para manter o mesmo): ")
    email = input("Digite o novo email (ou deixe em branco para manter o mesmo): ")
    telefone = input("Digite o novo telefone (ou deixe em branco para manter o mesmo): ")

    filtro = {"_id": ObjectId(id_contato)}
    dados_atualizados = {}

    if nome:
        dados_atualizados["nome"] = nome
    if email:
        dados_atualizados["email"] = email
    if telefone:
        dados_atualizados["telefone"] = telefone

    db.contatos.update_one(filtro, {"$set": dados_atualizados})
    print("Contato atualizado com sucesso!")

# Operação para deletar um contato existente
def deletar_contato(db):
    id_contato = input("Digite o ID do contato que deseja excluir: ")
    confirmacao = input("Tem certeza que deseja excluir este contato? (s/n): ")

    if confirmacao.lower() == 's':
        filtro = {"_id": ObjectId(id_contato)}
        db.contatos.delete_one(filtro)
        print("Contato excluído com sucesso!")

def main():
    db = conectar_banco()

    while True:
        print("\nEscolha uma opção:")
        print("1. Criar contato")
        print("2. Listar contatos")
        print("3. Atualizar contato")
        print("4. Deletar contato")
        print("5. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            criar_contato(db)
        elif opcao == '2':
            listar_contatos(db)
        elif opcao == '3':
            atualizar_contato(db)
        elif opcao == '4':
            deletar_contato(db)
        elif opcao == '5':
            break
        else:
            print("Opção inválida!")

    print("Encerrando o programa...")

if __name__ == "__main__":
    main()