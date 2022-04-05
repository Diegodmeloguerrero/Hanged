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
words = 'valoracion aprenderpython comida juego python web imposible variable curso volador cabeza reproductor mirada escritor billete lapicero celular valor revista gratuito disco voleibol anillo estrella'.split()

def searchrandomswords(wordslist):
    
    randomword = random.randint(0, len(wordslist) - 1)
    return wordslist[randomword]

def displayBoard(HANGED, wrongletter, correctletter, secretword):
    print(HANGED[len(wrongletter)])
    print ("")
    end = " "
    print ('Letras incorrectas:', end)
    for letter in wrongletter:
        print (letter, end)
    print ("")
    space = '_' * len(secretword)
    for i in range(len(secretword)): 
        if secretword[i] in correctletter:
            space = space[:i] + secretword[i] + space[i+1:]
    for letra in space:
        print (letter, end)
    print ("")

def choseletter(someletter):

    while True:
        print ('Adivina una letra:')
        letter = input()
        letter = letter.lower()
        if len(letter) != 1:
            print ('Introduce una sola letra.') 
        elif letter in someletter:
            print ('Ya has elegido esa letra ¿Qué tal si pruebas con otra?')
        elif letter not in 'abcdefghijklmnopqrstuvwxyz':
            print ('Elije una letra.')
        else:
            return letter

def start():
    print ('Quieres jugar de nuevo? (Si o No)')
    return input().lower().startswith('s')

print ('A H O R C A D O')
wrongletter = ""
correctletter = ""
words = searchrandomswords(words)
endgame = False
while True:
    displayBoard(HANGED, wrongletter, correctletter, secretword)

    letter = choseletter(wrongletter + correctletter)
    if letter in secretword:
        correctletter = correctletter + letter

        findletters = True
        for i in range(len(secretword)):
            if secretword[i] not in wrongletter:
                findletters = False
                break
        if findletters:
            print ('¡Muy bien! La palabra secreta es "' + secretword + '"! ¡Has ganado!')
            endgame = True
    else:
        wrongletter = wrongletter + letter

        if len(wrongletter) == len(HANGED) - 1:
            displayBoard(HANGED, wrongletter, correctletter, secretword)
            print ('¡Se ha quedado sin letras!\nDespues de ' + str(len(wrongletter)) + ' letras erroneas y ' + str(len(correctletter)) + ' letras correctas, la palabra era "' + secretword + '"')
            endgame = True

    if endgame:
        if start():
            wrongletter = ""
            wrongletter = ""
            endgame = False
            secretword = searchrandomswords(words)
        else:
            break