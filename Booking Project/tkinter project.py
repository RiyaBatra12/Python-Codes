from tkinter import *
import mysql.connector
import tkinter.messagebox
from PIL import ImageTk,Image

mydb=mysql.connector.connect(host='localhost',user='root',passwd='Riyabhavya@7581',database='movieticket')
mycursor=mydb.cursor()
mycursor.execute('drop table details')
mycursor.execute('Create table details (name varchar(30) not null ,phone varchar(30) not null , email varchar(40) not null , movie varchar(30) , cinema varchar(60) , timing varchar(30))')


def enter_details():
    sqlcommand='Insert into details (name,phone,email,movie,cinema,timing) values (%s,%s,%s,%s,%s,%s)'
    values=(name.get(),phone.get(),email.get(),movieclick.get(),cinemaclick.get(),timingclick.get())
    mycursor.execute(sqlcommand,values)            
    mydb.commit()
              
                 
def menu():
    x=Tk()
    l1=Label(x,text='Hello '+name.get(),font=("Century",20))
    l1.place(x=0,y=0)
    l2=Label(x,text='How may I help you today?',font=("Century",20))
    l2.place(x=0,y=50)
    x.title('Menu')
    x.geometry("500x350")
    b1=Button(x,text='Book New Tickets',font=("Comic Sans ms",16),command=book_ticket)
    b2=Button(x,text='Edit Booking',font=("Comic Sans ms",16),command=edit_booking)
    b3=Button(x,text='Cancel booking',font=("Comic Sans ms",16),command=onclick)
    b4=Button(x,text='Exit',font=("Comic Sans ms",16),command=registration)
    b1.place(x=0,y=100)
    b2.place(x=0,y=150)
    b3.place(x=0,y=200)
    b4.place(x=0,y=250)
    
def onclick():
    res=tkinter.messagebox.askyesno('prompt','Do you want to proceed?')
    if res==True:
        delete_booking()

    else:
        pass

def delete_booking():
    y=phone.get()
    mycursor.execute('delete from details where phone = '  + phone.get())
    mydb.commit()


def book_ticket():
    y=Tk()
    y.geometry("550x450")
    l=Label(y,text="Now Showing",font=("Comic Sans ms",20,"bold"))
    l.place(x=160,y=0)
    l1=Label(y,text="Hindi Movies",font=("Comic Sans ms",20,"bold"))
    l1.place(x=0,y=50)
    b1=Button(y,text="Uunchai",font=("Century",13),fg='maroon',command=uunchai)
    b1.place(x=50,y=100)
    b2=Button(y,text="Ram Setu",font=("Century",13),fg='maroon',command=ramsetu)
    b2.place(x=150,y=100)
    b3=Button(y,text="Drishyam 2",font=("Century",13),fg='maroon',command=drishyam)
    b3.place(x=260,y=100)
    l2=Label(y,text="English Movies",font=("Comic Sans ms",20,"bold"))
    l2.place(x=0,y=150)
    b4=Button(y,text="Top Gun Maverick",font=("Century",13),fg='blue4',command=topgun)
    b4.place(x=50,y=200)
    b5=Button(y,text="Black Adam",font=("Century",13),fg='blue4',command=blackadam)
    b5.place(x=230,y=200)
    b6=Button(y,text="Wakanda Forever",font=("Century",13),fg='blue4',command=wakandaforever)
    b6.place(x=360,y=200)
    l3=Label(y,text="Other Movies",font=("Comic Sans ms",20,"bold"))
    l3.place(x=0,y=250)
    b7=Button(y,text="Sher Bagga",font=("Century",13),fg='dark green',command=sherbagga)
    b7.place(x=50,y=300)
    b8=Button(y,text="Kantara",font=("Century",13),fg='dark green',command=kantara)
    b8.place(x=180,y=300)
    b9=Button(y,text="Yashoda",font=("Century",13),fg='dark green',command=yashoda)
    b9.place(x=280,y=300)
    y.mainloop()

