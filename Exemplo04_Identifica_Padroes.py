#Vamos criar um exemplo onde você vai ao supermercadom 20 reais e deverá consumir itens de  no máximo 10 reais
arroz_kg = 7.00
feijao_kg = 9.00
carne_kg = 35.00

for i in range(3):
#Agora vamos  perguntar ao computador quais desses itens eu posso comprar
    valor = input('Digite o valor do seu item: ')
    valor = float(valor)
    if valor <= 10.00 :
        print('Posso comprar!')
    else:
        print('Não posso comprar!')