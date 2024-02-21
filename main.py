#https://www.analyticsvidhya.com/blog/2020/09/precision-recall-machine-learning/

from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import openai
import os



class Table:
     
    def __init__(self,root):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])



def setup_llm():
    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
    )



def ask_llm_to_convert():



    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model="gpt-3.5-turbo",
    )


def show_verification_question():
    # object of TK()
    main = Tk()
     
    # function to use the 
    # askquestion() function
    def Submit(): 
        messagebox.askquestion("Form",
                               "Do you want to Submit")
         
    # setting geometry of window 
    # instance
    main.geometry("100x100")
     
    # creating Window
    B1 = Button(main, text = "Submit", command = Submit) 
     
    # Button positioning 
    B1.pack()   
     
    # infinite loop till close
    main.mainloop()  



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
        
    
def multiple_times():
    ask_llm_to_convert()
    show_verification_question()
    
def main():
    setup_llm()
    multiple_times()
    show_results()

if __name__ == "__main__":
    main()