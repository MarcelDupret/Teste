import psycopg2 as conector

conn = None
cur = None

try:
    # Connect to your postgres DB
    conn = conector.connect(user="marcel", password="2024&Madaba", dbname="marcel")

    # Open a cursor to perform database operations
    cur = conn.cursor()
    #(codalu, nome, cpf, sexo, dtnasc)
    #cur.execute("DELETE FROM alu WHERE codalu = %s;",(7,))

    # Execute a query
    cur.execute("SELECT * FROM alu")

    # Retrieve query results
    records = cur.fetchall()

    conn.commit() 


    # View the data
    print("Tabela: ")
    for reg in records:
        print(reg)

except conector.DatabaseError as erro:
    print("Erro de banco de dados: ", erro)


finally:
    # Close cursor and conection 
    if cur:
        cur.close()
    if conn:
        conn.close()