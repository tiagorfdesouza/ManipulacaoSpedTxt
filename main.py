arquivo = open('0-EFD0821.TXT', 'r+')

novoArquivo = []

for registro in arquivo:
    if registro [:6] == '|C170|':
        newFile = list(registro.split('|'))

        for dados in newFile:
            if dados == '1' or dados == '2' or dados == '3' or dados == '4' or dados == '5':
                newFile[38] = 'MetaContadores'
        x = ('|'.join(newFile))
        novoArquivo.append(x)
        continue
    novoArquivo.append(registro)

arquivo.close()

novoSped = open('new - 552.txt', 'w')
for linha in novoArquivo:
    novoSped.writelines(linha)

novoSped.close()

print('Processo Concluido')