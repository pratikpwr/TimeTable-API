import pandas as pd
from sqlalchemy import create_engine

# read CSV file

column_names = []

df = pd.read_csv('assets/csv_files/sitrc_comp_se_b.csv', header=0)
print(df)

# save to DB
engine = create_engine('sqlite:///data.DB')
with engine.connect() as connection, connection.begin():
    df.to_sql('csv', connection, if_exists='append', index=False)