def booking():
    abc=Toplevel()
    abc.geometry('600x600')
    l1=Label(abc,text="Select Movie",font=("Century",20))
    global movieclick
    global cinemaclick
    global timingclick
    movieclick=StringVar()
    movieclick.set("Movie Name")
    cinemaclick=StringVar()
    cinemaclick.set("Cinema Name")
    timingclick=StringVar()
    timingclick.set("Movie Timings")
    movies=['','Uunchai','Ram Setu','Drishyam 2','Top Gun Maverick','Black Adam','Wakanda Forever','Sher Bagga','Kantara','Yashoda']
    movie=OptionMenu(abc,movieclick,*movies)
    l2=Label(abc,text="Select Cinema",font=('Century',20))
    cinemas=['',"Cinepolis: Cross River Mall,Shahdara","Cinepolis: DLF Avenue,Saket","Inox: Janak Place","Inox: R Cube,Monad Mall","Movietime: Pritampura","PVR: Select City Walk,Delhi","Wave: Raja Garden"]
    cinema=OptionMenu(abc,cinemaclick,*cinemas)
    l3=Label(abc,text="Select Timings",font=('Century',20))
    options=['','11:00AM','01:30PM','4:15PM','6:00PM','9:00PM','10:20PM']
    timing=OptionMenu(abc,timingclick,*options)
    l4=Label(abc,text='Booking',font=("Comic Sans ms",25,"bold"))
    l4.place(x=190,y=0)
    b1=Button(abc,text="Enter" ,font=("Comic Sans ms",18),command= lambda:[menu(),enter_details()])
    b1.place(x=200,y=300)
    l1.place(x=0,y=50)
    l2.place(x=0,y=150)
    l3.place(x=0,y=250)
    movie.place(x=300,y=50)
    cinema.place(x=300,y=150)
    timing.place(x=300,y=250)
    abc.mainloop()
def edit_booking():
    a=Toplevel()
    a.geometry('600x600')
    l1=Label(a,text="Select Movie",font=("Century",20))
    global movieclick_edit
    global cinemaclick_edit
    global timingclick_edit
    movieclick_edit=StringVar()
    movieclick_edit.set(movieclick.get())
    cinemaclick_edit=StringVar()
    cinemaclick_edit.set(cinemaclick.get())
    timingclick_edit=StringVar()
    timingclick_edit.set(timingclick.get())
    movies=['','Uunchai','Ram Setu','Drishyam 2','Top Gun Maverick','Black Adam','Wakanda Forever','Sher Bagga','Kantara','Yashoda']
    movie=OptionMenu(a,movieclick_edit,*movies)
    l2=Label(a,text="Select Cinema",font=('Century',20))
    cinemas=['',"Cinepolis: Cross River Mall,Shahdara","Cinepolis: DLF Avenue,Saket","Inox: Janak Place","Inox: R Cube,Monad Mall","Movietime: Pritampura","PVR: Select City Walk,Delhi","Wave: Raja Garden"]
    cinema=OptionMenu(a,cinemaclick_edit,*cinemas)
    l3=Label(a,text="Select Timings",font=('Century',20))
    options=['','11:00AM','01:30PM','4:15PM','6:00PM','9:00PM','10:20PM']
    timing=OptionMenu(a,timingclick_edit,*options)
    l4=Label(a,text='Booking',font=("Comic Sans ms",25,"bold"))
    l4.place(x=190,y=0)
    b1=Button(a,text="Save Changes" ,font=("Comic Sans ms",18),command= lambda:[menu(),new_details()])
    b1.place(x=200,y=300)
    l1.place(x=0,y=50)
    l2.place(x=0,y=150)
    l3.place(x=0,y=250)
    movie.place(x=300,y=50)
    cinema.place(x=300,y=150)
    timing.place(x=300,y=250)
    a.mainloop()
def new_details():
    mycursor.execute('Update details SET movie = %s , cinema = %s, timing = %s where phone = %s ',(movieclick_edit.get(),cinemaclick_edit.get(),timingclick_edit.get(),phone.get()))
    mydb.commit()    

def uunchai():
    z=Toplevel()
    z.geometry("750x600")
    image = Image.open("uunchai.png")
    img=image.resize((150,250))
    test = ImageTk.PhotoImage(img)
    bimg= Label(z,image=test)
    bimg.image=test
    bimg.place(x=500,y=250)
    l1=Label(z,text="Uunchai",font=("Century",20))
    l1.place(x=300,y=0)
    l2=Label(z,text="8.5/10 Rating",font=('Arial',17))
    l3=Label(z,text="About the movie",font=("Century",20))
    l4=Label(z,text='''Three friends take a trek to the Everest Base Camp which
                  becomes a personal, emotional and spiritual journey while battling their
         physical limitations and discovering the true meaning of freedom.''',font=('Arial',15))
    l5=Label(z,text="Cast",font=("Century",20))
    l6=Label(z,text='''                 Amitabh Bachchan
           Anupam Kher
         Boman Irani
                Parineeti Chopra
          Neena Gupta''',font=('Arial',15))
    b1=Button(z,text="Book Ticket",font=("Century",20),command=booking)
    b2=Button(z,text="Back",font=("Century",20),command=book_ticket)
    l2.place(x=0,y=50)
    l3.place(x=0,y=100)
    l4.place(x=0,y=150)
    l5.place(x=0,y=250)
    l6.place(x=0,y=290)
    b1.place(x=150,y=430)
    b2.place(x=350,y=430)
    z.mainloop()



