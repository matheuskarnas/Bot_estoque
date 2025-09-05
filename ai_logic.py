import ollama

def generate_sql(user_question):
    """Gera uma consulta SQL com a IA (Ollama/Qwen) para o banco de estoque."""
    system_prompt = """
    Você é um tradutor de linguagem natural para SQL.
    Sua única função é converter a pergunta do usuário para uma consulta SQL válida.
    NÃO adicione explicações, texto adicional, formatação extra ou qualquer outra coisa.
    Sua resposta deve ser APENAS a consulta SQL.

    O banco de dados tem a seguinte tabela e colunas:

    Tabela 'produtos':
    - id_produto (INTEGER, CHAVE PRIMÁRIA)
    - nome_produto (TEXT)
    - tipo (TEXT)
    - quantidade (INTEGER)
    - preco (REAL)
    """
    try:
        response = ollama.chat(
            model='qwen',
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_question}
            ]
        )
        return response['message']['content']
    except Exception as e:
        return f"Erro ao gerar SQL: {e}"