sqlfile = None
mbti_dict = {
    'INTP': 145,
    'INFP': 128,
    'INTJ': 102,
    'INFJ': 97,
    'ENFP': 86,
    'ISFJ': 77,
    'ISTJ': 72,
    'ENTP': 70,
    'ENFJ': 60,
    'ENTJ': 58,
    'ISFP': 56,
    'ESTJ': 51,
    'ISTP': 50,
    'ESFJ': 44,
    'ESFP': 39,
    'ESTP': 31,
}

#

def createSQLFile():
    global sqlfile
    sqlfile = open('createMBTITable.sql', 'w', encoding='utf-8')

def createTable():
    global sqlfile
    sqlfile.write(
        'CREATE TABLE mbti( \n\t'
        + 'id INT PRIMARY KEY AUTO_INCREMENT, \n\t'
        + '1st char(1) NOT NULL, \n\t'
        + '2nd char(1) NOT NULL, \n\t'
        + '3rd char(1) NOT NULL, \n\t'
        + '4th char(1) NOT NULL, \n\t'
        + 'CONSTRAINT chk_mbti CHECK '
        + "(1st IN ('E', 'I') AND 2nd IN ('S', 'N') AND 3rd IN ('T', 'F') AND 4th IN ('J', 'P')) \n"
        + '); \n\n'
    )

def insertTable():
    global sqlfile
    global mbti_dict
    
    for key in mbti_dict.keys():
        cnt = mbti_dict[key]

        for n in range(cnt):
            sqlfile.write(
                "INSERT INTO mbti(id, 1st, 2nd, 3rd, 4th) "
                + f"VALUES(NULL, '{key[0]}', '{key[1]}', '{key[2]}', '{key[3]}');\n"
            )

def closeSQLFile():
    sqlfile.close()

#

createSQLFile()
createTable()
insertTable()
closeSQLFile()
