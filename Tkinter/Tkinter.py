from tkinter import *

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("First Tkinter GUI")
        self.root.iconbitmap()
        self.root.geometry("400x400")
        self.root.configure(bg = "#8C6962")


        self.login_gui()


        self.root.mainloop()


    def login_gui(self):
       
       self.clear()
        
       hadding = Label(self.root, text= 'First GUI App', bg='#8C6962', fg = 'white')
       hadding.pack(pady=(30,30))
       hadding.configure(font=('verdana', 24, 'bold'))

       lable1 = Label(self.root,text="enter your mail")
       lable1.pack(pady=(10,10))

       self.email_input = Entry(self.root, width = 30)
       self.email_input.pack(pady=(5, 10), ipady=3)

       lable2 = Label(self.root,text="enter your password")
       lable2.pack(pady=(10,10))

       self.password_input = Entry(self.root, width = 30, show='*') #cant give height perameter to entery 
       self.password_input.pack(pady=(5, 10), ipady=3)

       login_but = Button(self.root, text='Login', width=30, height=3) # you can give height parameter to button
       login_but.pack(pady=(10,10))

       
       lable3 = Label(self.root,text="not a member")
       lable3.pack(pady=(20,10))

       redirect_but = Button(self.root, text='register now', width=30, height=3, command=self.register_gui) # you can give height parameter to button
       redirect_but.pack(pady=(10,10))


    def register_gui(self):
       self.clear()

       hadding = Label(self.root, text= 'First GUI App', bg='#8C6962', fg = 'white')
       hadding.pack(pady=(30,30))
       hadding.configure(font=('verdana', 24, 'bold'))

       lable10 = Label(self.root,text="enter name")
       lable10.pack(pady=(10,10))

       self.name_input = Entry(self.root, width = 30)
       self.name_input.pack(pady=(5, 10), ipady=3)

       lable1 = Label(self.root,text="enter your mail")
       lable1.pack(pady=(10,10))

       self.email_input = Entry(self.root, width = 30)
       self.email_input.pack(pady=(5, 10), ipady=3)

       lable2 = Label(self.root,text="enter your password")
       lable2.pack(pady=(10,10))

       self.password_input = Entry(self.root, width = 30, show='*') #cant give height perameter to entery 
       self.password_input.pack(pady=(5, 10), ipady=3)

       register_but = Button(self.root, text='registe', width=30, height=3) # you can give height parameter to button
       register_but.pack(pady=(10,10))

       
       lable3 = Label(self.root,text="already a member")
       lable3.pack(pady=(20,10))

       redirect_but = Button(self.root, text='login now', width=30, height=3, command=self.login_gui) # you can give height parameter to button
       redirect_but.pack(pady=(10,10))




    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

app = App()