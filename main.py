from functions import *

registro = [{
        "mes_ano_referencia" : "01-2022",
        "total_habitantes" : 1000000,
        "Total_obitos": 500000
    },
    {
        "mes_ano_referencia": "12-2021",
        "total_habitantes": 1500000,
        "Total_obitos": 600000
    },
    {
        "mes_ano_referencia": "10-2019",
        "total_habitantes": 1400000,
        "Total_obitos": 400000
    },
    {
        "mes_ano_referencia": "11-2022",
        "total_habitantes": 400000,
        "Total_obitos": 100000
    },
    {
        "mes_ano_referencia": "02-2021",
        "total_habitantes": 2500000,
        "Total_obitos": 6400000
    },
    {
        "mes_ano_referencia": "05-2022",
        "total_habitantes": 4500000,
        "Total_obitos": 100000
    }
]


while True:
    menu = int(input("MENU PRINCIPAL\n"
                 "\n1 – Cadastrar mês de referência\n"
                 "2 – Exibir dados do mês de referência\n"
                 "3 – Relatório comparativo – Referência 2019\n"
                 "4 – Listar todos os meses cadastrados\n"
                 "\nDigite a opção desejada: "))
    if menu == 1:
        item = cadastrarMes()
        registro.append(item)
        if continuar():
            print("Programa encerrado.")
            break
        else:
            continue
    elif menu == 2:
        pesquisarMes(registro)
        if continuar():
            print("Programa encerrado.")
            break
        else:
            continue
    elif menu == 3:
        relatorioComparativo(registro)
        if continuar():
            print("Programa encerrado.")
            break
        else:
            continue
    elif menu == 4:
        listarTudo(registro)
        if continuar():
            print("Programa encerrado.")
            break
        else:
            continue
    else:
        print("Entrada inválida. Retornando ao menu principal")
        continue
