''' Considerações:
        * O 2 é o único número natural par que é número primo
        * Um número natural (ímpar ou par) não tem divisor que seja maior que sua mentade arredondada (para cima ou para baixa caso seja ímpar), exceto o próprio número em questão. 
        Observação: Para o número ímpar, nem a sua metade arredondada para baixo é divisor do número em questão.
        Exemplo: O número 101 não possui divisor maior OU IGUAL que 50 (metade arredondada para baixo)'''

while True:
    try:
        num = input("Verificar os números primos até: ")
        
        if num.isnumeric() and int(num) > 1:  # Verificando se o número é inteiro >= 0

            num = int(num)
            num_primos = "2,"

            if num > 5:
                
                for i in range(3, num+1, 2): # Números a serem verificados se são primos
                    multiplo = 0
                    
                    for divisor in range(3, int(i/2), 2): # Divisores dos números que estão sendo verificados
                        if (i % divisor == 0):
                            multiplo += 1
                            break
                    
                    if(multiplo == 0): #É primo
                        num_primos += str(i) + ","

                print("p({}) = [{}]".format(num, num_primos[:-1]))
                break

            elif  num == 2:
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
        print("O valor digitado é inválido! Favor digitar um número inteiro maior que zero!")

