Это программа для парсинга 12 баз данных АСУ ЕИРЦ
0. Установи библиотеки из requirements.txt
1. Поменяй пароли в файле database.txt
2. Введи в файл dict.txt данные в формате:
    select
    max(LENGTH(SCD$ADDR_ACT.del_reason))
    from SCD$ADDR_ACT
    where SCD$ADDR_ACT.del_reason is not null

   
3. Запускай main.py
4. Программа сформирует result.xlsx файл
