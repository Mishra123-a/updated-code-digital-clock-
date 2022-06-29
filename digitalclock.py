from tkinter import *
import datetime
def date_time():

    time= datetime.datetime.now()
    hr = time.strftime('%I')
    min = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')

    date= time.strftime("%d")
    month= time.strftime("%m")
    year = time.strftime("%y")
    day= time.strftime("%a")

    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_am.config(text=am)

    lab_date.config(text=date)
    lab_mo.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)

    lab_hr.after(100,date_time)
#Add Image
window =Tk()
window.title('*********  Digital Clock  *********')
window.geometry("1200x720")

global our_images,count
count = -1

our_images =[

    PhotoImage(file = 'C:\\Users\\Lenovo\\Downloads\\Best-Beautiful-Images-For-Desktop-Nature.png'),
    PhotoImage(file = 'C:\\Users\\Lenovo\\Downloads\\A1cy5nrXujL.png'),
    PhotoImage(file = 'C:\\Users\\Lenovo\\Downloads\\pic\\nature-fcp.png')
]

#Create canvas

window = Canvas(window, width = 1200, height= 720)
window.pack(fill='both', expand = True)

#Set the canvas image

window.create_image(0,0, image=our_images[0], anchor='nw')

def next():
    global count
    if count == 2:
        window.create_image(0, 0, image=our_images[0], anchor='nw')
        count = 0
    else:
        window.create_image(0, 0, image=our_images[count+1], anchor='nw')
        count += 1

        window.after(2000, next)

#Time

lab_hr=Label(window,text="00",font=('Time New Roman',60,"bold"),bg= 'red',fg = "white")
lab_hr.place(x=200,y=45,height=100,width=100)
lab_hr_txt=Label(window,text="Hour",font=('Time New Roman',20,"bold"),bg= 'red',fg = "white")
lab_hr_txt.place(x=200,y=190,height=40,width=100)

lab_min=Label(window,text="00",font=('Time New Roman',60,"bold"),bg= 'red',fg = "white")
lab_min.place(x=400,y=50,height=100,width=100)
lab_min_txt=Label(window,text="Min.",font=('Time New Roman',20,"bold"),bg= 'red',fg = "white")
lab_min_txt.place(x=400,y=190,height=40,width=100)

lab_sec=Label(window,text="00",font=('Time New Roman',50,"bold"),bg= 'red',fg = "white")
lab_sec.place(x=600,y=50,height=100,width=100)
lab_sec_txt=Label(window,text="sec",font=('Time New Roman',20,"bold"),bg= 'red',fg = "white")
lab_sec_txt.place(x=600,y=190,height=40,width=100)

lab_am=Label(window,text="00",font=('Time New Roman',50,"bold"),bg= 'red',fg = "white")
lab_am.place(x=820,y=50,height=100,width=100)
lab_am_txt=Label(window,text="AM/PM",font=('Time New Roman',20,"bold"),bg= 'red',fg = "white")
lab_am_txt.place(x=820,y=190,height=40,width=100)

#Date

lab_date=Label(window,text="00",font=('Time New Roman',60,"bold"),bg= 'red',fg = "white")
lab_date.place(x=200,y=270,height=100,width=100)
lab_date_txt=Label(window,text="Date",font=('Time New Roman',20,"bold"),bg= 'red',fg = "white")
lab_date_txt.place(x=200,y=410,height=40,width=100)

lab_mo=Label(window,text="00",font=('Time New Roman',60,"bold"),bg= 'red',fg = "white")
lab_mo.place(x=400,y=270,height=100,width=100)
lab_mo_txt=Label(window,text="Month.",font=('Time New Roman',20,"bold"),bg= 'red',fg = "white")
lab_mo_txt.place(x=400,y=410,height=40,width=100)

lab_year=Label(window,text="00",font=('Time New Roman',50,"bold"),bg= 'red',fg = "white")
lab_year.place(x=600,y=270,height=100,width=100)
lab_year_txt=Label(window,text="Year",font=('Time New Roman',20,"bold"),bg= 'red',fg = "white")
lab_year_txt.place(x=600,y=410,height=40,width=100)


lab_day=Label(window,text="00",font=('Time New Roman',35,"bold"),bg= 'red',fg = "white")
lab_day.place(x=820,y=270,height=100,width=100)
lab_day_txt=Label(window,text="Day",font=('Time New Roman',20,"bold"),bg= 'red',fg = "white")
lab_day_txt.place(x=820,y=410,height=40,width=100)


date_time()
next()
window.mainloop()