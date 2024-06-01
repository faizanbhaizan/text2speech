# mini project - Text to Speech Converter
# 1. Text to Speech
# 2. PDF Reader

import tkinter #as tk
from tkinter import ttk #GUI
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from gtts import gTTS  
from playsound import playsound
from datetime import datetime
from tkinter import filedialog
import os
import sys

import PyPDF2
import pyttsx3

def read_fun(g):

    try:

        read_val=f.get()
        
        path = open(read_val, 'rb')

        pdfReader = PyPDF2.PdfFileReader(path)

        from_page = pdfReader.getPage(0)


        text = from_page.extractText()

        speak = pyttsx3.init()
        speak.say(text)
        speak.runAndWait()

    except:
        messagebox.showerror("File Not Found","File Not Found, Please Place file under folder")


def open_file():
   filepath = filedialog.askopenfilename(title="Open a Text File", filetypes=(("text    files","*.txt"), ("all files","*.*")))
   file = open(filepath,'rb')
   print(file.read())
   file.close()

def later():
    messagebox.showinfo('Later','This Feature Available Soon')

def text2speechfunc(t):
    
    text_val=p.get()
    #text_val = 'Welcome Mohammad Dayam Ansari'    
    language = 'en'  
    obj = gTTS(text=text_val, lang=language, slow=False)   
    date_string = datetime.now().strftime("%d%m%Y%H%M%S")

    filename = "voice"+date_string+".mp3"

    obj.save(filename)
    playsound(filename)


class tts(tkinter.Tk): 
    
    def __init__(self,*args,**kwargs):
        tkinter.Tk.__init__(self,*args,**kwargs) 
        
        self.geometry('300x600+480+50') 
        
        self.title('Text to Speech Converter')
        
        container=Frame(self) #frame is used to manage the components of the window
        
        container.pack(side="right",fill="both",expand=True) 

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames={}

        for F in (main_screen,main_menu,text2speech,pdf_reader):

            global img
            
            frame=F(container,self)
            frame.configure(bg='white',borderwidth=1)


            self.frames[F]=frame
            #c_label=Label(self,text='Mohd Dayem Ansari - 25',bg='white',fg='blue',borderwidth=0,relief='solid').place(x=95,y=480)
            #m_label=Label(self,text='Md Faizan Ahmed - 23',bg='white',fg='blue',borderwidth=0,relief='solid').place(x=95,y=500)
            frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(main_screen)

    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()

class main_screen(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)

        global tkimage
        global img2alpha

        img=Image.open("GLB.jpg")
        img = img.resize((400,400))
        tkimage = ImageTk.PhotoImage(img)
        img2alpha=Label(self,image=tkimage).place(x=-53,y=0)
        glb_label=Label(self,text='Welcome to GLBITM')

        next_button=Button(self,text="Next ->",fg='blue',bg='white',relief='groove',command=lambda:controller.show_frame(main_menu),font=12).place(x=115,y=425)

class main_menu(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)

        #text to Speech
        mm_menu=Label(self,text='Main Menu',font=12,bg='white',fg='blue',relief='groove').place(x=115,y=20)
        tts_button=Button(self,text='Text to Speech Convertor',relief='groove',wraplength=120,command=lambda:controller.show_frame(text2speech),fg='white',bg='#1338BE',width=8,height=4,font=('helvetica 14 bold')).place(x=20,y=120)
        translate_btn=Button(self,text='PDF Reader',fg='white',bg='green',relief='groove',command=lambda:controller.show_frame(pdf_reader),wraplength=100,width=8,height=4,font=('helvetica 14 bold')).place(x=160,y=120)
        stt_button=Button(self,text='Eng Dictionary',command=later,wraplength=120,fg='white',bg='black',relief='groove',font=('helvetica 14 bold'),width=8,height=4).place(x=90,y=250)
        backbutton2=Button(self,text='Back',fg='white',bg='black',relief='groove',command=lambda:controller.show_frame(main_screen)).place(x=20,y=500)
        
class text2speech(Frame):
    
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)

        global p

        p=StringVar()

        tts2_label=Label(self,text='Text to Speech Converter',bg='white',fg='blue',relief='groove',font=14).place(x=50,y=20)
        backbutton=Button(self,text='Back',fg='white',bg='black',relief='groove',command=lambda:controller.show_frame(main_menu)).place(x=20,y=500)

        user_label=Label(self,text='Text:',bg='white').place(x=20,y=80)
        user_input_text=Entry(self,textvariable=p,borderwidth=2,relief='groove').place(x=20,y=140)
        w=p.get()
        arrow=Button(self,text='->',command=lambda:text2speechfunc(w),bg='white',borderwidth=1,relief='groove').place(x=160,y=140)
        
class pdf_reader(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)

        #text to Speech

        global f
        f=StringVar()
        
        mm_menu=Label(self,text='PDF Reader',font=12,bg='white',fg='blue',relief='groove').place(x=115,y=20)
        abc=Label(self,text='Enter File Name :').place(x=20,y=80)
        abc2=Entry(self,textvariable=f,borderwidth=2,relief='groove').place(x=20,y=140)
        abc2btn=Button(self,text='->',command=lambda:read_fun(f),bg='white',borderwidth=1,relief='groove').place(x=160,y=140)
        backbutton2=Button(self,text='Back',fg='white',bg='black',relief='groove',command=lambda:controller.show_frame(main_menu)).place(x=20,y=500)
    
app = tts()
app.mainloop()
