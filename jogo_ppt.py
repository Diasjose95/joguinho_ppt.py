def jogo_ppt(ppt: str ) -> str:
    return ppt
import random     #esse comando importa o modo random ou seja aleatorio

# aqui vai ficar todas as variavei q vou utilizar e tbm as lista!
ppt = ["pedra", "papel", "tesoura"]
maquina = random.choice(ppt) #comando para utilizar o random!

contador_empate = 0
contador_victoria = 0
contador_derrota = 0
tesoura = 'tesoura'
papel = 'papel'
pedra = 'pedra'

# aqui  utilizei o laço for pra fazer uma melhor de 3!
for v in  range(1,3+1):
    usuario = input("escolha entre pedra, papel ou tesoura: ").lower().strip()


    # utilizei o laõ while para  verificar se o valor inserido pelo usuario e valido!
    while usuario not in ppt:
        print("Digite uma opção valida!")
        usuario = input("escolha entre pedra, papel ou tesoura: ").lower().strip()




    print(f"Maquina: {maquina}")
    print("Usuario: {}".format(usuario)) #usei o ponto format so de sacanagem fessor! kkkkkkkkkkkkkkkkkkkk


# aqui e a verificação de quem venceu no pedra, papel e tesoura
    if maquina == usuario:
        print("empate!")
        contador_empate +=1
    elif maquina == pedra and usuario == tesoura:
        print("A maquina venceu!")
        contador_derrota +=1
    elif maquina == papel and usuario == pedra:
        print("A maquina venceu!")
        contador_derrota +=1
    elif maquina == tesoura and usuario == papel:
        print("A maquina venceu!")
        contador_derrota +=1
    else:
        print("vc venceu!")
        contador_victoria+=1

# aqui se encontar o placar que sera exibido ao final de cada rodada!
    print(f"victoria: {contador_victoria}")
    print(f"derrota: {contador_derrota}")
    print(f"empate: {contador_empate}") 



# e por fim a verificação de quem venceu a melhor de 3 ou se ouve empate!
if contador_empate == contador_victoria and contador_empate == contador_derrota:
    print("EMPATE!")
elif contador_empate > contador_victoria and contador_empate > contador_derrota:
    print('EMPATE!')
elif contador_derrota > contador_victoria and contador_derrota > contador_empate:
    print('VC PERDEU!')
else :
    print("VC FOI O VENCEDOR!")

#por fim a mensagem de fim de jogo!
print("GAME OVER")
