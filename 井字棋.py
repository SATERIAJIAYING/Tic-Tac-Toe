import os

def Update():  #更新棋盘
    os.system("cls")
    print("+---+---+---+\n",
          "| ",Board[6]," | ",Board[7]," | ",Board[8]," |\n",
          "+---+---+---+\n",
          "| ",Board[3]," | ",Board[4]," | ",Board[5]," |\n",
          "+---+---+---+\n",
          "| ",Board[0]," | ",Board[1]," | ",Board[2]," |\n",
          "+---+---+---+\n",sep="")

def IsWin():  #判定胜负
    if((Board[0]==Board[1]==Board[2]!=" ") | (Board[3]==Board[4]==Board[5]!=" ") | (Board[6]==Board[7]==Board[8]!=" ") |
       (Board[0]==Board[3]==Board[6]!=" ") | (Board[1]==Board[4]==Board[7]!=" ") | (Board[2]==Board[5]==Board[8]!=" ") |
       (Board[0]==Board[4]==Board[8]!=" ") | (Board[2]==Board[4]==Board[6]!=" ")):
        return True
    elif(Board[0]!=" ")&(Board[1]!=" ")&(Board[2]!=" ")&(Board[3]!=" ")&(Board[4]!=" ")&(Board[5]!=" ")&(Board[6]!=" ")&(Board[7]!=" ")&(Board[8]!=" "):
        return "draw"
    else:
        return False

state=2  #2正常游戏  1重开游戏  0关闭游戏
while state:
    Board=[" "," "," "," "," "," "," "," "," "] #九个
    Update()
    Player="X" #玩家对应的棋子类型 X(先手) ＆ O
    state=2

    while state is 2:
        buf=input("当前玩家：{0}\n请从1~9（对应小键盘）中选择落子位置：".format(Player))
        while (not buf.isdigit()) or (int(buf) not in range(1,10)) or (Board[int(buf)-1] != " "):
            buf=input("输入非法!\n请从1~9（对应小键盘）中选择落子位置：")
        chess=int(buf)
        Board[chess-1]=Player
        Update()

        if (IsWin() is True)or(IsWin() is "draw"):
            if IsWin() is True:
                print("{0} 玩家获得了胜利".format(Player))
            else:
                print("平局")
            buf=input("请选择是否开始新的一局游戏？  \n1.重开游戏 2.关闭游戏\n".format(Player))
            while (not buf.isdigit())or(int(buf) not in range(1,3)):
                buf=input("输入非法!\n请选择是否开始新的一局游戏？  \n1.重开游戏 2.关闭游戏\n")
            state=int(buf)-2

        if Player is "X": # 交换玩家
            Player="O"
        else:
            Player="X"

    
