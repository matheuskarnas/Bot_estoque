import os
import re
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
    - tipo (TEXT) - valores possíveis: 'Descartável', 'Limpeza', 'Higiene', 'Escritório'
    - quantidade (INTEGER)
    - preco (REAL)

    EXEMPLOS:
    Pergunta: "Lista todos os produtos"
    SQL: SELECT * FROM produtos;

    Pergunta: "Produtos de limpeza"
    SQL: SELECT * FROM produtos WHERE tipo = 'Limpeza';

    Pergunta: "Produtos com quantidade maior que 100"
    SQL: SELECT * FROM produtos WHERE quantidade > 100;

    Pergunta: "Produtos mais caros que 5 reais"
    SQL: SELECT * FROM produtos WHERE preco > 5.0;

    Pergunta: "Produtos que são sacos de lixo" ou "sacos de lixo"
    SQL: SELECT * FROM produtos WHERE nome_produto LIKE '%Saco%';

    Pergunta: "Produtos com nome contendo copo"
    SQL: SELECT * FROM produtos WHERE nome_produto LIKE '%Copo%';

    Pergunta: "Produtos do mais caro para o mais barato" ou "ordenar por preço decrescente"
    SQL: SELECT * FROM produtos ORDER BY preco DESC;

    Pergunta: "Produtos do mais barato para o mais caro" ou "ordenar por preço crescente"  
    SQL: SELECT * FROM produtos ORDER BY preco ASC;

    REGRAS IMPORTANTES: 
    - Para buscar por nome específico de produto, use LIKE '%palavra%'
    - Para ordenação, use ORDER BY sem LIMIT (a menos que seja explicitamente pedido apenas alguns itens)
    - DESC = decrescente (maior para menor), ASC = crescente (menor para maior)
    """
    model_name = os.getenv('OLLAMA_MODEL', 'qwen3:1.7b')
    try:
        response = ollama.chat(
            model=model_name,
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_question}
            ],
            options={'temperature': 0.0}
        )
        raw = response['message']['content']

        def extract_sql(text: str) -> str | None:
            if not text:
                return None
            # Remove code fences and common wrapper tags
            text = re.sub(r'```(?:sql)?', '', text, flags=re.IGNORECASE)
            text = re.sub(r'</?think>', '', text, flags=re.IGNORECASE)
            # Remove any markdown backticks
            text = text.replace('`', '')
            # Try to find the first SELECT ...; block
            m = re.search(r"(SELECT\b[\s\S]*?;)", text, re.IGNORECASE)
            if m:
                return m.group(1).strip()
            # If no semicolon, try to capture from SELECT to end of line/block
            m2 = re.search(r"(SELECT\b[\s\S]*)", text, re.IGNORECASE)
            if m2:
                return m2.group(1).strip()
            return None

        sql = extract_sql(raw)
        if sql:
            return sql

        # Retry once with a stricter instruction if model didn't return SQL
        retry_user = (
            "O modelo anterior não retornou apenas a consulta SQL.\n"
            "Responda APENAS com a consulta SQL válida para a pergunta a seguir, nada mais:\n\n"
            f"{user_question}"
        )
        response2 = ollama.chat(
            model=model_name,
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': retry_user}
            ],
            options={'temperature': 0.0}
        )
        raw2 = response2['message']['content']
        sql2 = extract_sql(raw2)
        if sql2:
            return sql2

        # Se ainda não houver SQL, retorna erro com parte da resposta para debug
        preview = (raw2 or raw or '')[:300]
        return f"Erro ao gerar SQL: modelo não retornou SQL. Resposta do modelo: {preview}"
    except Exception as e:
        return f"Erro ao gerar SQL: {e}"