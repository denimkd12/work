import pandas as pd
import pyodbc
import streamlit as st


conn1 = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=strumica_sql;"
                      "Database=TPDM-TSF;"
                      "Trusted_Connection=yes;")

df1 = pd.read_sql_query('SELECT com_code,code FROM c_plans where state=1', conn1)

conn2 = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=loznica_sql;"
                      "Database=TPDM-TSF;"
                      "Trusted_Connection=yes;")

df2 = pd.read_sql_query('SELECT com_code,code FROM c_plans where state=1', conn2)



st.title('Cutman Active Workshop!')
data1 = pd.DataFrame(df1)
data2 = pd.DataFrame(df2)
merged_df = pd.concat([df1, df2])
st.write(merged_df)