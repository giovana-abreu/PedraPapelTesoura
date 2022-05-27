opcoes = ["Pedra", "Papel", "Tesoura"]
while True:
    #sua jogada!
    print(f"1 - Pedra,\n2 - Papel,\n3 - Tesoura\n")

    while True:
        jogJogador = int(input("Faça sua jogada! "))

        if jogJogador < 1 or jogJogador > 3:
            print("Opção inválida! Por favor escolha uma opção da lista!")
        else:
            print
            break

    jogJogador -= 1

    #jogada do computador

    from random import randint
    jogComputador = (randint(0,2))

    #Jogo
    if jogJogador == 0 and jogComputador == 2 or jogJogador == 1 and jogComputador == 0 or jogJogador == 2 and jogComputador == 1:
        print(f"Você escolheu: {opcoes[jogJogador]}\nSeu adversário escolheu: {opcoes[jogComputador]}\nVocê ganhou!")
    elif jogJogador == jogComputador:
            print(f"Você escolheu: {opcoes[jogJogador]} \nSeu  adversário escolheu: {opcoes[jogComputador]}\nVocês empataram!")
    else:
            print(f"Você escolheu: {opcoes[jogJogador]}\n Seu adversário escolheu: {opcoes[jogComputador]}. \nVocê perdeu!")

    reiniciar = input('Deseja reiniciar? S/N: ')
    if reiniciar == 's' or reiniciar == 'S':
        continue
    else:
        print('Obrigada por jogar conosco!')
        break