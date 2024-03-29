# Stuarrt Boekelman - 3/28/24
# PokeBot program for Sword/Shield Versions

# Library imports
import tkinter as tk
import subprocess
import pydirectinput
import pyautogui
import time
import os
import sys

# Function to create Pokemon/Modify Save files
def createPokemon():
    pkhex = "PKHeX.exe"
    global popWindowCR
    popWindowCR = tk.Toplevel()
    popWindowCR.title("Creating Pokémon")
    global pkhexWindow 
    pkhexWindow = subprocess.Popen([pkhex])
    endpkhex = tk.Button(popWindowCR, text="Click me when you finish saving your Pokémon", command=closePKHEX)
    endpkhex.pack()

# Function to close PKHex
def closePKHEX():
    global pkhexWindow
    global popWindowCR
    if pkhexWindow and pkhexWindow.poll() is None:
        pkhexWindow.terminate() 
    popWindowCR.destroy()

# Bot commands for Game
def botProcess():
    global ryuWindow
    global entry
    localMode = ["e", "u", "f"]
    ryuWindow = entry.get()
    try:
        pyautogui.press("win") 
        pyautogui.typewrite(ryuWindow)
        time.sleep(5) 
        pyautogui.press("enter")
    except Exception as e:
        print("An error occurred, please restart the program.", e)
    time.sleep(50)
    pyautogui.moveTo(950, 470)
    pyautogui.click()
    pydirectinput.press("z")
    pydirectinput.press("z")
    pydirectinput.press("z")
    pydirectinput.press("z")
    pydirectinput.press("z")
    time.sleep(10)
    pydirectinput.press("c")
    time.sleep(2)
    pydirectinput.press("d")
    pydirectinput.press("d")
    pydirectinput.press("d")
    pydirectinput.press("s")
    pydirectinput.press("z")
    time.sleep(2)
    for key in localMode:
        pydirectinput.keyDown(key)
    time.sleep(0.1)
    for key in localMode:
        pydirectinput.keyUp(key)
    time.sleep(20)
    pydirectinput.press("z")
    time.sleep(2)
    pydirectinput.press("x")
    time.sleep(2)
    pydirectinput.press("x")
    time.sleep(2)
    pydirectinput.press("x")
    pydirectinput.press("v")
    time.sleep(2)
    pydirectinput.press("z")
    time.sleep(5)
    pydirectinput.press("s")
    pydirectinput.press("z")
    time.sleep(5)
    pydirectinput.press("z")
    time.sleep(2)
    pydirectinput.press("7")
    pydirectinput.press("5")
    pydirectinput.press("3")
    pydirectinput.press("9")
    pydirectinput.press("1")
    pydirectinput.press("4")
    pydirectinput.press("6")
    pydirectinput.press("2")
    pydirectinput.press("enter")
    time.sleep(2)
    pydirectinput.press("z")
    time.sleep(2)
    pydirectinput.press("z")
    time.sleep(2)
    pydirectinput.press("z")
    time.sleep(2)
    pydirectinput.press("z")
    time.sleep(2)
    pydirectinput.press("z")
    time.sleep(2)
    pydirectinput.press("z")
    time.sleep(2)
    pydirectinput.press("z")
    time.sleep(2)
    pydirectinput.press("z")
    time.sleep(2)
    pydirectinput.press("z")
    time.sleep(30)
    pydirectinput.press("z")
    time.sleep(5)
    pydirectinput.press("z")
    time.sleep(15)
    pydirectinput.press("z")
    time.sleep(2)
    pydirectinput.press("z")
    time.sleep(2)
    pydirectinput.press("z")
    time.sleep(2)
    pydirectinput.press("z")
    pydirectinput.press("z")
    pydirectinput.press("z")
    pydirectinput.press("z")
    time.sleep(30)
    pydirectinput.press("x")
    time.sleep(2)
    pydirectinput.press("x")
    time.sleep(2)
    pydirectinput.press("x")
    time.sleep(2)
    pydirectinput.press("x")
    time.sleep(2)
    pydirectinput.press("x")
    time.sleep(2)
    pydirectinput.press("c")
    pydirectinput.press("w")
    pydirectinput.press("z")
    time.sleep(2)
    pydirectinput.press("z")
    time.sleep(2)
    pydirectinput.press("z")

# Function to start Pokemon Export
def exportPokemon():
    global popWindowEXP
    popWindowEXP = tk.Tk()
    popWindowEXP.title("Initiate Trade")
    label = tk.Label(popWindowEXP, text="Enter your game path")
    label.pack()
    global entry
    entry = tk.Entry(popWindowEXP)
    entry.pack()
    label2 = tk.Label(popWindowEXP, text="Eight Digit Trade Code is: 75391462")
    label2.pack()
    submitButton = tk.Button(popWindowEXP, text="Submit", command=botProcess)
    submitButton.pack()
    endTrade = tk.Button(popWindowEXP, text="Click me when your trade is over", command=closeRYU)
    endTrade.pack()

# Function to finish trade/close emulator
def closeRYU():
    global popWindowEXP
    global ryuWindow
    if ryuWindow is not None:
        os.system("taskkill /f /im Ryujinx.exe")
    if popWindowEXP is not None:
        popWindowEXP.destroy()
    
# Function to terminate program when finished
def endProgram():
    global window
    if window is not None:
        window.destroy()
    sys.exit(0)

# Main Windows, buttons and initilization of program.
global window
window = tk.Tk()
window.title("Pokémon Sysbot")

# Buttons 
create_button = tk.Button(window, text="Create Pokémon", command=createPokemon)
create_button.pack()

trade_button = tk.Button(window, text="Export Pokémon", command=exportPokemon)
trade_button.pack()

stopProgram = tk.Button(window, text="Quit", command=endProgram)
stopProgram.pack()


window.mainloop()
