'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11 para o Imposto de Renda, 8 para o INSS e 5 para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''


valor_hora = float(input("Quanto você ganha por hora? R$ "))
qtd_horas = int(input("Quantas horas você trabalha no mês? "))

salario_bruto = (valor_hora * qtd_horas)
imposto = salario_bruto * 0.11
inss = salario_bruto  * 0.08
sindicato = salario_bruto * 0.05
descontos = imposto + inss + sindicato
salario_liquido = salario_bruto - descontos

print(f"Recebendo R$ {valor_hora} por hora em {qtd_horas} no mês, você possui um total de R${descontos} descontados do seu salário bruto, assim seu saĺario líquido é de R$ {salario_liquido} mensais")