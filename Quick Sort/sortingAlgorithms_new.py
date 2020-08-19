#Tkinter is used for developing GUI
from tkinter import *
from tkinter import ttk
import random
from BubbleSort import bubble_sort
from QuickSort import quick_sort

#create a random new array
#root is the name of the main window object
root = Tk() 
root.title('Sorting Algorithm Visualizer')

#setting the minimum size of the root window
root.minsize(900, 600)

root.config(bg='black')

#variables to select the algorithms
selected_algo = StringVar()
data = [] #make data global since we are using two buttons for generating and starting algo

def drawData(data, colorArray):
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
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    
    root.update_idletasks()    

def Generate():
    global data    #to access global data
    minValue = int(minEntry.get())
    maxValue = int(maxEntry.get())
    size = int(sizeEntry.get())
    
    data = []  #first create empty dataset
    for _ in range(size):
        data.append(random.randrange(minValue, maxValue+1))
            
    drawData(data, ['red' for x in range(len(data))])
    

def StartAlgorithm():
    global data 
    
    if not data:
        return
    
    if (algoMenu.get() == 'Quick Sort'):
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
        drawData(data, ['green' for x in range(len(data))])
        
    elif (algoMenu.get() == 'Bubble Sort'):  
        bubble_sort(data, drawData, speedScale.get())

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

#Instead of button we'll put a slider
speedScale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
speedScale.grid(row=0, column=2, padx=5, pady=5)

Button(UI_frame, text="Start", command=StartAlgorithm, bg='red').grid(row=0, column=3, padx=5, pady=5)

#Row=1
sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text="Generate", command=Generate, bg='white').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()