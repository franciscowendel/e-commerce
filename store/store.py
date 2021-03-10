from typing import List, Dict
from time import sleep
from product import Product
from userverify import User


produtos: List[Product] = []
carrinho: List[Dict[Product, int]] = []


def menu():
    try:
        print('-------------------------------------------------------------------------------------------------------')
        print('---------------------------------------------- STORE --------------------------------------------------')
        print('-------------------------------------------------------------------------------------------------------')
        print()
        print('O QUE DESEJA: ')
        print()
        print('1 - CADASTRAR PRODUTO: ')
        print('2 - LISTAR PRODUTOS: ')
        print('3 - COMPRAR PRODUTO: ')
        print('4 - VER CARRINHO: ')
        print('5 - FECHAR PEDIDO: ')
        print('6 - SAIR: ')
        print()

        opcao: int = int(input())

        if opcao == 1:
            cadastrar_produto()
        elif opcao == 2:
            listar_produtos()
        elif opcao == 3:
            comprar_produto()
        elif opcao == 4:
            ver_carrinho()
        elif opcao == 5:
            fechar_pedido()
        elif opcao == 6:
            print('VOLTE SEMPRE!')
            sleep(1)
            exit(1)
        else:
            print('OPÇÃO INVÁLIDA...')
            sleep(1)
            menu()

    except (ValueError, TypeError) as err:
        return f'Erro do tipo {err} encontrado...'


def cadastrar_produto():
    try:
        print('-------------------')
        print('CADASTRAR PRODUTO: ')
        print('-------------------')
        print()
        nome: str = input('NOME DO PRODUTO: ')
        valor: float = float(input('VALOR DO PRODUTO: '))
        print()
        produto: Product = Product(nome, valor)

        print('------------------')
        print('DADOS DO PRODUTO: ')
        print('------------------')
        print()
        print(produto)
        produtos.append(produto)
        print()
        print('PRODUTO CADASTRADO COM SUCESSO!')
        print()
        sleep(1)
        menu()

    except (ValueError, TypeError) as err:
        return f'Erro do tipo {err} encontrado...'


def listar_produtos():
    if len(produtos) > 0:

        print('-------------------')
        print('LISTA DE PRODUTOS: ')
        print('-------------------')
        print()
        for produto in produtos:
            print(produto)
            print('-------------------')
            print()
            sleep(1)

    else:
        print('NENHUM PRODUTO CADATRADO...')
    sleep(1)
    menu()


def comprar_produto():
    try:
        if len(produtos) > 0:
            print('-------------------------------------------')
            print('CÓDIGO DO PRODUTO QUE VOCÊ DESEJA COMPRAR: ')
            print('-------------------------------------------')
            print()
            for produto in produtos:
                print(produto)
                print()

            numero: int = int(input())

            produto: Product = rastrear_produto(numero)

            if produto:
                if len(carrinho) > 0:
                    exist: bool = False

                    for item in carrinho:
                        quant: int = item.get(produto)

                        if quant:
                            item[produto] = quant + 1
                            print(f'PRODUTO {produto.nome} AGORA POSSUI {quant + 1} UNIDADES NO CARRINHO.')
                            exist: bool = True
                            print('-----------------------------------------------------------------------')
                            sleep(1)

                else:
                    item: Dict[Product, int] = {produto: 1}
                    carrinho.append(item)
                    print(f'O PRODUTO {produto.nome} FOI ADICIONADO NO CARRINHO COM SUCESSO!')
                    print()

            else:
                print(f'PRODUTO COM CÓDIGO INFORMADO NÃO FOI ENCONTRADO.')
                print()

            sleep(1)
            menu()

        else:
            print('NENHUM PRODUTO CADASTRADO...')
        sleep(1)
        menu()

    except (ValueError, TypeError) as err:
        return f'Erro do tipo {err} encontrado...'


def ver_carrinho():
    pass


def fechar_pedido():
    pass


def rastrear_produto(numero):
    x: Product = None  # noqa

    if len(produtos) > 0:
        for produto in produtos:
            if produto.codigo == numero:
                x: Product = produto
    return x


if __name__ == '__main__':
    menu()