def drishyam():
    z=Toplevel()
    z.geometry("790x600")
    image = Image.open("drishyam.jpg")
    img=image.resize((150,250))
    test = ImageTk.PhotoImage(img)
    bimg= Label(z,image=test)
    bimg.image=test
    bimg.place(x=500,y=250)
    l1=Label(z,text="Drishyam 2",font=("Century",20))
    l1.place(x=300,y=0)
    l2=Label(z,text="9/10 Rating",font=('Arial',17))
    l3=Label(z,text="About the movie",font=("Century",20))
    l4=Label(z,text='''                  7 years after the case related to Vijay Salgaonkar and his family was closed,
    a series of unexpected events bring a truth to light that threatens to
              change everything for the Salgaonkars.Can Vijay save his family this time?''',font=('Arial',15))
    l5=Label(z,text="Cast",font=("Century",20))
    l6=Label(z,text='''         Ajay Devgn
Tabu
                 Akshaye Khanna''',font=('Arial',15))
    b1=Button(z,text="Book Ticket",font=("Century",20),command=booking)
    b2=Button(z,text="Back",font=("Century",20),command=book_ticket)
    l2.place(x=0,y=50)
    l3.place(x=0,y=100)
    l4.place(x=0,y=150)
    l5.place(x=0,y=270)
    l6.place(x=0,y=320)
    b1.place(x=150,y=430)
    b2.place(x=350,y=430)
    z.mainloop()




def ramsetu():
    z=Toplevel()
    z.geometry("760x600")
    image = Image.open("ram.jpg")
    img=image.resize((150,250))
    test = ImageTk.PhotoImage(img)
    bimg= Label(z,image=test)
    bimg.image=test
    bimg.place(x=500,y=250)
    l1=Label(z,text="Ram Setu",font=("Century",20))
    l1.place(x=300,y=0)
    l2=Label(z,text="8.1/10 Rating",font=('Arial',17))
    l3=Label(z,text="About the movie",font=("Century",20))
    l4=Label(z,text='''An atheist archaeologist turned believer must race against time to prove
     the true existence of the legendary Ram Setu before evil forces destroy the
    pillar of India`s heritage.An action adventure with a strong serving of twists
      and turns, Ram Setu promises to keep the viewer engaged and entertained,
          making it the perfect festive film to be enjoyed with the entire family in cinemas.''',font=('Arial',15))
    l5=Label(z,text="Cast",font=("Century",20))
    l6=Label(z,text='''  Akshay Kumar
           Jacqueline fernandez
          Nushrratt Bharuccha''',font=('Arial',15))
    b1=Button(z,text="Book Ticket",font=("Century",20),command=booking)
    b2=Button(z,text="Back",font=("Century",20),command=book_ticket)
    l2.place(x=0,y=50)
    l3.place(x=0,y=100)
    l4.place(x=0,y=150)
    l5.place(x=0,y=270)
    l6.place(x=0,y=320)
    b1.place(x=150,y=430)
    b2.place(x=350,y=430)
    z.mainloop()






def topgun():
    z=Toplevel()
    z.geometry("760x600")
    image = Image.open("topgun.jpg")
    img=image.resize((150,250))
    test = ImageTk.PhotoImage(img)
    bimg= Label(z,image=test)
    bimg.image=test
    bimg.place(x=500,y=250)
    l1=Label(z,text="Top Gun Maverick",font=("Century",20))
    l1.place(x=250,y=0)
    l2=Label(z,text="8.4/10 Rating",font=('Arial',17))
    l3=Label(z,text="About the movie",font=("Century",20))
    l4=Label(z,text='''30 years after the events of `Top Gun` (1986), the sequel hinges on
        Captain Pete Mitchell`s (Tom Cruise) attempts to come to terms with his
        past, while training his friend`s son (Miles Teller) for a dangerous mission.''',font=('Arial',15))
    l5=Label(z,text="Cast",font=("Century",20))
    l6=Label(z,text='''  Tom Cruise
Val Kilmer
 Miles Teller
        Jennifer Connelly''',font=('Arial',15))
    b1=Button(z,text="Book Ticket",font=("Century",20),command=booking)
    b2=Button(z,text="Back",font=("Century",20),command=book_ticket)
    l2.place(x=0,y=50)
    l3.place(x=0,y=100)
    l4.place(x=0,y=150)
    l5.place(x=0,y=270)
    l6.place(x=0,y=320)
    b1.place(x=150,y=430)
    b2.place(x=350,y=430)
    z.mainloop()



