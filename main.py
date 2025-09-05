from database import setup_database, execute_sql_query
from ai_logic import generate_sql
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


# --- FUNÇÕES DO TELEGRAM BOT ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia uma mensagem de boas-vindas."""
    await update.message.reply_text('Olá! Eu sou um bot de estoque. Faça sua pergunta sobre produtos!')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Lida com as mensagens do usuário, processa com a IA e responde."""
    user_question = update.message.text
    
    # 1. Gera o SQL com a IA.
    sql_query = generate_sql(user_question)
    
    # 2. Limpa o SQL.
    start_index = sql_query.upper().find("SELECT")
    if start_index != -1:
        cleaned_sql = sql_query[start_index:].strip()
        if cleaned_sql.endswith(';'):
            cleaned_sql = cleaned_sql[:-1]
        sql_query = cleaned_sql
    else:
        await update.message.reply_text("Desculpe, não consegui gerar uma consulta SQL válida para a sua pergunta.")
        return

    # 3. Executa a consulta no banco de dados.
    cursor, db_result = execute_sql_query(sql_query)
    
    # 4. Formata a resposta para o usuário.
    if isinstance(db_result, str) and db_result.startswith("Erro"):
        response_text = "Desculpe, ocorreu um erro ao executar a consulta. Por favor, tente novamente com uma pergunta mais específica."
    elif not db_result:
        response_text = "Nenhum resultado encontrado para a sua busca."
    else:
        # Formata a resposta de forma mais genérica
        header = [description[0] for description in cursor.description]
        formatted_list = [", ".join(map(str, row)) for row in db_result]
        
        response_text = f"Resultado do banco de dados:\n"
        response_text += ", ".join(header) + "\n"
        response_text += "\n".join(formatted_list)
        
    await update.message.reply_text(response_text)

# --- EXECUÇÃO PRINCIPAL DO BOT ---

def main():
    """Inicia o bot."""
    TELEGRAM_BOT_TOKEN = "SEU_TOKEN_AQUI"  # Substitua pelo token do seu bot do telegram

    # Crie o banco de dados de estoque
    setup_database()
    
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("Bot rodando! Envie uma mensagem para ele no Telegram.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()