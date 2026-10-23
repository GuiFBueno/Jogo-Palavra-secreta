"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = 'perfume'
palavra_final = ''
contador = 0

while True:
    letra_nova = input('Digite uma letra: ')
    contador += 1

    if len(letra_nova) > 1:
        print('Só pode 1 letra por vez')
        continue 

    if letra_nova in palavra_secreta:
        palavra_final += letra_nova

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in palavra_final:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*' 
    print(palavra_formada)   
        
    if palavra_formada == palavra_secreta:
            print(f'meus parabens, a palavra era {palavra_secreta}')
            print(f'o numero de tentativas foi {contador}')
            break



    
        
    

