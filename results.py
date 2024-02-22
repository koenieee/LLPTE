from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt

class Table:
   
    def __init__(self,root):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])





def show_results():
    # x axis values
    x = [1,2,3]
    # corresponding y axis values
    y = [2,4,1]
     
    # plotting the points 
    plt.plot(x, y)
     
    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')
     
    # giving a title to my graph
    plt.title('My first graph!')
     
    # function to show the plot
    plt.show()
    
    
 
def show_table_precision_recall():
    # take the data
    lst = [(1,'Raj','Mumbai',19),
           (2,'Aaryan','Pune',18),
           (3,'Vaishnavi','Mumbai',20),
           (4,'Rachna','Mumbai',21),
           (5,'Shubham','Delhi',21)]
      
    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])
      
    # create root window
    root = Tk()
    t = Table(root)
    root.mainloop()
        


