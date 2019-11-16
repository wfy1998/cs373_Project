import csv
import numpy as np
filename = "amazon.csv"
fields = []
rows = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = csvreader.next()
    for row in csvreader:
        rows.append(row)

data = []
for i in range(np.shape(rows)[0]):
    # print (rows[i][0])
    if rows[i][0] == "2007" or rows[i][0] == "2012" or rows[i][0] == "2017":
        if float(rows[i][3]) > 30:
            rows[i][3] = 1
        else:
            rows[i][3] = -1

        rows[i][0] = float(rows[i][0])

        if rows[i][2] == "Janeiro":
            rows[i][2] = 1
        elif rows[i][2] == "Fevereiro":
            rows[i][2] = 2
        elif rows[i][2] == "Mar\xe7o":
            rows[i][2] = 3
        elif rows[i][2] == "Abril":
            rows[i][2] = 4
        elif rows[i][2] == "Maio":
            rows[i][2] = 5
        elif rows[i][2] == "Junho":
            rows[i][2] = 6
        elif rows[i][2] == "Julho":
            rows[i][2] = 7
        elif rows[i][2] == "Agosto":
            rows[i][2] = 8
        elif rows[i][2] == "Setembro":
            rows[i][2] = 9
        elif rows[i][2] == "Outubro":
            rows[i][2] = 10
        elif rows[i][2] == "Novembro":
            rows[i][2] = 11
        elif rows[i][2] == "Dezembro":
            rows[i][2] = 12
        else:
            rows[i][2] = 0

        if rows[i][1] == "Acre":
            rows[i][1] = 1
        elif rows[i][1] == "Alagoas":
            rows[i][1] = 2
        elif rows[i][1] == "Amapa":
            rows[i][1] = 3
        elif rows[i][1] == "Amazonas":
            rows[i][1] = 4
        elif rows[i][1] == "Bahia":
            rows[i][1] = 5
        elif rows[i][1] == "Ceara":
            rows[i][1] = 6
        elif rows[i][1] == "Distrito":
            rows[i][1] = 7
        elif rows[i][1] == "Espirito":
            rows[i][1] = 8
        elif rows[i][1] == "Goias":
            rows[i][1] = 9
        elif rows[i][1] == "Maranhao":
            rows[i][1] = 10
        elif rows[i][1] == "Mato Grosso":
            rows[i][1] = 11
        elif rows[i][1] == "Minas Gerais":
            rows[i][1] = 12
        elif rows[i][1] == "Paraiba":
            rows[i][1] = 13
        elif rows[i][1] == "Pernambuco":
            rows[i][1] = 14
        elif rows[i][1] == "Piau":
            rows[i][1] = 15
        elif rows[i][1] == "Rio":
            rows[i][1] = 16
        elif rows[i][1] == "Rondonia":
            rows[i][1] = 17
        elif rows[i][1] == "Roraima":
            rows[i][1] = 18
        elif rows[i][1] == "Santa Catarina":
            rows[i][1] = 19
        elif rows[i][1] == "Sao Paulo":
            rows[i][1] = 20
        elif rows[i][1] == "Sergipe":
            rows[i][1] = 21
        elif rows[i][1] == "Tocantins":
            rows[i][1] = 22
        elif rows[i][1] == "Espirito Santo":
            rows[i][1] = 23
        elif rows[i][1] == "Distrito Federal":
            rows[i][1] = 24

        data.append(rows[i])


with open('data.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(data)


print (data)

csvfile.close()
writeFile.close()