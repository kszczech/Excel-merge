import Automat as a
import TableAutomat as t

a.fill()







'''
for i in input_tab:
    if i[2] == "Cyberbezpieczeństwo" or i[2] == "Teleinformatyka" or i[2] == "Elektronika i Telekomunikacja" or i[2] == "Electronics and Telecommunications":
        autobus1.append(i)
    elif i[3] != "OUT":
        autobus2.append(i)
    else:
        out.append(i)
print(len(input_tab))
print(len(autobus1))
print(len(autobus2))
print(len(out))
print(autobus1)
print(autobus2)

for i in range(len(autobus1)):
    char = 'A' + str(i + 2)
    wsOutput[char].value = autobus1[i][0]
    char = 'B' + str(i + 2)
    wsOutput[char].value = autobus1[i][1]
    char = 'C' + str(i + 2)
    wsOutput[char].value = autobus1[i][2]

for i in range(len(autobus2)):
    char = 'F' + str(i + 2)
    wsOutput[char].value = autobus2[i][0]
    char = 'G' + str(i + 2)
    wsOutput[char].value = autobus2[i][1]
    char = 'H' + str(i + 2)
    wsOutput[char].value = autobus2[i][2]



output.save('output_autobusy_done.xlsx')


column_in = [3, 4, 7]

for row in range(2,83):
    line = []
    for col in column_in:
        char = ou.get_column_letter(col) + str(row)
        line.append(wsInput[char].value)
    input_tab.append(line)
print(input_tab)

column_out = [1,2,12]
for row in range(2,98):
    line = []
    for col in column_out:
        char = ou.get_column_letter(col) + str(row)
        line.append(wsOutput[char].value)
    output_tab.append(line)
print(output_tab)


for outdata in range(len(output_tab)):
    for indata in range(len(input_tab)):
        if input_tab[indata][0] == output_tab[outdata][0] and input_tab[indata][1] == output_tab[outdata][1] and output_tab[outdata][2] == None:
            char = 'O' + str(outdata + 2)
            wsOutput[char].value = input_tab[indata][2]
output.save('output_estrarto.xlsx')

for outdata in range(len(input_tab_p)):
    for indata in range(len(input_tab)):
        if input_tab[indata][0] in input_tab_p[outdata][0] and input_tab[indata][1] in input_tab_p[outdata][0]:
            char = 'A' + str(outdata+2)
            wsOutput[char].value = input_tab[indata][0]
            char = 'B' + str(outdata + 2)
            wsOutput[char].value = input_tab[indata][1]
            char = 'C' + str(outdata + 2)
            wsOutput[char].value = input_tab_p[outdata][1]

output.save('output_auto.xlsx')
'''

