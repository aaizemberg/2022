from fastapi import FastAPI
import duckdb

def duckdb_connect():
    return duckdb.connect(database=":memory:")

# Crear la conexión y cargar los datos
conn = duckdb_connect()

def load_data():
    # Cargar datos en memoria desde los archivos Parquet
    conn.execute("""
        CREATE OR REPLACE TABLE participant_status_logs AS
        SELECT * FROM read_parquet('../data/vast/activity_logs/ParticipantStatusLogs*.parquet');
    """)
    conn.execute("""
        CREATE OR REPLACE TABLE financial_journal AS
        SELECT * FROM read_parquet('../data/vast/journals/FinancialJournal.parquet');
    """)

# Cargar los datos al iniciar
load_data()

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/al_count")
def al_count():
    query = "SELECT count(*) FROM participant_status_logs;"
    return {"rows": conn.execute(query).fetchone()[0]}

@app.get("/al_cmode_count")
def al_cmode_count():
    query = """
        SELECT currentMode, count(*) 
        FROM participant_status_logs
        GROUP BY currentMode;
    """
    return conn.execute(query).fetchall()

@app.get("/fj_wage_by_month")
def fj_wage_by_month():
    query = """
        SELECT date_trunc('month', timestamp) AS month, sum(amount) AS total_wage
        FROM financial_journal
        WHERE category = 'Wage'
        GROUP BY month
        ORDER BY month;
    """
    return conn.execute(query).fetchall()
