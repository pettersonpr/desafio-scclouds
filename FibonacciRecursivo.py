def calculaFibonatti(lista, posicao):

    if posicao == 1:
        print("fib({}) = {}".format(posicao_original, lista[1]))
    else:
        posicao = posicao - 1
        novo_valor = lista[0] + lista[1]
        calculaFibonatti([lista[1], novo_valor], posicao)

while True:
    try:
        posicao_original = input("Digite a posicao desejada da sequêcia de fibonatti: ")
        
        if posicao_original.isnumeric():  # Verificando se o número é inteiro >= 0
            posicao_original = int(posicao_original)
            posicao = posicao_original
            
            if posicao_original == 0:
                print("fib(0): 0")
                break
            elif posicao_original == 1:
                print("fib(1): 1")
                break
            else:
                calculaFibonatti([0, 1], posicao_original)
                break
        else:
            print(
                "O valor digitado é inválido! Favor digitar um número inteiro maior ou igual a zero!")

    except ValueError:
        print("O valor digitado é inválido! Favor digitar um número inteiro maior ou igual a zero!")
