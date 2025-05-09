from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk

class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")



        #=================title==================
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


        #=================logo==================
        img2=Image.open(r"D:\Hotel_Management_System\images\logohotel.png")
        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #=================label frame==================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("arial",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490) 

        #=================label and entries==================
        #Customer Ref
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        entry_ref.grid(row=0,column=1)

        #custname
        cname=Label(labelframeleft,text="Customer Name",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtcname.grid(row=1,column=1)

        #MotherName
        lblname=Label(labelframeleft,text="Mother Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtmname.grid(row=2,column=1)

        #gender combobox
        label_gender=Label(labelframeleft,font=("arial",12,"bold"),text="Gender:",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)




        #postalcode
        lblPostCode=Label(labelframeleft,text="Postal Code:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=4,column=1)

        #mobilenumber
        lblMobile=Label(labelframeleft,text="Mobile Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=5,column=1)

        #email
        lblEmail=Label(labelframeleft,text="Email:",font=("arial",12,"bold"),padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtEmail.grid(row=6,column=1)

        #nationality
        lblNationality=Label(labelframeleft,font=("arial",12,"bold"),text="Nationality:",padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)

        combo_Nationality=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Nationality["value"]=("Indian","Russian","American","British","Other")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)

        #idproof type combobox
        lblIdProof=Label(labelframeleft,text="ID Proof Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_id["value"]=("Aadhar Card","Driving License","Passport","Pan Card","Other")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)

        # id number
        lblIdNumber=Label(labelframeleft,font=("arial",12,"bold"),text="Id Number:",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtIdNumber.grid(row=9,column=1)

        # address
        lblAddress=Label(labelframeleft,font=("arial",12,"bold"),text="Address:",padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtAddress.grid(row=10,column=1)

        #================buttons==================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        #=================table frame==================

        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2)
        Table_frame.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(Table_frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W)

        combo_Search=ttk.Combobox(Table_frame,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Search["value"]=("Mobile Number","Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        txtSearch=ttk.Entry(Table_frame,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_frame,text="Search",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_frame,text="Show All",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)


        #=================Show data table==================

        details_table=Frame(Table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.cust_table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_table.xview)
        scroll_y.config(command=self.cust_table.yview)

        self.cust_table.heading("ref",text="Reference No")
        self.cust_table.heading("name",text="Customer Name")
        self.cust_table.heading("mother",text="Mother Name")
        self.cust_table.heading("gender",text="Gender")
        self.cust_table.heading("post",text="Postal Code")
        self.cust_table.heading("mobile",text="Mobile No")
        self.cust_table.heading("email",text="Email")
        self.cust_table.heading("nationality",text="Nationality")
        self.cust_table.heading("idproof",text="ID Proof Type")
        self.cust_table.heading("idnumber",text="ID Number")
        self.cust_table.heading("address",text="Address")

        self.cust_table["show"]="headings"
        self.cust_table.column("ref",width=100)
        self.cust_table.column("name",width=100)
        self.cust_table.column("mother",width=100)
        self.cust_table.column("gender",width=100)
        self.cust_table.column("post",width=100)
        self.cust_table.column("mobile",width=100)
        self.cust_table.column("email",width=100)
        self.cust_table.column("nationality",width=100)
        self.cust_table.column("idproof",width=100)
        self.cust_table.column("idnumber",width=100)
        self.cust_table.column("address",width=100)
        
        self.cust_table.pack(fill=BOTH,expand=1)






 


if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()