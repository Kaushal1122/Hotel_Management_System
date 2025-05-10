from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #=================variables==================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noOfdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_subtotal=StringVar()
        self.var_totalcost=StringVar()

        #=================title==================
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


        #=================logo==================
        img2=Image.open(r"D:\Hotel_Management_System\images\logohotel.png")
        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #=================label frame==================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("arial",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #=================label and entries==================
        #Customer Contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,font=("arial",13,"bold"),width=20)
        entry_contact.grid(row=0,column=1,sticky=W)

        #Fetch data button
        btnFetchData=Button(labelframeleft,command=self.Fetch_Contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=347,y=4)

        #Check-in date
        check_in_date=Label(labelframeleft,text="Check-in Date:",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,font=("arial",13,"bold"),width=29)
        txtcheck_in_date.grid(row=1,column=1)

        #Check-out date
        lbl_Check_out=Label(labelframeleft,text="Check-out Date:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_Check_out.grid(row=2,column=0,sticky=W)
        txt_Check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout,font=("arial",13,"bold"),width=29)
        txt_Check_out.grid(row=2,column=1)

        #Room Type
        label_RoomType=Label(labelframeleft,text="Room Type:",font=("arial",12,"bold"),padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=("Standard","Deluxe","Suite")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        #Available Room
        lblRoomAvailable=Label(labelframeleft,text="Available Room:",font=("arial",12,"bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,font=("arial",13,"bold"),width=29)
        txtRoomAvailable.grid(row=4,column=1)

        #Meal
        lblMeal=Label(labelframeleft,text="Meal:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,font=("arial",13,"bold"),width=29)
        txtMeal.grid(row=5,column=1)
        

        #No of days
        lblNoOfDays=Label(labelframeleft,text="No of Days:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noOfdays,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=6,column=1)

        #Paid Tax
        lblPaidTax=Label(labelframeleft,text="Paid Tax:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPaidTax.grid(row=7,column=0,sticky=W)
        txtPaidTax=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,font=("arial",13,"bold"),width=29)
        txtPaidTax.grid(row=7,column=1)

        #Sub Total
        lblSubTotal=Label(labelframeleft,text="Sub Total:",font=("arial",12,"bold"),padx=2,pady=6)
        lblSubTotal.grid(row=8,column=0,sticky=W)
        txtSubTotal=ttk.Entry(labelframeleft,textvariable=self.var_subtotal,font=("arial",13,"bold"),width=29)
        txtSubTotal.grid(row=8,column=1)

        #Total Cost
        lblTotalCost=Label(labelframeleft,text="Total Cost:",font=("arial",12,"bold"),padx=2,pady=6)
        lblTotalCost.grid(row=9,column=0,sticky=W)
        txtTotalCost=ttk.Entry(labelframeleft,textvariable=self.var_totalcost,font=("arial",13,"bold"),width=29)
        txtTotalCost.grid(row=9,column=1)

        #Bill Button
        btnBill=Button(labelframeleft,text="Bill",font=("arial",11,"bold"),bg="black",fg="gold",width=9)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)


        #================buttons==================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        #=================right side image==================

        img3=Image.open(r"D:\Hotel_Management_System\images\bed.jpg")
        img3=img3.resize((520,300),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=520,height=200)        

        #=================table frame search system==================

        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2)
        Table_frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(Table_frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()

        combo_Search=ttk.Combobox(Table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Search["value"]=("Contact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()

        txtSearch=ttk.Entry(Table_frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_frame,text="Search",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_frame,text="Show All",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        #=================Show data table==================

        details_table=Frame(Table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfdays",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact No")
        self.room_table.heading("checkin",text="Check-in Date")
        self.room_table.heading("checkout",text="Check-out Date")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="No of Days")

        self.room_table["show"]="headings"
        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)
        self.fetch_data()

    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Kaushal@2815",database="kaushal")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_contact.get(),
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noOfdays.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room "booked successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)
    
    #=================fetch data==================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Kaushal@2815",database="kaushal")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()



    #=================All data fetch==================

    def Fetch_Contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Kaushal@2815",database="kaushal")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","No record found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataFrame.place(x=450,y=55,width=300,height=180)

                #=================Name==================

                lblName=Label(showDataFrame,text="Name",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

                #=================Gender==================

                conn=mysql.connector.connect(host="localhost",username="root",password="Kaushal@2815",database="kaushal")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataFrame,text="Gender",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)

                #=================Email==================
                conn=mysql.connector.connect(host="localhost",username="root",password="Kaushal@2815",database="kaushal")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblEmail=Label(showDataFrame,text="Email",font=("arial",12,"bold"))
                lblEmail.place(x=0,y=60)

                lbl3=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)

                #=================Nationality==================

                conn=mysql.connector.connect(host="localhost",username="root",password="Kaushal@2815",database="kaushal")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblNationality=Label(showDataFrame,text="Nationality",font=("arial",12,"bold"))
                lblNationality.place(x=0,y=90)

                lbl4=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl4.place(x=90,y=90)

                #=================Address==================

                conn=mysql.connector.connect(host="localhost",username="root",password="Kaushal@2815",database="kaushal")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                lblAddress=Label(showDataFrame,text="Address",font=("arial",12,"bold"))
                lblAddress.place(x=0,y=120)

                lbl5=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl5.place(x=90,y=120)





if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()