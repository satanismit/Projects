from tkinter import*
from PIL import Image,ImageTk
import speech_to_text, action,text_to_speech

root=Tk()
root.title("Virtual Smit")
root.geometry("700x750")
root.resizable(False,False)
root.configure(bg="Orange",cursor="hand2")

def ask():
    user_val=speech_to_text.speech_to_text()
    bot_val=action.Action(user_val)
    text.insert(END, "User-->   "+user_val+"\n")
    text.insert(END, "Bot-->   "+str(bot_val)+"\n")
    if bot_val=="Shutting down":
        root.destroy()

def send():
    user=entry.get() 
    bot=action.Action(user) 
    text.insert(END, "User-->   "+user+"\n")
    text.insert(END, "Bot-->   "+str(bot)+"\n")
    if bot=="Shutting down":
        root.destroy()

def delete():
    text.delete(1.0, END)
    entry.delete(0, END)
    
def exit():
    root.quit()

# frame 
frame=LabelFrame(root,bg="white" ,padx=100,pady=10,relief="sunken")
frame.config(bg="orange")  
frame.grid(row=0, column=1, padx=55, pady=10)

# text label
text_label=Label(frame,text="Virtual Smit",font=("Arial",20),bg="white")
text_label.grid(row=0,column=0,columnspan=2)

#image
image=Image.open("virtual_assistant/VA.png")
photo=ImageTk.PhotoImage(image)
image_label=Label(frame,image=photo)
image_label.grid(row=1,column=0, pady=20)


# adding a text widget 
text= Text(root, font=("Arial", 10), bg="orange")
text.grid(row=2, column=0)
text.place(x=50, y=400, height=100, width=630)

# entry widget
entry=Entry(root, font=("Arial", 20), justify="center")
entry.grid(row=3, column=0)
entry.place(x=200, y=525, height=50, width=375)

# button 1
button1=Button(root,text="Speak",font=("Arial", 20),bg="white",borderwidth=5,command=ask)
button1.grid(row=4,column=0)
button1.place(x=100, y=600, height=50, width=175)

# button 2
button2=Button(root,text="Send",font=("Arial", 20),bg="white",borderwidth=5,command=send)      
button2.grid(row=5,column=0)
button2.place(x=300, y=600, height=50, width=175)

# button 3
button3=Button(root,text="Delete",font=("Arial", 20),bg="white",borderwidth=5, command=delete)  
button3.grid(row=6,column=0)
button3.place(x=500, y=600, height=50, width=175)

# button 4
button4=Button(root,text="Exit",font=("Arial", 20),bg="white",borderwidth=5,command=exit)
button4.grid(row=7,column=0)
button4.place(x=300, y=675, height=50, width=175)

text_to_speech.text_to_speech("Hello Smit, How can i help you ?")
root.mainloop()

