# Programa para avaliar se um candidato pode ou não participar de um evento esportivo.


# Função para coletar informações do usuário.


def coletar_informacoes(mensagem, tipo_dado):
    while True:
        try:
            dado = tipo_dado(input(mensagem))
            return dado
        except ValueError:
            print("Entrada inválida. Por favor, tente novamente.")


# Função para avaliar se um candidato atende aos padrões necessários.


def avaliar_candidato(idade, altura):
    idade_minima = 18
    altura_minima = 1.50

    if idade < idade_minima or altura < altura_minima:
        return "Padrões necessários não atingidos, reprovado(a)."
    else:
        return "Padrões necessários atingidos, aprovado(a)!"


# Função principal do programa.


def main():
    idade = coletar_informacoes("\nDigite sua idade: ", int)
    altura = coletar_informacoes("\nDigite sua altura: ", float)

    resultado = avaliar_candidato(idade, altura)
    print(resultado)


if __name__ == "__main__":
    main()
