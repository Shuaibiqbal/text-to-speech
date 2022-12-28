## import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound



################### Initialized window####################

root = Tk()
root.geometry('350x300')
root.resizable(0,0)
root.config(bg = 'ghost white')
root.title('TEXT-TO-SPEECH')


##heading
# Label(root, text = 'TEXT_TO-SPEECH' , font='arial 20 bold' , bg ='white smoke').pack()
Label(root, text ='' , font ='Times 15 bold', bg = 'white smoke').pack(side = BOTTOM)




#label
Label(root, text ='Enter Text', font ='Times 15 bold', bg ='white smoke').place(x=20,y=60)


##text variable
Msg = StringVar()


#Entry
entry_field = Entry(root,textvariable =Msg, width ='50')
entry_field.place(x=20 , y=100)


###################define function##############################

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('audio.mp3')
    playsound('audio.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

#Button
Button(root, text = "PLAY" , font = 'Times 15 bold', command = Text_to_speech, width =4).place(x=25, y=140)
Button(root,text = 'EXIT',font = 'Times 15 bold' , command = Exit, bg = 'OrangeRed1').place(x=100,y=140)
Button(root, text = 'RESET', font='Times 15 bold', command = Reset).place(x=175 , y =140)


#infinite loop to run program
root.mainloop()
