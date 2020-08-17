#Tkinter is used for developing GUI
from tkinter import *
from tkinter import ttk
import random

#create a random new array
#root is the name of the main window object
root = Tk() 
root.title('Sorting Algorithm Visualizer')

#setting the minimum size of the root window
root.minsize(900, 600)

root.config(bg='black')

#variables to select the algorithms
selected_algo = StringVar()

def drawData(data):
    #delete the previous input
    canvas.delete("all")
    #set the canvas dimension
    c_height = 380
    c_width = 900
    #set the bar graph dimension which will be changed bcoz of differebt dataset
    x_width = c_width / (len(data) + 1)
    
    offset = 30
    spacing = 10
    
    #normalize the data to match the bars acc to canvas height
    #normalize would help to make bar heights of (1, 2, 4, 6) same as (10, 20, 40, 60)
    normalizedData = [i / max(data) for i in data] 
    #for i, height in enumerate(data):
    for i, height in enumerate(normalizedData):
        #set top left corner
        x0 = i * x_width + offset + spacing
        #y0 = c_height - height
        y0 = c_height - height * 340
        #set bottom right corner
        x1 = (i+1) * x_width + offset  #this time without spacing
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill="red")
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

def Generate():
    print("Algorithm Selected: " + selected_algo.get()) #get the value selected by user
    #data = [10, 20, 40, 60]
    
    #use try-except if the user do not put any value, insert default instead
    try:
        minValue = int(minEntry.get())
    except:
        minValue = 1
        
    try:    
        maxValue = int(maxEntry.get())
    except:
        maxValue = 100
        
    try:    
        size = int(sizeEntry.get())
    except:
        size = 10
    
    #check for some bugs in advance
    if minValue < 0:
        minValue=0
    if maxValue > 100:
        maxValue=100
    # size > 30 would clutter our space    
    if size > 30 or size < 3: 
        size = 25
    if minValue > maxValue: minValue, maxValue = maxValue, minValue            
        
    data = []  #first create empty dataset
    for _ in range(size):
        data.append(random.randrange(minValue, maxValue+1))
            
    drawData(data)

#frame / base layout
UI_frame = Frame(root, width=900, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=900, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

#User Interface Area
#Row=0
Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algoMenu = ttk.Combobox(UI_frame, textvariable=selected_algo, values=['Bubble Sort', 'Quick Sort', 'Merge Sort'])
algoMenu.grid(row=0, column=1, padx=5, pady=5)
algoMenu.current(0) #Keep the first algo as the default 

#Now put a button beside that
Button(UI_frame, text="Generate", command=Generate, bg='red').grid(row=0, column=2, padx=5, pady=5)

#Row=1
Label(UI_frame, text="Size: ", bg='grey').grid(row=1, column=0, padx=5, pady=5, sticky=W)
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=1, column=1, padx=5, pady=5)

Label(UI_frame, text="Min Value: ", bg='grey').grid(row=1, column=2, padx=5, pady=5, sticky=W)
minEntry = Entry(UI_frame)
minEntry.grid(row=1, column=3, padx=5, pady=5)

Label(UI_frame, text="Max Value: ", bg='grey').grid(row=1, column=4, padx=5, pady=5, sticky=W)
maxEntry = Entry(UI_frame)
maxEntry.grid(row=1, column=5, padx=5, pady=5)

root.mainloop()