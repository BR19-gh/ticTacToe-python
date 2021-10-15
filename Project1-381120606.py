# مشروع رقم 1 - موضوعات عامة لعلوم الحاسب 492 - إبراهيم الخويطر 381120606

import random
from os import system, name
from time import sleep

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

board=['-','-','-',
       '-','-','-',
       '-','-','-']
firstplayer=0
secondplayer=0
startMsg=0
finish=0
computerPlaying=0

def choosePlayer(player):
    playerChar=input(f"Player-{str(player)}, choose your character, either X or O: ")
    clear()
    if(playerChar=='X' or playerChar=='x'):
        print(f"Player-{str(player)} choosed X, so other Player will be O")
        sleep(3)
        clear()
        return 'X'
    elif(playerChar=='O' or playerChar=='o'):
        print(f"Player-{str(player)} choosed O, so other Player will be X")
        sleep(3)
        clear()
        return 'O'
    else:
        error=input('ERORR: Wrong Input, choose between X or O\n\nPress Enter to Select Again')
        clear()
        choosePlayer(player)
    return

def printBoard():
    i=0
    while(i<9):
        if (i==0):
            print("-------------")
        if (i==2):
            print("| "+board[i]+" |")
            print("-------------")
            i=i+1
        if (i==5):
            print("| "+board[i]+" |")
            print("-------------")
            i=i+1
        if (i==8):
            print("| "+board[i]+" |")
            print("-------------")
            i=i+1
        else:
            print("| "+board[i], end = " ")
            i=i+1
    
    return



def printBoards():
    print("The current state of the board is:")
    printBoard()
    print(" ")
    print('Use the below figure as a reference:')
    exampleBoard=['1','2','3',
                  '4','5','6',
                  '7','8','9']
    i=0
    while(i<9):
        if (i==0):
            print("-------------")
        if (i==2):
            print("| "+exampleBoard[i]+" |")
            print("-------------")
            i=i+1
        if (i==5):
            print("| "+exampleBoard[i]+" |")
            print("-------------")
            i=i+1
        if (i==8):
            print("| "+exampleBoard[i]+" |")
            print("-------------")
            i=i+1
        else:
            print("| "+exampleBoard[i], end = " ")
            i=i+1


def checkWin():
    
    # 1 2 3
    #
    #
    if (board[0]!='-' and board[0]==board[1] and board[1]==board[2]):
        clear()
        printBoard()
        
        nothing=input(f'Player-{board[0]} won, congrats.\nPress Enter to Exit')
        finish=1 
        exit()

    #
    # 4 5 6
    #
    elif (board[3]!='-' and board[3]==board[4] and board[4]==board[5]):
        clear()
        printBoard()

        nothing=input(f'Player-{board[3]} won, congrats.\nPress Enter to Exit')
        finish=1 
        exit()

    #
    #
    # 7 8 9
    elif (board[6]!='-' and board[6]==board[7] and board[7]==board[8]):
        clear()
        printBoard()

        nothing=input(f'Player-{board[6]} won, congrats.\nPress Enter to Exit')
        finish=1 
        exit()

    # 1 # #
    # 4 # #
    # 7 # #
    elif (board[0]!='-' and board[0]==board[3] and board[3]==board[6]):
        clear()
        printBoard()

        nothing=input(f'Player-{board[0]} won, congrats.\nPress Enter to Exit')
        finish=1 
        exit()

    # # 2 #
    # # 5 #
    # # 8 #
    elif (board[1]!='-' and board[1]==board[4] and board[4]==board[7]):
        clear()
        printBoard()

        nothing=input(f'Player-{board[1]} won, congrats.\nPress Enter to Exit')
        finish=1 
        exit()

    # # # 3
    # # # 6
    # # # 9
    elif (board[2]!='-' and board[2]==board[5] and board[5]==board[8]):
        clear()
        printBoard()

        nothing=input(f'Player-{board[2]} won, congrats.\nPress Enter to Exit')
        finish=1 
        exit()

    # 1
        # 5
            # 9
    elif (board[0]!='-' and board[0]==board[4] and board[4]==board[8]):
        clear()
        printBoard()

        nothing=input(f'Player-{board[0]} won, congrats.\nPress Enter to Exit')
        finish=1 
        exit()

            # 3
        # 5
    # 7
    elif (board[2]!='-' and board[2]==board[4] and board[4]==board[6]):
        clear()
        printBoard()
        if(computerPlaying==1):
            nothing=input(f'Computer (played as {board[0]}) won, Good Luck next time!\nPress Enter to Exit')
        else:
            nothing=input(f'Player-{board[2]} won, congrats.\nPress Enter to Exit')
        finish=1 
        exit()
    
    # tie
    else:
        j=0
        while(j<9):
            if(board[j]=='-'):
                break
            elif(j==8):
                clear()
                printBoard()
                if(computerPlaying==1):
                    nothing=input(f"wow! You tied with the Computer! I guess AI won't take over the planet...\nPress Enter to Exit")
                else:
                    nothing=input(f"wow! It's a tie... Good luck to you two\nPress Enter to Exit")
                finish=1 
                exit()
            j=j+1
    return False



