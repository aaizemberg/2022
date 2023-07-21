from fastapi import FastAPI
import duckdb

def duckdb_connect():
    return duckdb.connect(database=':memory:')

conn = duckdb_connect();
app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/al_count")
def al_count():
    return  { "rows" : conn.execute("SELECT count(*) from read_parquet('../data/vast/activity_logs/ParticipantStatusLogs*.parquet');").fetchone()[0] }

@app.get("/al_cmode_count")
def al_cmode_count():
    query= """
          SELECT currentMode, count(*) 
          from read_parquet('../data/vast/activity_logs/ParticipantStatusLogs*.parquet') 
          group by 1;
          """
    return conn.execute(query).fetchall()

@app.get("/fj_wage_by_month")
def fj_wage_by_month():
    query= """
    select date_trunc('month', timestamp), sum(amount) 
    from '../data/vast/journals/FinancialJournal.parquet' 
    where category = 'Wage' group by 1 order by 1;
    """
    return conn.execute(query).fetchall()