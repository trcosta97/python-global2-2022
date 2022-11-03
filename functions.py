from operator import itemgetter


def cadastrarMes():
    mesAno = str(input("Mês-ano..............:"))
    if len(mesAno) < 2:
        mesAno = '0' + mesAno
    print(mesAno)
    totalHab = int(input("Total de Habitantes..: "))
    totalObitos = int(input("Total de óbitos......:"))
    registro = {
        "mes_ano_referencia" : mesAno,
        "total_habitantes" : totalHab,
        "Total_obitos": totalObitos
    }
    print("\n***** Gravado com sucesso *****\n")
    return registro

def pesquisarMes(listaRegistros):

    mesAno = input("Digite o mês-ano desejado.....:")
    possui_registros = False

    for item in listaRegistros:
        if mesAno in item["mes_ano_referencia"]:
            print("Mês-ano..............: " , item["mes_ano_referencia"])
            print("Total de Habitantes..: " , item["total_habitantes"])
            print("Total de óbitos......:  " , item["Total_obitos"], "\n")
            print("***** Registro encontrado *****\n")
            possui_registros = True

    if not possui_registros:
        print("***** Mês-ano não cadastrado! *****\n")

def relatorioComparativo(listaRegistros):
    anoSelecionado = input("Digite ano a ser comparado........:")
    global totalHab
    totalHab = 0
    totalObitos = 0

    for item in listaRegistros:
        if anoSelecionado in item["mes_ano_referencia"] :
            totalHab = totalHab + item["total_habitantes"]
            totalObitos = totalObitos + item["Total_obitos"]

    taxa100Hab = round(totalObitos/100.000, 2)

    if totalHab != 0:
        print("\nTotal de Habitantes...............: ", totalHab)
        print("Total de óbitos...................: ", totalObitos)
        print("Taxa por 100k habitantes - ", anoSelecionado, "....: ", taxa100Hab)
        print("Taxa por 100k habitantes - 2019....: 15.00")
        diferencaObitos = ((totalObitos-15000)/1500)
        print("Comparativo % entre ", anoSelecionado, "-2019.....: ", round(diferencaObitos, 2), "%\n" )

    else:
        print("***** Ano não cadastrado! *****")

def listarTudo(listaRegistro):

    listaOrdenada = sorted(listaRegistro, key=itemgetter('mes_ano_referencia'))

    for item in listaOrdenada:
        print("\nMês-ano referência...........:", item["mes_ano_referencia"])
        print("Total Habitantes.............:", item["total_habitantes"])
        print("Total óbitos.................:", item["Total_obitos"])

def continuar():
    encerrar = input("\nDeseja continuar? s/n\n").capitalize()
    if encerrar == "N":
        return True
    elif encerrar == "S":
        return False
    else:
        print("\nEntrada inválida. Retornando ao menu principal\n")
        return False

def quickSort(lista):
    less = []
    equal = []
    greater = []

    if len(lista) > 1:
        pivot = lista[0]
        for x in lista:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quickSort(less)+equal+quickSort(greater)

    else:
        return lista






