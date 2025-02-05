"""
Wellington Pereira Luiz - UTF8 - pt-br
- Tkinter: model.py
JSON - JavaScript Object Notation
"""

import os
import json
import regex as re
from tkinter import messagebox

# Função para validar campos de entrada (Nome e Sobrenome)
def valida_campo(campo, tipo_campo):
    if not campo:
        messagebox.showwarning('Aviso', f'{tipo_campo} inválido.')
        return False
    if len(campo) > 50:
        messagebox.showwarning('Aviso', f'{tipo_campo} muito longo. Deve ter no máximo 50 caracteres.')
        return False

    pattern = r'^[\p{L}\s]{1,50}$'
    if not re.match(pattern, campo):
        messagebox.showwarning('Aviso', f'{tipo_campo} inválido. Não use números ou caracteres especiais.')
        return False

    preposicoes = ['da', 'de', 'do', 'das', 'dos']
    campo = ' '.join([parte.capitalize() if parte not in preposicoes else parte for parte in re.sub(r'\s+', ' ', campo).split()])
    return campo

# Função para carregar os dados do arquivo JSON
def carregar_dados_arquivo():
    arquivo_json = "cadastro.json"
    
    if os.path.exists(arquivo_json) and os.path.getsize(arquivo_json) > 0:
        with open(arquivo_json, 'r', encoding="utf-8") as arquivo:
            try:
                dados = json.load(arquivo)

                # Verifica se os dados carregados são uma lista de dicionários
                if isinstance(dados, list) and all(isinstance(item, dict) for item in dados):
                    return dados
                elif isinstance(dados, dict):
                    return [dados]  # Se for um único dicionário, converte para lista
                else:
                    return []  # Retorna lista vazia se o formato for inválido

            except json.JSONDecodeError:
                return []  # Se o JSON estiver corrompido, retorna lista vazia
    return []

# Função para salvar novos dados no arquivo JSON
def salvar_dados_arquivo(dados):
    arquivo_json = "cadastro.json"
    
    with open(arquivo_json, 'w', encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

