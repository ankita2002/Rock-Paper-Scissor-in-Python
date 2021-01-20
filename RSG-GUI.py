import tkinter as tk
import random
from tkinter import messagebox

score_player=0
score_com=0
mainwindow=tk.Tk()
mainwindow.title("Rock Paper Scissors")
mainwindow.geometry("550x550")
#----------------image file handles-------------------
img_com_rock=tk.PhotoImage(file="images\com_rock.png")
img_com_paper=tk.PhotoImage(file="images\com_paper.png")
img_com_scissor=tk.PhotoImage(file="images\com_scissor.png")
img_blank=tk.PhotoImage(file="images\\blank.png")
img_player_rock=tk.PhotoImage(file="images\player_rock.png")
img_player_paper=tk.PhotoImage(file="images\player_paper.png")
img_player_scissor=tk.PhotoImage(file="images\player_scissor.png")
#-----------------------functions for buttons-----------------------
def check():             # Checks Score if it is 10 or not
    global score_com
    global score_player
    if(score_com>=10):
        messagebox.showinfo("Rock Paper Scissors","Computer Won the game\nGame Resets now")  
        score_com=0
        score_player=0
    if(score_player>=10):
        messagebox.showinfo("Rock Paper Scissors","You Won the game\nGame Resets now")  
        score_com=0
        score_player=0   
def rock():               #1 is rock 2 is paper 3 is scissors
    player_choice=1
    global score_player
    global score_com
    player_choiceimg["image"]=img_player_rock
    comp_choice=random.randint(1,3)
    if comp_choice==1:
        result_label["text"]="TIE Match Draw"
        com_choiceimg["image"]=img_com_rock
    elif comp_choice==2:
        result_label["text"]="You Lost Computer Won"
        com_choiceimg["image"]=img_com_paper
        score_com+=1
    elif comp_choice==3:
        result_label["text"]="You Won Computer Loses"
        com_choiceimg["image"]=img_com_scissor
        score_player+=1
    check()
    tablescore1["text"]="Your score is: "+str(score_player)
    tablescore2["text"]="Computer score is: "+str(score_com)
def paper():               #1 is rock 2 is paper 3 is scissors
    player_choice=2
    global score_player
    global score_com
    player_choiceimg["image"]=img_player_paper
    comp_choice=random.randint(1,3)
    if comp_choice==2:
        result_label["text"]="TIE Match Draw"
        com_choiceimg["image"]=img_com_paper
    elif comp_choice==3:
        result_label["text"]="You Lost Computer Won"
        com_choiceimg["image"]=img_com_scissor
        score_com+=1
    elif comp_choice==1:
        result_label["text"]="You Won Computer Loses"
        com_choiceimg["image"]=img_com_rock
        score_player+=1
    check()
    tablescore1["text"]="Your score is: "+str(score_player)
    tablescore2["text"]="Computer score is: "+str(score_com)
def scissor():               #1 is rock 2 is paper 3 is scissors
    player_choice=3
    global score_player
    global score_com
    player_choiceimg["image"]=img_player_scissor
    comp_choice=random.randint(1,3)
    if comp_choice==3:
        result_label["text"]="TIE Match Draw"
        com_choiceimg["image"]=img_com_scissor
    elif comp_choice==1:
        result_label["text"]="You Lost Computer Won"
        com_choiceimg["image"]=img_com_rock
        score_com+=1
    elif comp_choice==2:
        result_label["text"]="You Won Computer Loses"
        com_choiceimg["image"]=img_com_paper
        score_player+=1
    check()
    tablescore1["text"]="Your score is: "+str(score_player)
    tablescore2["text"]="Computer score is: "+str(score_com)
#----------------------Window And buttons-------------------------

player_rock=tk.Button(
    image=img_player_rock,
    command=rock,
    )#player button for rock
player_paper=tk.Button(
    image=img_player_paper,
    command=paper,
    )#player button for paper
player_scissor=tk.Button(
    image=img_player_scissor,
    command=scissor,
    )#player button for scissor
result_label=tk.Label(
    font='Arial 12 bold',
    fg="white",
    bg="black",
    text="                                            "#blank
    )
player_choiceimg=tk.Label(
    image=img_blank,
    )
com_choiceimg=tk.Label(
    image=img_blank,
    )
tablescore1=tk.Label(
    text="Your score is:",
    font="Arial 10 bold")
tablescore2=tk.Label(
    text="Computer Score is:",
    font="Arial 10 bold")
player_rock.grid(row=1,column=1,pady=30,padx=30)#image button rock
player_scissor.grid(row=1,column=2,pady=30,padx=30)#image button paper
player_paper.grid(row=1,column=3,pady=30,padx=30)#image button scissor
result_label.grid(row=4,columnspan=3,pady=30,padx=30)#text answer label only
tablescore1.grid(row=5,columnspan=3)#row of table scoreplayer
tablescore2.grid(row=6,columnspan=3)#row of table scorecom
player_choiceimg.grid(row=2,column=1,pady=30,padx=30)#image of choice by player
com_choiceimg.grid(row=2,column=3,pady=30,padx=30)#image of choice by computer
mainwindow.mainloop()#excecute mainwindow