def blackadam():
    z=Toplevel()
    z.geometry("860x600")
    image = Image.open("blackadam.jpg")
    img=image.resize((150,250))
    test = ImageTk.PhotoImage(img)
    bimg= Label(z,image=test)
    bimg.image=test
    bimg.place(x=500,y=250)
    l1=Label(z,text="Black Adam",font=("Century",20))
    l1.place(x=300,y=0)
    l2=Label(z,text="8.7/10 Rating",font=('Arial',17))
    l3=Label(z,text="About the movie",font=("Century",20))
    l4=Label(z,text='''Nearly 5,000 years after he was bestowed with the almighty powers of the
ancient gods-and imprisoned just as quickly-Black Adam (Johnson) is freed
                from his earthly tomb, ready to unleash his unique form of justice on the modern world.''',font=('Arial',15))
    l5=Label(z,text="Cast",font=("Century",20))
    l6=Label(z,text='''                Dawyne Johnson
       Viola Davis
        Sarah Shahi
              Pierce Brosnan''',font=('Arial',15))
    b1=Button(z,text="Book Ticket",font=("Century",20),command=booking)
    b2=Button(z,text="Back",font=("Century",20),command=book_ticket)
    l2.place(x=0,y=50)
    l3.place(x=0,y=100)
    l4.place(x=0,y=150)
    l5.place(x=0,y=270)
    l6.place(x=0,y=320)
    b1.place(x=150,y=430)
    b2.place(x=350,y=430)
    z.mainloop()




def wakandaforever():
    z=Toplevel()
    z.geometry("860x600")
    image = Image.open("wakanda.jpg")
    img=image.resize((150,250))
    test = ImageTk.PhotoImage(img)
    bimg= Label(z,image=test)
    bimg.image=test
    bimg.place(x=500,y=250)
    l1=Label(z,text="Wakanda Forever",font=("Century",20))
    l1.place(x=300,y=0)
    l2=Label(z,text="8.7/10 Rating",font=('Arial',17))
    l3=Label(z,text="About the movie",font=("Century",20))
    l4=Label(z,text='''In the wake of King T`Challa`s death, Queen Ramonda, Shuri, M`Baku, Okoye and
the Dora Milaje fight to protect their nation from intervening world powers with the
         help of War Dog Nakia and Everett Ross to forge a new path for the kingdom of Wakanda.''',font=('Arial',15))
    l5=Label(z,text="Cast",font=("Century",20))
    l6=Label(z,text='''                Angela Bassett
                 Martin Freeman
             Danai Gurira
              Winston Duke''',font=('Arial',15))
    b1=Button(z,text="Book Ticket",font=("Century",20),command=booking)
    b2=Button(z,text="Back",font=("Century",20),command=book_ticket)
    l2.place(x=0,y=50)
    l3.place(x=0,y=100)
    l4.place(x=0,y=150)
    l5.place(x=0,y=270)
    l6.place(x=0,y=320)
    b1.place(x=150,y=430)
    b2.place(x=350,y=430)
    z.mainloop()



def sherbagga():
    z=Toplevel()
    z.geometry("790x600")
    image = Image.open("sher.jpg")
    img=image.resize((150,250))
    test = ImageTk.PhotoImage(img)
    bimg= Label(z,image=test)
    bimg.image=test
    bimg.place(x=500,y=250)
    l1=Label(z,text="Sher Bagga",font=("Century",20))
    l1.place(x=300,y=0)
    l2=Label(z,text="8.1/10 Rating",font=('Arial',17))
    l3=Label(z,text="About the movie",font=("Century",20))
    l4=Label(z,text='''When Shera starts to embark on a journey to get love of his life, he encounters Gulab
 on the way. She manipulates her way to get her things done through Shera. Gulab falls
  for Shera but he is there to meet his girlfriend. What will happen when they meet again?''',font=('Arial',15))
    l5=Label(z,text="Cast",font=("Century",20))
    l6=Label(z,text='''        Ammy Virk
           Sonam Bajwa
          Nirmal Rishi''',font=('Arial',15))
    b1=Button(z,text="Book Ticket",font=("Century",20),command=booking)
    b2=Button(z,text="Back",font=("Century",20),command=book_ticket)
    l2.place(x=0,y=50)
    l3.place(x=0,y=100)
    l4.place(x=0,y=150)
    l5.place(x=0,y=270)
    l6.place(x=0,y=320)
    b1.place(x=150,y=430)
    b2.place(x=350,y=430)
    z.mainloop()





