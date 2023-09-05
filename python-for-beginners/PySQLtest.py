"""
Connects to a SQL database using pyodbc
"""
import pyodbc
SERVER = 'IT3369'
DATABASE = 'PBS'
USERNAME = 'sa'
PASSWORD = 'cisd@1234'
connectionString = f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
conn = pyodbc.connect(connectionString)
SQL_QUERY = """
SELECT TOP (5) [CONT_ID]
      ,[CONT_NO]
      ,[CONT_DT]
      ,[FNL_USR]
      ,[LOAD_PORT]
      ,[UNLOAD_PORT]
      ,[VIA]
      ,[CTRY_CD_FR]
      ,[CTRY_CD_TO]
  FROM [PBS].[dbo].[CONT_MAST];
"""
cursor = conn.cursor()
cursor.execute(SQL_QUERY)
records = cursor.fetchall()
for x in records:
    print(x)
    