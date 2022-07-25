# cd Desktop\programming\python\project
from tkinter import *
from tkinter import messagebox as ms
from tkinter import ttk
import time
import turtle
# import mysql.connector

class Billing:
    def __init__(self, root):
        self.root = root
        self.root.title("Restorent Management System")

        #-------------------------Declair Variable For Calculator----------------------
        self.text_input=StringVar()
        self.operator=""
        #-------------------------Declair Variable For UserDetials---------------------
        self.table_no = StringVar()
        self.user_name = StringVar()
        self.mobile_no = StringVar()
        #-------------------------Declair Variable For Date And Time-------------------
        self.Date1 = StringVar()
        self.Time1 = StringVar()
        self.Date1.set(time.strftime("%d/%m/%Y"))
        self.Time1.set(time.strftime("%H:%M:%S"))

        #-------------------------Declair Variable For Receipt-------------------------
        self.select1 = []
        self.members1 =[]
        self.txt1 = StringVar()
        #-------------------------Create Frams For Visualization-----------------------
        self.FLF = Frame(self.root, width=750, height=600, bg="palegreen")
        self.FLF.grid()

        # ----------------------------Frame Top Left ----------------------------------
        self.FTL = Frame(self.FLF, width=300, height=300, bg="palegreen")
        self.FTL.grid(row=0,column=0,sticky=W)

        # ----------------------------Frame Horizantal Middle Left---------------------
        self.FHML = Frame(self.FLF, width=225, height=300, bg="palegreen")
        self.FHML.grid(row=0,column=1,sticky=W) 

        #-----------------Display the Textbox and Scrollbar----------------------------
        # create the Textbox with scrollbar widgets
        self.txt=Text(self.FHML, height=17, width=25, wrap="word")
        self.scrl=Scrollbar(self.FHML, orient="vertical")

        #scrollbar and textbox connect with each other
        self.txt.configure(yscrollcommand=self.scrl.set)
        self.scrl.configure(command=self.txt.yview)

        # Frame Top Right
        self.FTR = Frame(self.FLF, width=225, height=300, bg="palegreen")#blue
        self.FTR.grid(row=0,column=2,sticky=W)       
        #-----------------Display the Order Item-----------------------------------
        # Frame Horizantal Middle Left
        self.FML = Frame(self.FLF, width=225, height=200, bg="palegreen")#it is red
        self.FML.grid(row=2,column=1,sticky=W)
         # Frame Bottom Left
        self.FBL = Frame(self.FLF, width=225, height=200, bg="palegreen")
        self.FBL.grid(row=2,column=2,sticky=W)       
        #-----------------User Details Frame and Label-----------------------------
        # Frame Buttom Right
        self.FBR = Frame(self.FLF, width=300, height=200, bg="palegreen")
        self.FBR.grid(row=2,column=0,sticky=W)
        #create label frame
        self.frame=LabelFrame(self.FBL, text="User Details", bg="palegreen")
        self.frame.grid(row=0,column=0)
        #create label in labelframe
        Label(self.frame,text="Table No.", bg="palegreen").grid(row=1,column=0)
        Entry(self.frame, textvariable=self.table_no).grid(row=1,column=1)
        Label(self.frame, text="UserName", bg="palegreen").grid(row=2,column=0)
        Entry(self.frame, textvariable=self.user_name).grid(row=2,column=1)
        Label(self.frame, text="MobileNo.", bg="palegreen").grid(row=3,column=0)
        Entry(self.frame, textvariable=self.mobile_no).grid(row=3,column=1)
        
        #-----------------Label For The Date And Time-----------------------------
        self.lblDate = Label(self.FBR, textvariable=self.Date1, font=('arial', 15, 'bold'), bg="palegreen").grid(row=0,column=0)
        
        #-----------------Function of Display the Order Item-----------------------
        def Displayitem():
                if(self.var.get() == 'Water'):
                    
                    #create List for insert data into Listbox
                    self.listOfItem = ['General Water---','Mineral Water---','Lemon Water-----']        
                    self.priceOfItem = [10,25,50]
                    self.members = StringVar()
                    
                    #create listbox with scrollbar
                    self.mylist=Listbox(self.FML, height=7, width=27, selectmode=SINGLE)
                    self.scroll=Scrollbar(self.FML, orient="vertical")
                    
                    #scrollbar and listbox Connect with each other
                    self.mylist.configure(yscrollcommand=self.scroll.set)
                    self.scroll.configure(command=self.mylist.yview)
                    #insert Data in Listbox                      
                    self.mylist.insert(END, "Name of Item and Price\n")
                    i = 0
                    while i < len(self.listOfItem):
                        self.mylist.insert("end", self.listOfItem[i]+"   "+str(self.priceOfItem[i]))
                        i = i+1
                            
                    #give the possition of listbox and scroll on widgets
                    self.mylist.grid(row=0,column=0, sticky="nsew")
                    self.scroll.grid(row=0, column=1, sticky="ns")

                    # #insert the data in textbox
                    self.txt.insert(END, "Items\t\t    P\tM \n")

                    def selectdisply():
                        # get the item from listbox
                        self.index = self.mylist.curselection()
                        self.member = self.members.get()
                                                                  
                        # fot the Retrive item from listbox using Loop 
                        self.seltext = self.mylist.get(self.index)
                        self.txt.insert(END,self.seltext+"  "+self.member+"\n")
                                       
                    #label
                    Label(self.FML, text="No of Members", bg="palegreen").grid(row=2,column=0,sticky=W)
                    #Entry
                    Entry(self.FML, textvariable=self.members).grid(row=3,column=0,sticky=W)

                    self.slct =Button(self.FML, text="Submit", command=selectdisply, bg="greenyellow")
                    self.slct.grid(row=4,column=0)

                elif(self.var.get() == 'Drink'):
                    #create List for insert data into Listbox
                    self.listOfItem = ['Milk------------','Normal-Coffee---','Cappaccino------','African-Coffee--','American-Coffee-','Normal-Tea------','Black-Tea-------','Green-Tea-------','Coca-Cola-------','Sprite----------','Thaumsup--------','Mirinda---------','Limka-----------']        
                    self.priceOfItem = [20,25,50,60,60,10,15,15,25,25,25,25,25]
                    self.members = StringVar()
                    
                    #create listbox with scrollbar
                    self.mylist=Listbox(self.FML, height=7, width=27, selectmode=SINGLE)
                    self.scroll=Scrollbar(self.FML, orient="vertical")
                    
                    #scrollbar and listbox Connect with each other
                    self.mylist.configure(yscrollcommand=self.scroll.set)
                    self.scroll.configure(command=self.mylist.yview)
                    #insert Data in Listbox                      
                    self.mylist.insert(END, "Name of Item and Price\n")
                    i = 0
                    while i < len(self.listOfItem):
                        self.mylist.insert("end", self.listOfItem[i]+"   "+str(self.priceOfItem[i]))
                        i = i+1
                            
                    #give the possition of listbox and scroll on widgets
                    self.mylist.grid(row=0,column=0, sticky="nsew")
                    self.scroll.grid(row=0, column=1, sticky="ns")

                    # #insert the data in textbox
                    self.txt.insert(END, "Items\t\t    P\tM \n")

                    def selectdisply():
                        # get the item from listbox
                        self.index = self.mylist.curselection()
                        self.member = self.members.get()
                                                                  
                        # fot the Retrive item from listbox using Loop 
                        self.seltext = self.mylist.get(self.index)
                        self.txt.insert(END,self.seltext+"  "+self.member+"\n")
                    
                    #label
                    Label(self.FML, text="No of Members", bg="palegreen").grid(row=2,column=0,sticky=W)
                    #Entry
                    Entry(self.FML, textvariable=self.members).grid(row=3,column=0,sticky=W)

                    self.slct = Button(self.FML, text="Submit", command=selectdisply, bg="greenyellow")
                    self.slct.grid(row=4,column=0)

                elif(self.var.get() == 'Food'):
                    #create List for insert data into Listbox
                    self.listOfItem = ['Pizza-----------','Vage-Sendvich---','Nonvage-Sendvich','Burger----------','Wada-Pav--------','Pav-Bhaji-------','Pani-Puri-------','Save-Puri-------','Bhel------------','Dabelee---------','Vage-Pulav------','Nonvage-Pulav---','Nuddles---------','Chinies---------','Momoes----------','Manchurian------']        
                    self.priceOfItem = [70,50,70,60,10,50,10,10,10,10,50,70,25,20,10,70]
                    self.members = StringVar()
                    
                    #create listbox with scrollbar
                    self.mylist=Listbox(self.FML, height=7, width=27, selectmode=SINGLE)
                    self.scroll=Scrollbar(self.FML, orient="vertical")
                    
                    #scrollbar and listbox Connect with each other
                    self.mylist.configure(yscrollcommand=self.scroll.set)
                    self.scroll.configure(command=self.mylist.yview)
                    #insert Data in Listbox                      
                    self.mylist.insert(END, "Name of Item and Price\n")
                    i = 0
                    while i < len(self.listOfItem):
                        self.mylist.insert("end", self.listOfItem[i]+"   "+str(self.priceOfItem[i]))
                        i = i+1
                            
                    #give the possition of listbox and scroll on widgets
                    self.mylist.grid(row=0,column=0, sticky="nsew")
                    self.scroll.grid(row=0, column=1, sticky="ns")

                    # #insert the data in textbox
                    self.txt.insert(END, "Items\t\t    P\tM \n")

                    def selectdisply():
                        # get the item from listbox
                        self.index = self.mylist.curselection()
                        self.member = self.members.get()
                                                                  
                        # fot the Retrive item from listbox using Loop 
                        self.seltext = self.mylist.get(self.index)
                        self.txt.insert(END,self.seltext+"  "+self.member+"\n")
                    
                    #label
                    Label(self.FML, text="No of Members", bg="palegreen").grid(row=2,column=0,sticky=W)
                    #Entry
                    Entry(self.FML, textvariable=self.members).grid(row=3,column=0,sticky=W)

                    self.slct = Button(self.FML, text="Submit", command=selectdisply, bg="greenyellow")
                    self.slct.grid(row=4,column=0)

                elif(self.var.get() == 'Juice'):
                    #create List for insert data into Listbox
                    self.listOfItem = ['Apple-Juice-----','Mango-Juice-----','Orange-Juice----','Pappya-Juice----','Banana-Sheike---','Anar-Juice------','Kivi-Juice------','Silce-----------','Mazza-----------']        
                    self.priceOfItem = [20,25,50,60,60,10,15,15,25,25,25,25,25]
                    self.members = StringVar()
                    
                    #create listbox with scrollbar
                    self.mylist=Listbox(self.FML, height=7, width=27, selectmode=SINGLE)
                    self.scroll=Scrollbar(self.FML, orient="vertical")
                    
                    #scrollbar and listbox Connect with each other
                    self.mylist.configure(yscrollcommand=self.scroll.set)
                    self.scroll.configure(command=self.mylist.yview)
                    #insert Data in Listbox                      
                    self.mylist.insert(END, "Name of Item and Price\n")
                    i = 0
                    while i < len(self.listOfItem):
                        self.mylist.insert("end", self.listOfItem[i]+"   "+str(self.priceOfItem[i]))
                        i = i+1
                            
                    #give the possition of listbox and scroll on widgets
                    self.mylist.grid(row=0,column=0, sticky="nsew")
                    self.scroll.grid(row=0, column=1, sticky="ns")

                    # #insert the data in textbox
                    self.txt.insert(END, "Items\t\t    P\tM \n")

                    def selectdisply():
                        # get the item from listbox
                        self.index = self.mylist.curselection()
                        self.member = self.members.get()
                                                                  
                        # fot the Retrive item from listbox using Loop 
                        self.seltext = self.mylist.get(self.index)
                        self.txt.insert(END,self.seltext+"  "+self.member+"\n")
                    
                    #label
                    Label(self.FML, text="No of Members", bg="palegreen").grid(row=2,column=0,sticky=W)
                    #Entry
                    Entry(self.FML, textvariable=self.members).grid(row=3,column=0,sticky=W)

                    self.slct = Button(self.FML, text="Submit", command=selectdisply, bg="greenyellow")
                    self.slct.grid(row=4,column=0)

        #give the possition of listbox and scroll on widgets
        self.txt.grid(row=0, column=0, sticky="nsew")
        self.scrl.grid(row=0,column=1, sticky="ns")

        #-------------------Function For Display The Receipt for Checking---------------------
        def receipt():
            #---------------Get the Value from insert Variable and Print to the Reciept-------
            self.tab_no = self.table_no.get()
            self.visitdate = self.Date1.get()
            self.usr_name = self.user_name.get()
            self.mob_no = self.mobile_no.get()
            self.rec = self.txt.get("1.0","end-1c")
            #---------------Total Amount Calculation widget-----------------------------------
            # this is find the integer number from the given string
            self.num = [int(s) for s in re.findall(r'\b\d+\b', self.rec)]
            # this loop multiply and add the amount
            i=0
            self.sum = 0
            while i< len(self.num):
                result = self.num[i] * self.num[i+1] # this means multiply possion [i] to possion [i + 1]
                self.sum = self.sum + result  # this means add the multiply possion [i] to possion [i + 1]
                i = i + 2   # it is increse the index number of list which is self.num
            
            self.Tax = self.sum * 18 /100
            self.Total = self.sum + self.Tax

            #-----------------Textbox For the Receipt-----------------------------------
            self.txt1=Text(self.FTL, height=17, width=35, wrap="word")
            self.scrl=Scrollbar(self.FTL, orient="vertical")
            #scrollbar and textbox connect with each other
            self.txt1.configure(yscrollcommand=self.scrl.set)
            self.scrl.configure(command=self.txt.yview)
            self.txt1.insert(END,"Table No." + self.tab_no+"    "+ "DATE: " + self.visitdate+"\n")
            self.txt1.insert(END,"Name: " + self.usr_name+"\n")
            self.txt1.insert(END,"Mobile No." + self.mob_no+"\n")
            self.txt1.insert(END,"==================================\n")
            self.txt1.insert(END, self.rec)
            self.txt1.insert(END,"==================================\n")
            self.txt1.insert(END, "Sub Total Amount\t\t\t"+ str(self.sum) + "\n")
            self.txt1.insert(END, "Tax Amount\t\t\t"+ str(self.Tax) + "\n")
            self.txt1.insert(END,"==================================\n")
            self.txt1.insert(END, "Payable Amount\t\t\t"+ str(self.Total))
            self.txt1.configure(state=DISABLED)
            self.txt1.grid(row=0, column=0, sticky="nsew")
            self.scrl.grid(row=0,column=1, sticky="ns") 
            self.tab_no = self.table_no.set("")
            self.usr_name = self.user_name.set("")
            self.mob_no = self.mobile_no.set("")
            self.txt.configure(state=DISABLED)
            

        #--------------------------------Print The Customer Bill------------------------------           
        def print1():
            #---------------------------Change the Disable State of Textbox for Clear---------
            self.txt1.configure(state=NORMAL)
            self.txt.configure(state=NORMAL)
            #---------------------------Textbox Clear-----------------------------------------
            self.txt.delete("1.0","end")
            self.txt1.delete("1.0","end")
            
        #--------------------------------Order Item List--------------------------------------       
        """def inst():
            # connect from database and table
            mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="password",
                database="testdb",
            )
            # create for the execute the query
            my_cursor = mydb.cursor()
            # insert the data into table
            query = "INSERT INTO costomer(name,MobileNo) VALUES(%s,%s)"
            # get the value of variables
            param = (self.user_name.get(),self.mobile_no.get())
            # execute the query and send two argument:
            #  first one is query and 
            #  second one is the value of given by usern from Entry box
            #  and this value cought by textvariable keyword and 
            #  its value get by the getmethod and send as parameter
            my_cursor.execute(query,param)
            mydb.commit()"""

        #-----------------------Function for Calculator-----------------------------------------
        def btnclick(numbers):
            global operator
            self.operator=self.operator + str(numbers)
            self.text_input.set(self.operator)
        
        def btnClearDisplay():
            global operator
            self.operator=""
            self.text_input.set("")

        def btnEqualsInput():
            global operator
            sumup=str(eval(self.operator))
            self.text_input.set(sumup)
            # self.operator=""

        #----------------------------Create Window For Watch----------------------------
        def watch():
            wn=turtle.Screen()
            wn.bgcolor("white")
            wn.setup(width=600,height=600)
            wn.title("Simple Analog Clock") 
            wn.tracer(0)

            #Create our drawing pen
            pen=turtle.Turtle()
            pen.hideturtle()
            pen.speed(0)
            pen.pensize(3)

            def draw_clock(h, m, s, pen):
                #Draw clock face
                pen.up() 
                pen.goto(0,210)
                pen.setheading(180)
                pen.color("black")
                pen.pendown()
                pen.circle(210)

                #Draw the lines for the hours
                pen.penup()
                pen.goto(0,0)
                pen.setheading(90)
                
                for _ in range(12):
                    pen.fd(190)
                    pen.pendown()
                    pen.fd(20)
                    pen.penup()
                    pen.goto(0,0)
                    pen.rt(30)
                
                #Draw the hour hand
                pen.penup()
                pen.goto(0,0)
                pen.color("blue")
                pen.setheading(90)
                angle=(h/12) * 360
                pen.rt(angle)
                pen.pendown()
                pen.fd(100)

                #Draw the minute hand
                pen.penup()
                pen.goto(0,0)
                pen.color("blue")
                pen.setheading(90)
                angle=(m/60) * 360
                pen.rt(angle)
                pen.pendown()
                pen.fd(180)

                #Draw the second hand
                pen.penup()
                pen.goto(0,0)
                pen.color("Red")
                pen.setheading(90)
                angle=(s/60) * 360
                pen.rt(angle)
                pen.pendown()
                pen.fd(100) 


            while True:
                # this matching time from system(our computer) time
                h = int(time.strftime("%I"))
                m = int(time.strftime("%M"))
                s = int(time.strftime("%S"))

                draw_clock(h,m,s,pen)
                wn.update()
                time.sleep(1)
                pen.clear()
            wn.mainloop() 

        #--------------------------------Combo Box For Select The Order Item------------------------       
         #create combo box
        self.var=StringVar(value="Item Order")
        combo = ttk.Combobox(self.FBR,width=40,textvariable=self.var, state="readonly")
        combo['values'] = (
            'Water',
            'Drink',
            'Food',
            'Juice',
        )
        combo.grid(row=1,column=0)
        #-----------------------Label For Name Of Calculator--------------------------------------
        lblcalculator = Label(self.FTR, text="CALCULATOR",font=("arial",15,"bold"), bg="palegreen").grid(row=0,column=0,columnspan=4)
        #-----------------------Calculator--------------------------------------------------------
        txtDisplay = Entry(self.FTR, width=17,state="readonly", bd=15, bg="gray",textvariable=self.text_input,font=("arial", 15,"bold")).grid(row=1,column=0,columnspan=4)
        #-----------------------Button in First Row-----------------------------------------------
        btndiv = Button(self.FTR, height=2,width=5, text="C", bd=5, command=btnClearDisplay,bg="Red").grid(row=2,column=0)
        btnmul = Button(self.FTR, height=2,width=5, text="/", bd=5, command=lambda: btnclick("/"),bg="greenyellow").grid(row=2,column=1)
        btnsub = Button(self.FTR, height=2,width=5, text="*", bd=5, command=lambda: btnclick("*"),bg="greenyellow").grid(row=2,column=2)
        btnpls = Button(self.FTR, height=2,width=5, text="-", bd=5, command=lambda: btnclick("-"),bg="greenyellow").grid(row=2,column=3)
        #-----------------------Button in Second Row----------------------------------------------
        btnqul = Button(self.FTR, height=2,width=5, text="+", bd=5, command=lambda: btnclick("+"),bg="greenyellow").grid(row=3,column=3)
        btn7 = Button(self.FTR, height=2,width=5, text="7", bd=5, command=lambda: btnclick(7), bg="palegreen").grid(row=3,column=0)
        btn8 = Button(self.FTR, height=2,width=5, text="8", bd=5, command=lambda: btnclick(8), bg="palegreen").grid(row=3,column=1)
        btn9 = Button(self.FTR, height=2,width=5, text="9", bd=5, command=lambda: btnclick(9), bg="palegreen").grid(row=3,column=2)
        #-----------------------Button in Third Row-----------------------------------------------
        btn4 = Button(self.FTR, height=2,width=5, text="4", bd=5, command=lambda: btnclick(4), bg="palegreen").grid(row=4,column=0)
        btn5 = Button(self.FTR, height=2,width=5, text="5", bd=5, command=lambda: btnclick(5), bg="palegreen").grid(row=4,column=1)
        btn6 = Button(self.FTR, height=2,width=5, text="6", bd=5, command=lambda: btnclick(6), bg="palegreen").grid(row=4,column=2)
        btnce = Button(self.FTR, height=2,width=5, text="=", bd=5, command=btnEqualsInput,bg="greenyellow").grid(row=4,column=3)
        #-----------------------Button in Fourth Row----------------------------------------------
        btn1 = Button(self.FTR, height=2,width=5, text="1", bd=5, command=lambda: btnclick(1), bg="palegreen").grid(row=5,column=0)
        btn2 = Button(self.FTR, height=2,width=5, text="2", bd=5, command=lambda: btnclick(2), bg="palegreen").grid(row=5,column=1)
        btn3 = Button(self.FTR, height=2,width=5, text="3", bd=5, command=lambda: btnclick(3), bg="palegreen").grid(row=5,column=2)
        btn0 = Button(self.FTR, height=2,width=5, text="0", bd=5, command=lambda: btnclick(0), bg="palegreen").grid(row=5,column=3)
        # Label(self.FTR).grid(row=5,column=0)
        
        #-----------------------Button For Insert The Record in Database--------------------------
        self.disbtn = Button(self.FBR, text="Displayitem", command=Displayitem, bg="greenyellow").grid(row=2,column=0)
        self.btndetails = Button(self.frame, bg="greenyellow", text="Receipt Preview", command=receipt).grid(row=4,column=0)
        self.btnbillprint = Button(self.FBL, text="Receipt Print", bg="greenyellow" , command=print1).grid(row=2,column=0,sticky=W)
        self.btnwatch = Button(self.FBR, text="For See Analog Watch, Push Me", bg="greenyellow" , height=2, command=watch).grid(row=3,column=0)
        


if __name__ == "__main__":
    root = Tk()
    root.geometry("750x500+0+0")
    # root.config(bg="powderblue")
    root.resizable(width=False, height=False)# don't resize the form
    app=Billing(root)
    mainloop()