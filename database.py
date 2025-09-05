import sqlite3

def setup_database():
    """Cria e popula o banco de dados de produtos descartáveis."""
    conn = sqlite3.connect('descartaveis.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id_produto INTEGER PRIMARY KEY,
            nome_produto TEXT,
            tipo TEXT,
            quantidade INTEGER,
            preco REAL
        )
    ''')
    
    c.execute("DELETE FROM produtos")

    # Inserindo dados de exemplo com 50 produtos
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Copo Plástico', 'Descartável', 5000, 0.15)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Prato de Papel', 'Descartável', 2500, 0.30)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Talher de Plástico', 'Descartável', 3000, 0.20)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Guardanapo de Papel', 'Descartável', 10000, 0.05)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Copo de Isopor', 'Descartável', 4000, 0.18)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Canudo Plástico', 'Descartável', 8000, 0.08)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Embalagem de Marmita', 'Descartável', 1500, 1.25)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Pote de Plástico', 'Descartável', 2000, 0.70)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Saco de Lixo 15L', 'Limpeza', 500, 3.50)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Detergente', 'Limpeza', 200, 5.80)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Álcool em Gel 500ml', 'Higiene', 300, 12.00)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Máscara Descartável', 'Higiene', 2000, 0.75)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Luva de Procedimento', 'Higiene', 1000, 0.85)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Papel Toalha', 'Higiene', 800, 4.20)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Sabonete Líquido', 'Higiene', 150, 8.90)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Papel Higiênico Rolo', 'Higiene', 600, 1.50)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Touca Descartável', 'Higiene', 1200, 0.40)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Touca de Banho', 'Higiene', 500, 0.60)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Copo de Papel', 'Descartável', 7500, 0.25)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Pires de Plástico', 'Descartável', 1000, 0.45)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Fita Adesiva', 'Escritório', 80, 2.50)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Clipes de Papel', 'Escritório', 200, 1.80)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Esponja de Banho', 'Higiene', 100, 2.90)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Cotonetes', 'Higiene', 50, 6.70)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Lenço Umedecido', 'Higiene', 200, 4.50)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Toalha de Papel Bobina', 'Limpeza', 150, 15.00)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Sabão em Barra', 'Limpeza', 300, 3.20)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Saco de Lixo 30L', 'Limpeza', 400, 5.00)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Saco de Lixo 60L', 'Limpeza', 250, 7.50)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Água Sanitária', 'Limpeza', 180, 4.00)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Desinfetante', 'Limpeza', 160, 6.50)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Cera Líquida', 'Limpeza', 90, 10.00)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Limpador Multiuso', 'Limpeza', 220, 7.00)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Flanela de Limpeza', 'Limpeza', 120, 2.00)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Esponja de Limpeza', 'Limpeza', 280, 1.50)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Pá de Lixo', 'Limpeza', 40, 8.00)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Escova Sanitária', 'Limpeza', 60, 11.00)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Luvas de Borracha', 'Limpeza', 90, 6.00)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Dispenser Papel Toalha', 'Higiene', 15, 45.00)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Dispenser Sabonete Líquido', 'Higiene', 20, 35.00)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Saco de Lixo Hospitalar', 'Limpeza', 100, 9.50)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Pano Multiuso', 'Limpeza', 350, 2.50)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Lençol Descartável', 'Higiene', 300, 1.80)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Touca Cirúrgica', 'Higiene', 800, 0.50)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Álcool 70%', 'Higiene', 250, 8.50)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Sabão em Pó', 'Limpeza', 100, 12.00)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Lâmina de Barbear', 'Higiene', 40, 3.00)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Creme Dental', 'Higiene', 60, 5.00)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Escova de Dentes', 'Higiene', 80, 4.00)")
    c.execute("INSERT INTO produtos (nome_produto, tipo, quantidade, preco) VALUES ('Saco de Lixo 100L', 'Limpeza', 100, 10.00)")

    conn.commit()
    conn.close()

def execute_sql_query(query):
    """Executa a consulta SQL no banco de dados de estoque e retorna o resultado."""
    try:
        conn = sqlite3.connect('descartaveis.db')
        c = conn.cursor()
        c.execute(query)
        result = c.fetchall()
        return c, result
    except Exception as e:
        return None, f"Erro ao executar a consulta: {e}"