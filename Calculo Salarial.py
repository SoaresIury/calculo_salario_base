


mes = input('Informe o mês:')

salario_usuario = int(input('Informe seu salario:'))

def calculo_salarial():

    base_anual = salario_usuario * 12
    salario_bruto = salario_usuario
    imposto_de_renda = (salario_bruto * 11) / 100
    inss = (salario_bruto * 8) / 100
    sindicato = (salario_bruto *5)/100

    base_de_caulculo = (salario_bruto - imposto_de_renda - inss - sindicato)

    print(f'Esta é a base de ccalculo do seu salário para o mês de {mes} ')

    salario_mensal = [

    f'O seu salário bruto foi de R$: {salario_bruto}',
    f'O seu imposto de renda foi de R$: {imposto_de_renda}',
    f'O seu inss foi de R$: {inss}',
    f'O desconto do sindicato foi de R$: {sindicato}',
    ]



    for lista_salario in salario_mensal:
            print( lista_salario)


    print(f'O seu salário liquido de {mes} a receber é de R$ {base_de_caulculo} ')
    print(f'A sua base salarial anual é de R$ {base_anual} por ano ')

calculo_salarial()