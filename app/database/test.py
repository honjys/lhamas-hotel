import psycopg2
conn = psycopg2.connect('dbname=ifpb user=postgres host=localhost port=5432')
cpfip =1
senhaip =123


cursor = conn.cursor()

cursor.execute("SELECT * FROM admin")

for (cpf, nome, email, telefone, senha) in cursor.fetchall():
    if cpf == cpfip and senha == senhaip:
        print("DEU CERTO")