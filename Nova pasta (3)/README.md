# 📝 App de Anotações - Seu Primeiro CRUD

Uma aplicação simples e intuitiva para gerenciar suas anotações usando Python, com armazenamento em arquivos JSON.

## 🚀 Características

- ✅ **Criar** novas anotações com título e conteúdo
- ✅ **Listar** todas as anotações salvas
- ✅ **Buscar** anotações por ID
- ✅ **Atualizar** anotações existentes
- ✅ **Deletar** anotações
- ✅ Armazenamento persistente em JSON
- ✅ Data e hora automática de criação/atualização

## 📋 Requisitos

- Python 3.6+

## 🎯 Como Usar

### 1. Executar a aplicação

```bash
python main.py
```

### 2. Menu Principal

Após iniciar, você verá um menu com as seguintes opções:

```
1. Adicionar nova anotação
2. Listar todas as anotações
3. Buscar anotação por ID
4. Atualizar anotação
5. Deletar anotação
6. Limpar tela
0. Sair
```

### 3. Exemplos de Uso

#### Adicionar uma anotação
```
Escolha uma opção: 1
Título da anotação: Supermercado
Conteúdo da anotação: Comprar leite, pão, queijo
✅ Anotação adicionada com sucesso!
```

#### Listar anotações
```
Escolha uma opção: 2
LISTA DE ANOTAÇÕES
[ID: 1] Supermercado
Conteúdo: Comprar leite, pão, queijo
Data: 26/03/2026 10:30:45
```

#### Buscar anotação
```
Escolha uma opção: 3
Digite o ID da anotação: 1
[ID: 1] Supermercado
Conteúdo: Comprar leite, pão, queijo
Data: 26/03/2026 10:30:45
```

#### Atualizar anotação
```
Escolha uma opção: 4
Digite o ID da anotação a atualizar: 1
Novo título (deixe em branco para manter):
Novo conteúdo (deixe em branco para manter): Comprar leite, pão, queijo, manteiga
✅ Anotação atualizada com sucesso!
```

#### Deletar anotação
```
Escolha uma opção: 5
Digite o ID da anotação a deletar: 1
Tem certeza? (s/n): s
✅ Anotação deletada com sucesso!
```

## 📁 Arquivos do Projeto

- **main.py** - Interface CLI (Command Line Interface) da aplicação
- **notes_manager.py** - Classe que gerencia as operações CRUD e persistência em arquivo
- **notas.json** - Arquivo de armazenamento das anotações (criado automaticamente)

## 💾 Formato do Arquivo JSON

As anotações são armazenadas em `notas.json` com o seguinte formato:

```json
{
  "notas": [
    {
      "id": 1,
      "titulo": "Supermercado",
      "conteudo": "Comprar leite, pão, queijo",
      "data": "26/03/2026 10:30:45"
    }
  ],
  "proximo_id": 2
}
```

## 🔧 Estrutura do Código

### NotesManager (notes_manager.py)

Classe responsável por gerenciar todas as operações:

- `criar_nota(titulo, conteudo)` - Cria uma nova anotação
- `listar_notas()` - Retorna todas as anotações
- `buscar_nota(nota_id)` - Busca uma anotação pelo ID
- `atualizar_nota(nota_id, novo_titulo, novo_conteudo)` - Atualiza uma anotação
- `deletar_nota(nota_id)` - Deleta uma anotação

## 📚 Conceitos Aprendidos

Este projeto fornece prática com:

- ✅ Manipulação de arquivos JSON em Python
- ✅ Funções e classes
- ✅ CRUD (Create, Read, Update, Delete)
- ✅ Tratamento de exceções
- ✅ Interface CLI interativa
- ✅ Persistência de dados

## 🎓 Próximos Passos

Para expandir esse projeto, você pode:

1. Adicionar categorias/tags às anotações
2. Implementar busca por palavra-chave
3. Criar interface com GUI (usando tkinter)
4. Adicionar exportação para PDF
5. Implementar sincronização com banco de dados



Este projeto é de código aberto e livre para usar e modificar!
