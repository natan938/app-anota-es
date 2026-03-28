import json
import os
from datetime import datetime

class NotesManager:
    """Gerenciador de anotações com persistência em arquivo JSON"""
    
    def __init__(self, arquivo="notas.json"):
        """Inicializa o gerenciador de anotações"""
        self.arquivo = arquivo
        self._carregar_notas()
    
    def _carregar_notas(self):
        """Carrega as notas do arquivo (ou cria um arquivo vazio)"""
        if os.path.exists(self.arquivo):
            try:
                with open(self.arquivo, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                    self.notas = dados.get('notas', [])
                    self.proximo_id = dados.get('proximo_id', 1)
            except json.JSONDecodeError:
                self._inicializar_notas()
        else:
            self._inicializar_notas()
    
    def _inicializar_notas(self):
        """Inicializa uma nova lista de notas"""
        self.notas = []
        self.proximo_id = 1
        self._salvar_notas()
    
    def _salvar_notas(self):
        """Salva as notas no arquivo JSON"""
        dados = {
            'notas': self.notas,
            'proximo_id': self.proximo_id
        }
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)
    
    def criar_nota(self, titulo, conteudo):
        """Cria uma nova anotação"""
        nota = {
            'id': self.proximo_id,
            'titulo': titulo,
            'conteudo': conteudo,
            'data': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        }
        self.notas.append(nota)
        self.proximo_id += 1
        self._salvar_notas()
        return nota
    
    def listar_notas(self):
        """Retorna a lista de todas as anotações"""
        return self.notas
    
    def buscar_nota(self, nota_id):
        """Busca uma anotação por ID"""
        for nota in self.notas:
            if nota['id'] == nota_id:
                return nota
        return None
    
    def atualizar_nota(self, nota_id, novo_titulo=None, novo_conteudo=None):
        """Atualiza uma anotação existente"""
        for nota in self.notas:
            if nota['id'] == nota_id:
                if novo_titulo:
                    nota['titulo'] = novo_titulo
                if novo_conteudo:
                    nota['conteudo'] = novo_conteudo
                nota['data'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                self._salvar_notas()
                return nota
        return None
    
    def deletar_nota(self, nota_id):
        """Deleta uma anotação"""
        for i, nota in enumerate(self.notas):
            if nota['id'] == nota_id:
                self.notas.pop(i)
                self._salvar_notas()
                return True
        return False

