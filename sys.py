import sys

# Criando um objeto do tipo file
temp = open(input('Nome do arquivo a ser editado:') + ".txt", 'w')
# Escrevendo no arquivo
for i in range(100):
    temp.write('%03d\n' % i)
# Fechando
temp.close()
temp = open('Lucas Eduardo','r')
# Escrevendo no terminal
for x in temp:
    sys.stdout.write(x)
#Escrever em sys.stdout envia
# otexto para a saída padrão
temp.close()
