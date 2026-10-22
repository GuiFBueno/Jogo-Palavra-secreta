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

    if len(letra_nova) > 1:
        print('Só pode 1 letra por vez')
        continue 

    if letra_nova in palavra_secreta:
        palavra_final += letra_nova
    print(palavra_final)       
            

    if palavra_final == palavra_secreta:
        print('meus parabens')



    
        
    