def kantara():
    z=Toplevel()
    z.geometry("850x650")
    image = Image.open("kantara.jpg")
    img=image.resize((150,250))
    test = ImageTk.PhotoImage(img)
    bimg= Label(z,image=test)
    bimg.image=test
    bimg.place(x=500,y=350)
    l1=Label(z,text="Kantara",font=("Century",20))
    l1.place(x=300,y=0)
    l2=Label(z,text="8.1/10 Rating",font=('Arial',17))
    l3=Label(z,text="About the movie",font=("Century",20))
    l4=Label(z,text='''Set in a fictional village of Dakshina Kannada, Kantara is a visual grandeur that brings alive the
traditional culture of Kambla and Bhootha Kola. It is believed that Demigods are the guardians
and their energies encircle the village. In the story, there is a ripple when a battle of ego
swirls along tradition and culture of the land. The soul of the story is on human and nature
conflict in which Shiva is the rebellion and works against nature. There are intense conflicts
he indulges in. In the end, a much awaiting loop leads to war between the villagers and the evil
forces. Will Shiva, the protagonist of the film be able to reinstate peace and harmony in the
village perceiving his existence?''',font=('Arial',15))
    l5=Label(z,text="Cast",font=("Century",20))
    l6=Label(z,text='''        Rishab Shetty
           Sapthami Gowda
          Pramod Shetty''',font=('Arial',15))
    b1=Button(z,text="Book Ticket",font=("Century",20),command=booking)
    b2=Button(z,text="Back",font=("Century",20),command=book_ticket)
    l2.place(x=0,y=50)
    l3.place(x=0,y=100)
    l4.place(x=0,y=150)
    l5.place(x=0,y=320)
    l6.place(x=0,y=370)
    b1.place(x=150,y=470)
    b2.place(x=350,y=470)
    z.mainloop()



def yashoda():
    z=Toplevel()
    z.geometry('880x600')
    image = Image.open("yashoda.jpg")
    img=image.resize((150,250))
    test = ImageTk.PhotoImage(img)
    bimg= Label(z,image=test)
    bimg.image=test
    bimg.place(x=500,y=250)
    l1=Label(z,text="Sher Bagga",font=("Century",20))
    l1.place(x=300,y=0)
    l2=Label(z,text="8.5/10 Rating",font=('Arial',17))
    l3=Label(z,text="About the movie",font=("Century",20))
    l4=Label(z,text='''           An innocent woman `Yashoda` accepts to be a surrogate mother due to her circumstances.
           She then finds herself trapped in a world of unknown. Amidst a myriad of politicians, doctors,
and powerful people, how does she battle her way out? Watch Yashoda to find out.''',font=('Arial',15))
    l5=Label(z,text="Cast",font=("Century",20))
    l6=Label(z,text='''        Samantha Ruth Prabhu
           Varalaxmi Sarathkumar
          Unni Mukundan''',font=('Arial',15))
    b1=Button(z,text="Book Ticket",font=("Century",20),command=booking)
    b2=Button(z,text="Back",font=("Century",20),command=book_ticket)
    l2.place(x=0,y=50)
    l3.place(x=0,y=100)
    l4.place(x=0,y=150)
    l5.place(x=0,y=270)
    l6.place(x=0,y=320)
    b1.place(x=150,y=430)
    b2.place(x=350,y=430)
    z.mainloop()



def registration():
    global t
    t=Tk()
    l1=Label(t,text='Registration',font=("Comic Sans ms",25,"bold"))
    l1.place(x=190,y=0)
    l2=Label(t,text="Enter Your Name",font=("Arial",20))
    l2.place(x=0,y=50)
    global name
    name=Entry(t,width=20,font=("Century",16))
    name.place(x=250,y=55)
    l3=Label(t,text="Enter your Phone number",font=("Arial",16))
    l3.place(x=0,y=100)
    global phone
    phone=Entry(t,width=20,font=("Century",16))
    phone.place(x=250,y=100)
    l4=Label(t,text="Enter Your Email",font=("Arial",20))
    l4.place(x=0,y=150)
    global email
    email=Entry(t,width=20,font=("Century",16))
    email.place(x=250,y=150)
    t.title('Register')
    t.geometry("600x500")
    b2=Button(t,text='Menu',font=("Comic Sans ms",16),command=menu)
    b2.place(x=180,y=200)
    b3=Button(t,text='Exit',font=("Comic Sans ms",16),command=exit)
    b3.place(x=280,y=200)
registration()

t.mainloop()
