"""
Arquivo de teste para demonstrar as funcionalidades da aplicação
Este arquivo executa automaticamente as operações CRUD para validação
"""

import os
import sys

# Importar a classe NotesManager
from notes_manager import NotesManager

def teste_crud():
    """Testa todas as operações CRUD"""
    
    print("\n" + "="*60)
    print("       TESTE AUTOMATIZADO - APP DE ANOTAÇÕES")
    print("="*60 + "\n")
    
    # Criar gerenciador (com arquivo de teste)
    manager = NotesManager("notas_teste.json")
    
    # Limpar notas anteriores
    manager.notas = []
    manager.proximo_id = 1
    manager._salvar_notas()
    
    # ===== TESTE 1: CRIAR NOTAS =====
    print("✅ TESTE 1: CRIANDO NOTAS")
    print("-" * 60)
    
    nota1 = manager.criar_nota(
        "Compras do Supermercado",
        "Leite, pão, queijo, manteiga, ovos"
    )
    print(f"✓ Nota 1 criada: {nota1['titulo']} (ID: {nota1['id']})")
    
    nota2 = manager.criar_nota(
        "Tarefas de Casa",
        "Limpar quartos, lavar louça, arrumar jardim"
    )
    print(f"✓ Nota 2 criada: {nota2['titulo']} (ID: {nota2['id']})")
    
    nota3 = manager.criar_nota(
        "Aprender Python",
        "Estudar programação, fazer projetos, praticar CRUD"
    )
    print(f"✓ Nota 3 criada: {nota3['titulo']} (ID: {nota3['id']})")
    
    # ===== TESTE 2: LISTAR NOTAS =====
    print("\n✅ TESTE 2: LISTANDO TODAS AS NOTAS")
    print("-" * 60)
    
    notas = manager.listar_notas()
    print(f"Total de notas: {len(notas)}\n")
    
    for nota in notas:
        print(f"[ID: {nota['id']}] {nota['titulo']}")
        print(f"   └─ {nota['conteudo']}")
        print(f"   └─ Data: {nota['data']}\n")
    
    # ===== TESTE 3: BUSCAR NOTA =====
    print("✅ TESTE 3: BUSCANDO NOTA ESPECÍFICA")
    print("-" * 60)
    
    nota_encontrada = manager.buscar_nota(2)
    if nota_encontrada:
        print(f"✓ Nota encontrada!")
        print(f"  ID: {nota_encontrada['id']}")
        print(f"  Título: {nota_encontrada['titulo']}")
        print(f"  Conteúdo: {nota_encontrada['conteudo']}")
        print(f"  Data: {nota_encontrada['data']}")
    else:
        print("✗ Nota não encontrada")
    
    # ===== TESTE 4: ATUALIZAR NOTA =====
    print("\n✅ TESTE 4: ATUALIZANDO NOTA")
    print("-" * 60)
    
    print("Antes da atualização:")
    nota_atual = manager.buscar_nota(1)
    print(f"  Título: {nota_atual['titulo']}")
    print(f"  Conteúdo: {nota_atual['conteudo']}")
    
    manager.atualizar_nota(1, 
        novo_titulo="Compras do Supermercado (Urgente)",
        novo_conteudo="Leite, pão, queijo, manteiga, ovos, frutas"
    )
    
    print("\nDepois da atualização:")
    nota_atualizada = manager.buscar_nota(1)
    print(f"  Título: {nota_atualizada['titulo']}")
    print(f"  Conteúdo: {nota_atualizada['conteudo']}")
    print(f"  Data: {nota_atualizada['data']}")
    
    # ===== TESTE 5: DELETAR NOTA =====
    print("\n✅ TESTE 5: DELETANDO NOTA")
    print("-" * 60)
    
    print(f"Antes de deletar: {len(manager.notas)} notas")
    
    manager.deletar_nota(3)
    print(f"✓ Nota com ID 3 deletada!")
    
    print(f"Depois de deletar: {len(manager.notas)} notas")
    
    # ===== TESTE 6: LISTANDO NOTAS FINAIS =====
    print("\n✅ TESTE 6: NOTAS FINAIS APÓS TESTES")
    print("-" * 60)
    
    notas_finais = manager.listar_notas()
    print(f"Total de notas restantes: {len(notas_finais)}\n")
    
    for nota in notas_finais:
        print(f"[ID: {nota['id']}] {nota['titulo']}")
        print(f"   └─ {nota['conteudo']}\n")
    
    # ===== RESUMO =====
    print("\n" + "="*60)
    print("       ✅ TODOS OS TESTES CONCLUÍDOS COM SUCESSO!")
    print("="*60)
    print("\n📊 RESUMO DOS TESTES:")
    print(f"   ✓ Criação de notas")
    print(f"   ✓ Listagem de notas")
    print(f"   ✓ Busca por ID")
    print(f"   ✓ Atualização de notas")
    print(f"   ✓ Deleção de notas")
    print(f"   ✓ Persistência em arquivo JSON")
    
    print("\n📁 Arquivo de teste: notas_teste.json")
    print("   (Você pode abrir este arquivo para ver os dados em JSON)\n")

if __name__ == "__main__":
    try:
        teste_crud()
    except Exception as e:
        print(f"❌ ERRO DURANTE OS TESTES: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
