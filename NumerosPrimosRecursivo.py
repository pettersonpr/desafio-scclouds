''' Considerações:
        * O 2 é o único número natural par que é número primo
        * Um número natural (ímpar ou par) não tem divisor que seja maior que sua mentade arredondada (para cima ou para baixa caso seja ímpar), exceto o próprio número em questão. 
        Observação: Para o número ímpar, nem a sua metade arredondada para baixo é divisor do número em questão.
        Exemplo: O número 101 não possui divisor maior OU IGUAL que 50 (metade arredondada para baixo)'''


def verificaPrimos(num):

    multiplo = 0
    # Divisores dos números que estão sendo verificados
    for divisor in range(3, int(num/2), 2):
        if (num % divisor == 0):
            multiplo += 1
            break
    if (multiplo == 0):  # É primo
        global num_primos
        num_primos = "," + str(num) + num_primos

    num -= 2
    if 2 < num:
        verificaPrimos(num)


while True:
    try:
        num = input("Verificar os números primos até: ")

        if num.isnumeric() and int(num) > 1:  # Verificando se o número é inteiro >= 0
            num = int(num)
            num_primos = ""

            if num > 5:
                if num % 2 == 1:
                    verificaPrimos(num)
                else:
                    # Número par maior que dois não é primo
                    verificaPrimos(num-1)

                print("p({}) = [2{}]".format(num, num_primos))
                break
            elif num == 2:
                print("p({}) = [2]".format(num))
                break
            elif 2 < num < 5:
                print("p({}) = [2, 3]".format(num))
                break
            elif num == 5:
                print("p({}) = [2, 3, 5]".format(num))
                break
        else:
            print(
                "O valor digitado é inválido! Favor digitar um número inteiro maior que zero!")

    except ValueError:
        print(
            "O valor digitado é inválido! Favor digitar um número inteiro maior que zero!")

