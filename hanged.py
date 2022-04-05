import random
HANGED = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
words = 'facundo comida juegos python imposible java variable volador cabeza reproductor mirada molesto escrito lapicero minas celula valor revista lava gratuito discos cartucho anillos estrellas platzi profe'.split()

def searchrandomswords(wordslist):
    
    randomword = random.randint(0, len(wordslist) - 1)
    return wordslist[randomword]

def displayBoard(HANGED, wrongletter, correctletter, secretword):
    print(HANGED[len(wrongletter)])
    print ("")
    end = " "
    print ('Fallos: ', end)
    for letter in wrongletter:
        print (letter, end)
    print ("")
    space = '_' * len(secretword)
    for i in range(len(secretword)): 
        if secretword[i] in correctletter:
            space = space[:i] + secretword[i] + space[i+1:]
    for letter in space:
        print (letter, end)
    print ("")

def choseletter(someletter):

    while True:
        print ('Escribe una letra:')
        letter = input()
        letter = letter.lower()
        if len(letter) != 1:
            print ('Solo es valida una letra.') 
        elif letter in someletter:
            print ('Esa letra ya la has jugado, mejor escribe otra :)')
        elif letter not in 'abcdefghijklmnopqrstuvwxyz':
            print ('Elije una letra.')
        else:
            return letter

def start():

    print ('¿Quieres jugar otra vez? S(si) N(no)')
    return input().lower().startswith('s')

print(""" 
─█▀▀█ 　 ░█─░█ 　 ░█▀▀▀█ 　 ░█▀▀█ 　 ░█▀▀█ 　 ─█▀▀█ 　 ░█▀▀▄ 　 ░█▀▀▀█ 
░█▄▄█ 　 ░█▀▀█ 　 ░█──░█ 　 ░█▄▄▀ 　 ░█─── 　 ░█▄▄█ 　 ░█─░█ 　 ░█──░█ 
░█─░█ 　 ░█─░█ 　 ░█▄▄▄█ 　 ░█─░█ 　 ░█▄▄█ 　 ░█─░█ 　 ░█▄▄▀ 　 ░█▄▄▄█""")
wrongletter = ""
correctletter = ""
secretword = searchrandomswords(words)
endgame = False
while True:
    displayBoard(HANGED, wrongletter, correctletter, secretword,)
    
    letter = choseletter(wrongletter + correctletter)
    if letter in secretword:
        correctletter = correctletter + letter

        findletters = True
        for i in range(len(secretword)):
            if secretword[i] not in correctletter:
                findletters = False
                break
        if findletters:
            print ('¡Ganaste! tu palabra era "' + secretword + '"!!!!')
            endgame = True
    else:
        wrongletter = wrongletter + letter

        if len(wrongletter) == len(HANGED) - 1:
            displayBoard(HANGED, wrongletter, correctletter, secretword)
            print ('¡Te quedaste sin letras!\nDespuesde ' + str(len(wrongletter)) + ' Fallos ' + str(len(correctletter)) + ' Aciertos, la palabra era "' + secretword + '"')
            endgame = True

    if endgame:
        if start():
            wrongletter = ""
            wrongletter = ""
            endgame = False
            secretword = searchrandomswords(words)
        else:
            break