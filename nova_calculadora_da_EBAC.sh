#!/bin/bash

# Agora vai #

echo "Calculadora EBAC de 4 Operações"
echo "Escolha a operação:"
echo "1 - Adição"
echo "2 - Subtração"
echo "3 - Multiplicação"
echo "4 - Divisão"
read -p "Digite o número da operação desejada: " operacao

read -p "Digite o primeiro número: " num1
read -p "Digite o segundo número: " num2

case $operacao in
    1) resultado=$(echo "$num1 + $num2" | bc) ;;
    2) resultado=$(echo "$num1 - $num2" | bc) ;;
    3) resultado=$(echo "$num1 * $num2" | bc) ;;
    4) 
        if [ "$num2" -eq 0 ]; then
            echo "Erro: divisão por zero não é permitida."
            exit 1
        fi
        resultado=$(echo "scale=2; $num1 / $num2" | bc) ;;
    *)
        echo "Opção inválida!"
        exit 1 ;;
esac

echo "Resultado: $resultado"

