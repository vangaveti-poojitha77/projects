theBoard={'7':' ','8':' ','9':' ',
          '4':' ','5':' ','6':' ',
          '1':' ','2':' ','3':' '}
boardkeys=[]
for key in theBoard:
    boardkeys.append(key)
def printboard(board):
    print("  __ __ __ __ __ __  ")
    print(" |__"+board['7']+"__"+'|__'+board['8']+"__"+"|"+"__"+board['9']+"__|")
    print(" |__"+board['4']+"__"+'|__'+board['5']+"__"+"|"+"__"+board['6']+"__|")
    print(" |__"+board['1']+"__"+'|__'+board['2']+"__"+"|"+"__"+board['3']+"__|")

def game():
    turn="X"
    count=0
    for i in range(10):
        printboard(theBoard)

        print("its the turn of "+turn+"please specify the place want to go:")
        move=input()
        if theBoard[move]==" ":
            theBoard[move]=turn
            count+=1
        else:
            print("sorry this cell is filled please choose another one")
            continue

        if count>=5:
            if theBoard['7']==theBoard['8']==theBoard['9']!=" ":
                printboard(theBoard)
                print("-----GameOver-----")
                print("Player "+turn+" won the game")
                break
            elif theBoard['4']==theBoard['5']==theBoard['6']!=" ":
                printboard(theBoard)
                print("-----GameOver-----")
                print("Player "+turn+" won the game")
                break
            elif theBoard['1']==theBoard['2']==theBoard['3']!=" ":
                printboard(theBoard)
                print("-----GameOver-----")
                print("Player "+turn+" won the game")
                break
            elif theBoard['1']==theBoard['4']==theBoard['7']!=" ":
                printboard(theBoard)
                print("-----GameOver-----")
                print("Player "+turn+" won the game")
                break
            elif theBoard['2']==theBoard['5']==theBoard['8']!=" ":
                printboard(theBoard)
                print("-----GameOver-----")
                print("Player "+turn+" won the game")
                break
            elif theBoard['3']==theBoard['6']==theBoard['9']!=" ":
                printboard(theBoard)
                print("-----GameOver-----")
                print("Player "+turn+" won the game")
                break
            elif theBoard['1']==theBoard['5']==theBoard['9']!=" ":
                printboard(theBoard)
                print("-----GameOver-----")
                print("Player "+turn+" won the game")
                break
            elif theBoard['3']==theBoard['5']==theBoard['7']!=" ":
                printboard(theBoard)
                print("-----GameOver-----")
                print("Player "+turn+" won the game")
                break
        if count==9:
            print("GameOver")
            print("Tie")
        if turn=="X":
            turn="0"
        else:
            turn="X"

    restart=input("do you want to play again(y/n)? : ").lower()
    if restart=="y":
        for key in boardkeys:
            theBoard[key]=" "
        game()
game()