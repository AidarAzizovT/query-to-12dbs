import pandas as pd

# Загрузка данных из xlsx-файла
df = pd.read_excel('output.xlsx')

# Создание пустого списка для уникальных значений
unique_values = [[], []]
headers = df.columns.tolist()
print(headers)


for column_index in range(0, len(headers) -1, 2):
    # Получение уникальных значений каждого столбца и добавление их в список
    unique_values[0].extend(df[headers[column_index]].tolist())
    unique_values[1].extend(df[headers[column_index + 1]].tolist())

    print(df[headers[column_index]], df[headers[column_index + 1]])

# Преобразование списка уникальных значений во множество для удаления повторений

# Вывод уникальных значений
pd.DataFrame({'VAL': unique_values[0], 'VAL_SHORT': unique_values[1]}).to_excel('master_list_810.xlsx',index=False)

