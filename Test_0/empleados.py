from langchain_ollama import ChatOllama  # ✅ Cambiado
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.agent_toolkits import create_sql_agent

# 1. Conexión a la base de datos PostgreSQL
db = SQLDatabase.from_uri("postgresql+psycopg2://admin:admin123@localhost:5432/anamucpro")

# 2. Configurar Ollama
llm = ChatOllama(model="llama3.2", temperature=0.7)

# 3. Crear el toolkit para SQL
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# 4. Crear el agente SQL
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    handle_parsing_errors=True
)

# 5. Consulta en lenguaje natural
query = "cuántos usuarios hay."
response = agent_executor.invoke({"input": query})
print(response["output"])