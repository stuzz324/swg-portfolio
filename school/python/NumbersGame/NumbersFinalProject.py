'''
Author: Shawn Gallagher
Date: 12/14/2022
Purpose: A number based guessing game where the player must guess a secret number from a range.
'''
import tkinter
import tkinter.messagebox
import random

#creating a GUI class for easy manupulation.
class GameBoardGUI:
    def __init__(self):
        '''
        __init__ method will be used to call multiple 'build' functions in order to 
        improve flexability of developement.

        __init__ will also contain the tkinter.mainloop().
        '''
        self.__buildGameBoard()
        self.__buildMenu()
        #self.__dp()
        self.__gameInit()
        tkinter.mainloop()

    def __buildGameBoard(self):
        self.__gameBoard = tkinter.Tk()
        self.__gameBoard.geometry('600x600')
        self.__gameBoard.title('Number Guesser!')
        '''FRAMES'''
        #actual play area containing the Listbox showing available guesses
        self.__cbFrame = tkinter.Frame(self.__gameBoard)
        self.__playFrame = tkinter.Frame(self.__gameBoard,borderwidth=6,relief='ridge')
        self.__playFrame.pack(side='top')
        #confirm guess button frame
        self.__cbFrame.pack(side='top')
        #question buttons frame
        self.__qbFrame = tkinter.Frame(self.__gameBoard)
        self.__qbFrame.pack(side='top')
        
        '''WIDGETS'''
        #call Listbox function
        self.__buildListbox()
        
        self.__confirmGuess = tkinter.Button(self.__cbFrame,text='Confirm Guess',command=self.__guessChecker)
        self.__confirmGuess.pack(side='left')
        #turn count label and IntVar
        self.__turnLabel = tkinter.Label(self.__cbFrame,text='Turns Left:')
        self.__turnLabel.pack(side='left')
        self.__turnVar = tkinter.IntVar(self.__cbFrame)
        self.__tcLabel = tkinter.Label(self.__cbFrame,textvariable=self.__turnVar)
        self.__tcLabel.pack(side='left')
        #Is it even or odd?
        self.__evenOrOddB = tkinter.Button(self.__qbFrame,text='Even or Odd?',command=self.__evenOrOdd)
        self.__evenOrOddB.pack(side='top')
        #Greater than or less than n?
        self.__gorlB = tkinter.Button(self.__qbFrame,text='Is it > or < n?',command=self.__isItGorL)
        self.__gorlB.pack(side='top')

    def __buildMenu(self):
        '''MAIN MENU'''
        self.__menu = tkinter.Menu(self.__gameBoard)
        self.__gameBoard.config(menu=self.__menu)
        '''FILE MENU'''
        #file menu for quit and new game
        self.__fileMenu = tkinter.Menu(self.__menu)
        self.__menu.add_cascade(label='File',menu=self.__fileMenu)
        #new game and quit options
        self.__fileMenu.add_command(label='New Game',command=self.__gameInit)
        self.__fileMenu.add_command(label='Quit',command=self.__gameBoard.destroy)
        '''GAME OPTIONS MENU'''
        self.__optMenu = tkinter.Menu(self.__menu)
        self.__menu.add_cascade(label='Options',menu=self.__optMenu)
        #change range
        self.__dropdown = tkinter.Menu(self.__optMenu)
        self.__optMenu.add_cascade(label='Change Range...',menu=self.__dropdown)
        self.radVar = tkinter.IntVar(self.__gameBoard)
        #used to set range in __gameInit
        self.radVar.set(20)
        self.__dropdown.add_radiobutton(label='20',value=20,variable=self.radVar)
        self.__dropdown.add_radiobutton(label='30',value=30,variable=self.radVar)
        self.__dropdown.add_radiobutton(label='40',value=40,variable=self.radVar)
    #gRange argument to allow Options menu to manipulate
    def __gameInit(self):    
        '''
        In __gameInit, declare variables and initialize them. Probably
        a range variable to set the # of iterations when generating the 
        list of numbers, the secret number you are trying to guess,
        and the list of numbers itself.

        The list will basically control the Listbox conatining numbers when it is instantiated.
        '''
        #assign __range to a default value of 20, can be changed in cascading menu bar
        self.__range = self.radVar.get()
        #clear rlist, guessesList, and turnCount
        self.__rlist = []
        self.__guessesList.delete(0,tkinter.END)
        #chooses the appropriate number of turns based off of range
        if self.__range == 20:
            self.__turnCount = 4
        elif self.__range == 30:
            self.__turnCount = 6
        elif self.__range == 40:
            self.__turnCount = 8
        self.__turnVar.set(self.__turnCount)
        #reset buttons
        self.__confirmGuess['state'] = 'normal'
        self.__evenOrOddB['state'] = 'normal'
        self.__gorlB['state'] = 'normal'
        #populate list and Listbox
        for listAdd in range(1, self.__range+1):
            self.__rlist.append(listAdd)
            self.__guessesList.insert(tkinter.END, listAdd)
        #choose a random number from that list
        self.__secretNum = random.choice(self.__rlist)
        #debug IntVar
        #self.dpSecretVar.set(value=self.__secretNum)
    
    def __buildListbox(self):
        '''Self contained build function for a listbox.'''
        #create own frame for guess list?
        self.__guessesList = tkinter.Listbox(self.__playFrame, selectmode='SINGLE',height=20)
        self.__guessesList.pack(side='left')
        self.__gScroll = tkinter.Scrollbar(self.__playFrame)
        self.__gScroll.pack(side='left', fill=tkinter.Y)

    def __dp(self):
        '''
        DEBUG PANEL
        Used to show the secret number and implements a reroll button.
        '''
        self.dpFrame = tkinter.Frame(self.__gameBoard)
        self.dpFrame.pack(side='right')

        self.dpSecretVar = tkinter.IntVar(self.__gameBoard)
        
        self.dpSNum = tkinter.Label(self.dpFrame, textvariable=self.dpSecretVar)
        self.dpSNum.pack(side='top')
        #debug reroll button
        self.dpReroll = tkinter.Button(self.dpFrame, text='Reroll', command=self.__gameInit)
        self.dpReroll.pack(side='top')

    def __guessChecker(self):
        '''CHECKS GUESSES THROUGH DECISION STRUCTURES'''
        try:
            #update turn count
            self.__turnCount -= 1
            self.__turnVar.set(self.__turnCount)
            #create curselection to remove items from Listbox
            self.__gIndex = self.__guessesList.curselection()
            self.__guessNum = self.__guessesList.get(self.__gIndex)
            #if statement for winning, also disables the confirm guess button
            if self.__guessNum == self.__secretNum:
                self.__confirmGuess['state'] = 'disable'
                tkinter.messagebox.showinfo('Yay!','You guessed the secret number!')
            elif self.__turnCount == 0:
                self.__confirmGuess['state'] = 'disable'
                tkinter.messagebox.showinfo('You lose!',f"You've run out of turns! The secret number was {self.__secretNum}!")
            #checks for cold or hot
            elif self.__secretNum-3 <= self.__guessNum <= self.__secretNum+3:    
                for guess in self.__gIndex:
                    self.__guessesList.itemconfig(guess, bg='red')
            elif self.__secretNum-6 <= self.__guessNum <= self.__secretNum+6:    
                for guess in self.__gIndex:
                    self.__guessesList.itemconfig(guess, bg='orange')
            elif self.__secretNum-9 <= self.__guessNum <= self.__secretNum+9:    
                for guess in self.__gIndex:
                    self.__guessesList.itemconfig(guess, bg='cyan')
        except tkinter.TclError:
            #maybe create StringVar and a label to update guesses to display error there
            tkinter.messagebox.showinfo('Error!','You must select a guess!')
            
    def __evenOrOdd(self):
        '''Even or Odd callback function.'''
        self.__evenOrOddB['state'] = 'disabled'
        self.__gorlB['state'] = 'disabled'
        #if it is even
        if self.__secretNum % 2 == 0:
            tkinter.messagebox.showinfo('Even or Odd?', 'The secret number is even!')
            for strike in range(0,self.__range,2):
                self.__guessesList.itemconfig(strike, fg='grey')
        #if it is odd
        else:
            tkinter.messagebox.showinfo('Even or Odd?', 'The secret number is odd!')
            for strike in range(1,self.__range,2):
                self.__guessesList.itemconfig(strike,fg='grey')
        
    def __isItGorL(self):
        '''Greater or Less callback function.'''
        try:
            self.__gIndex = self.__guessesList.curselection()
            self.__guessNum = self.__guessesList.get(self.__gIndex)
            self.__evenOrOddB['state'] = 'disabled'
            self.__gorlB['state'] = 'disabled'
            #using self.__guessNum from self.__guessChecker
            if self.__secretNum < self.__guessNum:
                tkinter.messagebox.showinfo('> or < n?',f'The secret number is less than {self.__guessNum}!')
                for strike in range(self.__guessNum,self.__range):
                    self.__guessesList.itemconfig(strike,fg='grey')
            elif self.__secretNum > self.__guessNum:
                tkinter.messagebox.showinfo('> or < n?',f'The secret number is greater than {self.__guessNum}!')
                for strike in range(0,self.__guessNum):
                    self.__guessesList.itemconfig(strike,fg='grey')
        except tkinter.TclError:
            tkinter.messagebox.showinfo('Error!','You must select a guess!')

if __name__ == '__main__':
    #create the gb1 object
    gb1 = GameBoardGUI()