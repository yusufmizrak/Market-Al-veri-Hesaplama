from tkinter import*
win=Tk()

def hesapla():
    sonuc=int(e3.get())*int(e4.get())
    messagebox.showinfo("sonuc","{} {} ad ve soyadlı kişinin hesabı:{}"
                        .format(e1.get(),e2.get(),sonuc))

l1=Label(win,text="adını gir:").place(x=30, y=10)
e1=Entry(win)
e1.place(x=100,y=10)

l2=Label(win,text="soyadını gir:").place(x=30,y=50)
e2=Entry(win)
e2.place(x=100,y=50)

l3=Label(win,text="ürün adedi:").place(x=30,y=90)
e3=Entry(win)
e3.place(x=100,y=90)

l4=Label(win,text="ürün fiyatı:").place(x=30,y=130)
e4=Entry(win)
e4.place(x=100,y=130)

Button(win,text="hesapla",command=hesapla).place(x=100,y=150)

mainloop()