def insertIntoBoard(player):

    chosenPosition=input(f"\nPlayer-{player} choose position between 1 to 9: ")
    if(chosenPosition.isdigit()):
        chosenPosition=int(chosenPosition)
        if(chosenPosition>9 and chosenPosition<1):
            clear()
            error=input("ERORR: Worng Input, the number should be between 1 to 9\nPress Enter to choose again")
            clear()
            insertIntoBoard(player)
        
        #check if the chosen position is occupied
        if(board[chosenPosition-1]!='-'):
            clear()
            nothing=input(f'the position #{chosenPosition-1} is occupied with {board[chosenPosition-1]}.\nPress Enter to choose again')
            clear()
            printBoards()
            insertIntoBoard(player)
        else:#if not occupied continue
            board[chosenPosition-1]=player
        checkWin()
        clear()
        if (player=="X"):
            if(computerPlaying==1):
                print("Now Computer as O will play")
            else:
                print("Now is Player-O turn")
        elif (player=="O"):
            if(computerPlaying==1):
                print("Now Computer as X will play")
            else:
                print("Now is Player-X turn")
        sleep(1)
        clear()
    else:
        clear()
        error=input("ERORR: Worng Input, it should be a number between 1 to 9\nPress Enter to choose again")
        clear()
        printBoards()
        insertIntoBoard(player)
    return

def computerPlay(secondplayer):
    
    clear()
    print(f'Computer is playing.')
    sleep(0.1667)
    clear()
    print(f'Computer is playing..')
    sleep(0.1667)
    clear()
    print(f'Computer is playing...')
    sleep(0.1667)
    clear()
    print(f'Computer is playing.')
    sleep(0.1667)
    clear()
    print(f'Computer is playing..')
    sleep(0.1667)
    clear()
    print(f'Computer is playing...')
    sleep(0.1667)
    clear()

    computerPlayed=0
    while(computerPlayed==0):
        position=random.randint(0,8)
        if (board[position]=='-'):
            board[position]=secondplayer
            computerPlayed=1
    checkWin()
    print(f'% Computer played in position #{position+1} %\n')
    return
    

def multiPlayers():
    
    while(finish==0):
        printBoards()
        insertIntoBoard(firstplayer)
        printBoards()
        insertIntoBoard(secondplayer)
    return

def singlePlayerModeStart(randomValueForPlayerToStart):
    if(randomValueForPlayerToStart==1):
        while(finish==0):
            printBoards()
            computerPlay(secondplayer)
            printBoards()
            insertIntoBoard(firstplayer)
        return
    if(randomValueForPlayerToStart==2):
        while(finish==0):
            printBoards()
            insertIntoBoard(firstplayer)
            printBoards()
            computerPlay(secondplayer)
        return


def main():

    clear()
    global startMsg, firstplayer, secondplayer, computerPlaying
    if(startMsg==0):
        print('Welcome to <X && O>.\n')
        startMsg=1
    gamemode=input('Choose form the menu:\n1- Single Player\n2- Multi-Players\n3- Student Info\n\nType Your Choice: ')

    #Strat of: Gamemode: single player
    if(gamemode=='1'):
        clear()
        print("You Choosed Single-Player Mode")
        sleep(2)
        clear()
        
        player=random.randint(1,2)
        firstplayer=choosePlayer(player)
        if(firstplayer=='X'):
            secondplayer='O'
        elif(firstplayer=='O'):
            secondplayer='X'
        computerPlaying=1
        randomValueForPlayerToStart=random.randint(1,2)
        singlePlayerModeStart(randomValueForPlayerToStart)
    #End of: Gamemode: single player

    #Strat of: Gamemode: multi-players
    elif(gamemode=='2'):
        computerPlaying=0
        clear()
        print("You Choosed Multi-Players Mode")
        sleep(2)
        clear()

        #choosing palyers
        player=random.randint(1,2)
        firstplayer=choosePlayer(player)
        if(firstplayer=='X'):
            secondplayer='O'
        elif(firstplayer=='O'):
            secondplayer='X'


        multiPlayers()
    #End of: Gamemode: mylti-players
    elif(gamemode=='3'):
        clear()
        Nothing=input("Student Name: Ibrahim Alkhowaiter\nStudent U.ID: 381120606\nClass:        CS492-764\n\nPress Enter to continue")
        clear()
        main()
    else:
        clear()
        error=input('ERORR: Wrong Input, choose between 1 or 2.\n\nPress Enter to Select Again')
        clear()
        main()

        

main()