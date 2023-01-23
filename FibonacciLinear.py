def calculaFibonacci(posicao):
    anterior = 0
    atual = 1
    if posicao != 0:
        for i in range(1, posicao):
            proximo = atual + anterior
            anterior = atual
            atual = proximo   
        print("fib({}) = {}".format(posicao, atual))
    else:
        print("fib({}) = 0".format(posicao))


while True:
    try:
        posicao = input("Digite a posição desejada da sequência de Fibonatti: ")
        if posicao.isnumeric(): # Verificando se o número é inteiro >= 0
            posicao = int(posicao)
            calculaFibonacci(posicao)
            break
        else:
            print("O valor digitado é inválido! Favor digitar um número inteiro maior ou igual a zero!")
    
    except ValueError:
        print("O valor digitado é inválido! Favor digitar um número inteiro maior ou igual a zero!")
