#!/usr/bin/env python
# coding: utf-8

import tkinter as tk
import math
import time
import random


# processing

def run_grammar(A_grammar, B_grammar, C_grammar, D_grammar, start, iters):
    grammar = start
    AA_grammar = get_older(A_grammar)
    AAA_grammar = get_older(AA_grammar)
    for _ in range(iters):
        new_grammar = ""
        for i in range(len(grammar)):
            if grammar[i] == "A":
                new_grammar += A_grammar
            elif grammar[i] == "1":
                new_grammar += AA_grammar
            elif grammar[i] == "2":
                new_grammar += AAA_grammar
            elif grammar[i] == "B":
                new_grammar += B_grammar
            elif grammar[i] == "C":
                new_grammar += C_grammar
            elif grammar[i] == "D":
                new_grammar += D_grammar
            elif grammar[i] == "[" or grammar[i] == "]" or grammar[i] == "(" or grammar[i] == ")":
                new_grammar += grammar[i]
        grammar = new_grammar
        print("new grammar is", new_grammar)
        grammar = get_older(grammar)
        print("older new grammar is now", grammar)
    return grammar

def get_older(grammar):
    new_grammar = ""
    for i in range(len(grammar)):
        if grammar[i] == "A":
            new_grammar += "1"
        elif grammar[i] == "1":
            new_grammar += "2"
        else:
            new_grammar += grammar[i]
    return new_grammar

def validate_grammar(grammar):
    new_grammar = ""
    valid_chars = ["A", "B", "C", "D", "(", "[", ")", "]", "1", "2"]
    i = 0
    while i < len(grammar):
        if grammar[i] not in valid_chars:
            i += 1
            continue
        if i < len(grammar)-1:
            if grammar[i]==")" and grammar[i+1]=="(":
                i += 2
                continue
            if grammar[i]=="]" and grammar[i+1]=="[":
                i += 2
                continue
        new_grammar += grammar[i]
        i += 1
    print("validated ", grammar, " into ", new_grammar)
    return new_grammar
        

def draw_section(canvas, grammar, index, start, angle):
    current = start  # current point from which we draw
    while index != len(grammar) and grammar[index]!="]" and grammar[index]!=")":
        if grammar[index] == "A":
            current = draw_stem(canvas, current, angle, 3)
        elif grammar[index] == "1":
            current = draw_stem(canvas, current, angle, 5)
        elif grammar[index] == "2":
            current = draw_stem(canvas, current, angle, 7)
        elif grammar[index] == "B":
            current = draw_left_leaf(canvas, current, angle)
        elif grammar[index] == "C":
            current = draw_right_leaf(canvas, current, angle)
        elif grammar[index] == "D":
            current = draw_flower(canvas, current)
        elif grammar[index] == "(":
            index = draw_section(canvas, grammar, index+1, current, angle-30)
        elif grammar[index] == "[":
            index = draw_section(canvas, grammar, index+1, current, angle+30)
        index += 1
    return index
            
    
def draw_stem(canvas, point, angle, width):
    stem_len = 20
    x1 = point[0]
    y1 = point[1]
    x2 = point[0] - stem_len*math.sin(math.radians(angle))
    y2 = point[1] - stem_len*math.cos(math.radians(angle))
    canvas.after(delay)
    canvas.update()
    canvas.create_line(x1, y1, x2, y2, fill="green", width=width)
    return (x2, y2)

def draw_left_leaf(canvas, point, angle):
    angle += 45
    leaf_len = 15
    x1 = point[0]
    y1 = point[1]
    x2 = point[0] - leaf_len*math.sin(math.radians(angle))
    y2 = point[1] - leaf_len*math.cos(math.radians(angle))
    canvas.after(delay)
    canvas.update()
    canvas.create_line(x1, y1, x2, y2, fill="lightgreen", width=3)
    return point

def draw_right_leaf(canvas, point, angle):
    angle -= 45
    leaf_len = 15
    x1 = point[0]
    y1 = point[1]
    x2 = point[0] - leaf_len*math.sin(math.radians(angle))
    y2 = point[1] - leaf_len*math.cos(math.radians(angle))
    canvas.after(delay)
    canvas.update()
    canvas.create_line(x1, y1, x2, y2, fill="lightgreen", width=3)
    return point

def draw_flower(canvas, point):
    radius = 5
    x1 = point[0] - radius
    y1 = point[1] - radius
    x2 = point[0] + radius
    y2 = point[1] + radius
    canvas.after(delay)
    canvas.update()
    canvas.create_oval(x1, y1, x2, y2, fill="red", outline="red")
    return point

