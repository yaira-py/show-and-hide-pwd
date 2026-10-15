import tkinter as tk



class Manager:
    def __init__(self,root):
        self.root=root
        self.root.title('password manager')
        self.root.geometry('400x150')
        self.root.configure(bg="#EEEEEE")

        self.title_lb=tk.Label(self.root,text='Enter Password',font=('Arial',15,'bold'),
                               bg='#EEEEEE',fg="#333333")
        self.title_lb.pack(pady=10)

        self.frame=tk.Frame(self.root,bg='#EEEEEE')
        self.frame.pack(pady=10,padx=10)

        self.entry=tk.Entry(self.frame,width=29)
        self.entry.pack(side='left',pady=10,ipady=5,padx=10)

        self.label=tk.Label(self.frame,text='👁️',font=20,bg='#EEEEEE')
        self.label.pack(pady=10,side='left',padx=10)

        self.label.bind('<Button-1>',self.toggle_pass)


    def toggle_pass(self,event=None):
        if self.entry.cget('show')== '*':
            self.entry.config(show='')
            self.label.config(text='🫣')

        else:
            self.entry.config(show='*')
            self.entry.config(text='👁️')








if __name__=="__main__":
    window=tk.Tk()
    app= Manager(window)
    window.mainloop()
