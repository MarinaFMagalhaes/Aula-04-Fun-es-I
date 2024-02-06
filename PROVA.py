'''Desenvolva um programa em Python que permita ao usuário digitar várias notas. Em seguida, crie uma função chamada 
"calcular_media" que irá receber as notas digitadas e calcular a média do aluno. Também crie uma função chamada 
"verificar_situacao" que, com base na média calculada, irá exibir a situação do aluno: "Reprovado" se a média for 
menor que 7, "Aprovado" se a média for maior ou igual a 7, e "Parabéns, sua média é 10" se a média for igual a 10.'''

def main():
    num_notas = int(input("Digite a quantidade de notas: "))
    notas = []
    for x in range(num_notas):
        nota = float(input(f'Digite a nota {x + 1}: '))
        notas.append(nota)

    media_aluno = calcular_media(notas)

    situacao = verificar_situacao(media_aluno)
    print(f'A média do aluno é: {media_aluno:.2f}')
    print(f'Situação: {situacao}')

def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_situacao(media):
    if media < 7:
        return "Reprovado"
    elif media == 10:
        return "Parabéns, sua média é 10"
    else:
        return "Aprovado"

if __name__ == "__main__":
    main()