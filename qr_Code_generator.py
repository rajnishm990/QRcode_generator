from tkinter import *
import qrcode
import image


def generateR():
    qr = qrcode.QRCode(
        version = 15,
        box_size =10,
        border =5
    )
    data = userValue.get()
    qr.add_data(data)
    qr.make(fit =True)
    img = qr.make_image(fill="black" ,back_color ="white")
    img.save("Generated_Image.png")
    


app = Tk()
app.title("QR CODE GENERATOR")
app.geometry("550x720")
app.minsize(300,300)
app.maxsize(550,720)


bg = PhotoImage(file = "bground.png")


canvas1 = Canvas(app ,width = 550 , height=720)
canvas1.pack(fill ="both", expand=True)
canvas1.create_image(0,0 ,image =bg,anchor="nw")

canvas1.create_text(300,2,text ="QR CODE GENERATOR" , fill ="White", font=('Helvetica 20 bold '), anchor="n",justify =CENTER,)

l1 = Label(app,text ="ENTER THE TEXT OR LINK YOU WANT\n TO CONVERT TO QR CODE" , font=('Comicsans 15 italic'),bg = 'Black',fg ="white",justify=CENTER)
l1.place(relx=0.5,rely=0.4,anchor="n")
userValue = StringVar()
inputtxt = Entry(app,textvariable =userValue,bg ='white' , width =80,relief =SUNKEN)
inputtxt.place(relx=0.5,rely=0.5,anchor ='n')
submitButton = Button(app, text ="CONVERT", activebackground ='blue',font = ('Helvetica 10 bold'),command =generateR )
submitButton.place(relx = 0.5,rely=0.55,anchor ='n')


app.mainloop()
