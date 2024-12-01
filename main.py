numero_secreto = 8
tentativas = 3

print("Bem-vindos ao grande jogo de adivinhação!!!")
print("Tente descobrir o número secreto (entre 1 e 10) e apenas 3 tentativas. Boa sorte!")

while tentativas > 0:
    palpite = int(input("Digite seu palpite: "))
    
    if palpite == numero_secreto:
        if tentativas == 3:
                print("Parabéns. Voçê acertou de primeira!")
                

        elif tentativas == 2:
                print("Parabéns. Voçê acertou na segunda tentativa!")
                

        else:
                print("Parabéns. Na ultima voçê conseguiu!")
        break        

    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"Errado! Voçê ainda tem {tentativas} tentativa(s) restante")
        else:
            print("Errado! Suas tentas acabaram.")

if tentativas == 0:
    print(f"O número secreto era {numero_secreto}. Tente novamente!")