# button functions

def clear_canvas(canvas, entryA, entryB, entryC, entryD, entryS):
    canvas.delete("all")
    
def close_application(window):
    window.destroy()
    
def draw(canvas, entryA, entryB, entryC, entryD, entryS, picker):
    inputA = entryA.get()
    inputA = inputA.upper()
    inputB = entryB.get()
    inputB = inputB.upper()
    inputC = entryC.get()
    inputC = inputC.upper()
    inputD = entryD.get()
    inputD = inputD.upper()
    start = entryS.get()
    start = start.upper()
    iterations = int(picker.get())
    grammar = run_grammar(inputA, inputB, inputC, inputD, start, iterations)
    grammar = validate_grammar(grammar)
    start = (200,300)
    draw_section(canvas, grammar, 0, start, 0)
    
def meadow(canvas):
    # flower 1
    grammar = run_grammar("A", "A[B]AA(B)C", "(AD)", "D", "B", random.randint(3, 4))
    grammar = validate_grammar(grammar)
    start = (80,300)
    draw_section(canvas, grammar, 0, start, 0)
    
    # flower 2
    grammar = run_grammar("A", "AB[AB]A(B)", "", "", "B", random.randint(2, 3))
    grammar = validate_grammar(grammar)
    start = (150,300)
    draw_section(canvas, grammar, 0, start, 0)
    
    # flower 3
    grammar = run_grammar("A", "A[AB]A(AB)CD", "AC", "D", "B", random.randint(2, 4))
    grammar = validate_grammar(grammar)
    start = (220,300)
    draw_section(canvas, grammar, 0, start, 0)
    
    # flower 4
    grammar = run_grammar("A[B](B)", "AC(B)[ABC]", "A", "", "A", random.randint(2, 4))
    grammar = validate_grammar(grammar)
    start = (290,300)
    draw_section(canvas, grammar, 0, start, 0)


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Procedural Modeling")

    delay = 100
    canvas_width = 400
    canvas_height = 300

    left_panel = tk.Frame(window, width=200)
    left_panel.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="nsew")
    window.grid_columnconfigure(0, weight=1)
    
    labelA = tk.Label(left_panel, text="A:")
    labelA.grid(row=0, column=0, sticky="ew", pady=5)
    entryA = tk.Entry(left_panel)
    entryA.grid(row=0, column=1, sticky="e", pady=5)
    
    labelB = tk.Label(left_panel, text="B:")
    labelB.grid(row=1, column=0, sticky="ew", pady=5)
    entryB = tk.Entry(left_panel)
    entryB.grid(row=1, column=1, sticky="e", pady=5)
    
    labelC = tk.Label(left_panel, text="C:")
    labelC.grid(row=2, column=0, sticky="ew", pady=5)
    entryC = tk.Entry(left_panel)
    entryC.grid(row=2, column=1, sticky="e", pady=5)
    
    labelD = tk.Label(left_panel, text="D:")
    labelD.grid(row=3, column=0, sticky="ew", pady=5)
    entryD = tk.Entry(left_panel)
    entryD.grid(row=3, column=1, sticky="e", pady=5)
    
    labelS = tk.Label(left_panel, text="Start with:")
    labelS.grid(row=4, column=0, sticky="ew", pady=5)
    entryS = tk.Entry(left_panel)
    entryS.grid(row=4, column=1, sticky="e", pady=5)
    
    label_number = tk.Label(left_panel, text="Iterations:")
    label_number.grid(row=5, column=0, sticky="ew", pady=5)
    number_picker = tk.Spinbox(left_panel, from_=1, to=10)
    number_picker.grid(row=5, column=1, sticky="e", pady=5)

    canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="white")
    canvas.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")
    window.grid_columnconfigure(1, weight=1)
    
    submit_button = tk.Button(left_panel, text="Submit", command=lambda: draw(canvas, entryA, entryB, entryC, entryD, entryS, number_picker))
    meadow_button = tk.Button(left_panel, text="Meadow", command=lambda: meadow(canvas))
    clear_button = tk.Button(left_panel, text="Clear", command=lambda: clear_canvas(canvas, entryA, entryB, entryC, entryD, entryS))
    close_button = tk.Button(left_panel, text="Close", command=lambda: close_application(window))
    
    submit_button.grid(row=6, column=0, columnspan=2, sticky="ew")
    meadow_button.grid(row=7, column=0, columnspan=2, sticky="ew")
    clear_button.grid(row=8, column=0, columnspan=2, sticky="ew")
    close_button.grid(row=9, column=0, columnspan=2, sticky="ew")
    
    window.mainloop()



