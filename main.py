import cx_Oracle
import pandas as pd

cx_Oracle.init_oracle_client(lib_dir=r"instantclient_21_9")


def parse(connection, query):
    data = []
    conn = cx_Oracle.connect(user=connection['username'], password=connection['password'],
                             dsn=f"{connection['host']}/{connection['database']}")
    with conn.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows



# Read query and columns
with open('dict.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    columns = lines[1].replace('\n', '').split(', ')
    query = "".join(lines)

# Read connections
connections = []
with open('database.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        args = line.split('|')
        connections.append({
            'district': args[0].strip(),
            'host': args[1].strip(),
            'database': args[2].strip(),
            'username': args[3].strip(),
            'password': args[4].strip()
        })

gdict = {}

for index, connection in enumerate(connections):
    data = None
    print(f"START PARSING: {connection['district']}")
    try:
        data = parse(connection, query)
        print('END')
        print('')
    except Exception as e:
        print(e)
    if data is None:
        continue
    for column in columns:
        gdict[f"{connection['district']} - {column}"] = list()
    gdict[index * ' '] = list()
    #gdict[connection['district']] = list()

    for row in data:
        for index, column in enumerate(columns):
            gdict[f"{connection['district']} - {column}"].append(row[index])


    # for i in range(len(gdict[connection['district'] + column])):
    #     gdict[connection['district']].append('')

df = pd.DataFrame({k: pd.Series(v) for k, v in gdict.items()})


df.to_excel('test.xlsx', index=False)