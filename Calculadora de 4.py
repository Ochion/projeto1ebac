def calcular(operacao, num1, num2):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 == 0:
            return "Erro: divisão por zero não é permitida."
        return round(num1 / num2, 2)
    else:
        return "Opção inválida!"


def main():
    print("Calculadora Simples")
    print("Escolha a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    try:
        operacao = int(input("Digite o número da operação desejada: "))
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = calcular(operacao, num1, num2)
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Erro: entrada inválida. Certifique-se de inserir números válidos.")


if __name__ == "__main__":
    main()

