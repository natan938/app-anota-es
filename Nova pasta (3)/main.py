import os
from notes_manager import NotesManager

def menu():
    """Exibe o menu principal"""
    print("\n" + "="*50)
    print("       APP DE ANOTAÇÕES - GERENCIADOR DE NOTAS")
    print("="*50)
    print("1. Adicionar nova anotação")
    print("2. Listar todas as anotações")
    print("3. Buscar anotação por ID")
    print("4. Atualizar anotação")
    print("5. Deletar anotação")
    print("6. Limpar tela")
    print("0. Sair")
    print("="*50)
    return input("Escolha uma opção: ").strip()

def adicionar_nota(manager):
    """Adiciona uma nova anotação"""
    titulo = input("\nTítulo da anotação: ").strip()
    if not titulo:
        print("❌ Título não pode estar vazio!")
        return
    
    conteudo = input("Conteúdo da anotação: ").strip()
    if not conteudo:
        print("❌ Conteúdo não pode estar vazio!")
        return
    
    manager.criar_nota(titulo, conteudo)
    print("✅ Anotação adicionada com sucesso!")

def listar_notas(manager):
    """Lista todas as anotações"""
    notas = manager.listar_notas()
    
    if not notas:
        print("\n📝 Nenhuma anotação registrada ainda.")
        return
    
    print("\n" + "-"*50)
    print("LISTA DE ANOTAÇÕES")
    print("-"*50)
    for nota in notas:
        print(f"\n[ID: {nota['id']}] {nota['titulo']}")
        print(f"Conteúdo: {nota['conteudo']}")
        print(f"Data: {nota['data']}")
    print("\n" + "-"*50)

def buscar_nota(manager):
    """Busca uma anotação por ID"""
    try:
        nota_id = int(input("\nDigite o ID da anotação: ").strip())
        nota = manager.buscar_nota(nota_id)
        
        if nota:
            print("\n" + "-"*50)
            print(f"[ID: {nota['id']}] {nota['titulo']}")
            print(f"Conteúdo: {nota['conteudo']}")
            print(f"Data: {nota['data']}")
            print("-"*50)
        else:
            print("❌ Anotação não encontrada!")
    except ValueError:
        print("❌ ID inválido! Digite um número.")

def atualizar_nota(manager):
    """Atualiza uma anotação existente"""
    try:
        nota_id = int(input("\nDigite o ID da anotação a atualizar: ").strip())
        
        if not manager.buscar_nota(nota_id):
            print("❌ Anotação não encontrada!")
            return
        
        novo_titulo = input("Novo título (deixe em branco para manter): ").strip()
        novo_conteudo = input("Novo conteúdo (deixe em branco para manter): ").strip()
        
        manager.atualizar_nota(nota_id, novo_titulo, novo_conteudo)
        print("✅ Anotação atualizada com sucesso!")
    except ValueError:
        print("❌ ID inválido! Digite um número.")

def deletar_nota(manager):
    """Deleta uma anotação"""
    try:
        nota_id = int(input("\nDigite o ID da anotação a deletar: ").strip())
        
        if not manager.buscar_nota(nota_id):
            print("❌ Anotação não encontrada!")
            return
        
        confirmacao = input("Tem certeza? (s/n): ").strip().lower()
        if confirmacao == 's':
            manager.deletar_nota(nota_id)
            print("✅ Anotação deletada com sucesso!")
        else:
            print("❌ Deleção cancelada.")
    except ValueError:
        print("❌ ID inválido! Digite um número.")

def main():
    """Função principal"""
    manager = NotesManager()
    
    while True:
        opcao = menu()
        
        if opcao == "1":
            adicionar_nota(manager)
        elif opcao == "2":
            listar_notas(manager)
        elif opcao == "3":
            buscar_nota(manager)
        elif opcao == "4":
            atualizar_nota(manager)
        elif opcao == "5":
            deletar_nota(manager)
        elif opcao == "6":
            os.system("cls" if os.name == "nt" else "clear")
        elif opcao == "0":
            print("\n👋 Até logo!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
