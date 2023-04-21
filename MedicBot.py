from tkinter import *
root = Tk()
root.title("Medic Chatbot")
def send():
    send = "You -> "+e.get()
    txt.insert(END, "\n" + send)
    user = e.get().lower()
    if(user == "hello"):
         txt.insert(END, "\n" + "\n Bot -> Hi\n")
    elif(user == "hi" or user == "hii" or user == "hiiii"):
        txt.insert(END, "\n" + "\nBot -> Hello\n")
    elif(user == "your creator" or user == "who created you" or user == "creator"):
        txt.insert(END, "\n" + "\nBot -> I am created by group 8 members \n Ritwik Shukla\nPradeep Vishwakarma\nRajkumar Yadav")      
    elif(e.get() == "how are you"):
        txt.insert(END, "\n" + "\nBot -> fine! and you\n")
    elif(user == "fine" or user == "i am good" or user == "i am doing good\n"):
        txt.insert(END, "\n" + "\nBot -> Great! how can I help you.\n")
    elif(user == "i have headache" or user == "headache" or user == "medicine for headache"):
        txt.insert(END, "\n" + "Bot -> you should take rest and medicine like dolo,paracetamol\n contact doctor as soon as possible\n")
    elif(user == "vomit" or user == "vomiting" or user == "uneasy"):
        txt.insert(END, "\n" + "\nBot -> Pepto-Bismol\n Over-the-counter (OTC) medications to stop vomiting (antiemetics)\n contact doctorif possible\n")
    elif(user == "i have cough" or user == "coughing" or user == "coughing medicicine"):
        txt.insert(END, "\n" + "\nBot -> dry cough or wet cough\n")   
    elif(user == "Dry" or user == "dry cough" or user == "i have dry cough"):
        txt.insert(END, "\n" + "\nBot -> take rest\n medicine like koflet\n  take hot beverage like Hot tea,coffee etc\n")
    elif(user == "i have wet cough" or user == "wet cough" or user == "wet"):
        txt.insert(END, "\n" + "\nBot -> take rest \n use koflet\n")
    elif(user == "i have fever" or user == "cold" or user == "medicine for fever"):
        txt.insert(END, "\n" + "\nBot -> you should take rest\n  medicine like dolo,paracetamol or acylopara etc\n contact doctor as soon as possible\n")
    elif(user == "i have mouth ulcer" or user == "toung ulcer" or user == "mouth ulcer"):
        txt.insert(END, "\n" + "\nBot -> eat cold things to treat ulcer\n orasore medicine\n do not hot things for eating and drinking")                 
    else:
        txt.insert(END, "\n" + "\nBot -> Sorry! I dind't got you")
    e.delete(0, END)
txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
e.grid(row=1, column=0)
send = Button(root, text="Send", command=send).grid(row=1, column=1)
root.mainloop()
