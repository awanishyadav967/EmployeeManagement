from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk

class Employee:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Employee Management System')
        lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',37,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)
        img_logo=Image.open('college_images/Logo.png')
        img_logo=img_logo.resize((50,50),Image.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=270,y=0,width=50,height=50)

        #image frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160)

        #1st
        img1=Image.open('college_images/frame.png')
        img1=img1.resize((540,160),Image.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)

        #2nd
         
        img2=Image.open('college_images/frame5.png')
        img2=img2.resize((540,160),Image.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=540,y=0,width=540,height=160)

         #3rd
        img3=Image.open('college_images/frame7.png')
        img3=img3.resize((540,160),Image.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=1080,y=0,width=540,height=160)

        #main frame

        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=220,width=1500,height=560)

        #upper frame
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Employee Information',font=('times new roman',11,'bold'),fg='red',bg='white')
        upper_frame.place(x=10,y=10,width=1480,height=270)
        # Labels and  Entry fields 

        #Department

        lbl_dep=Label(upper_frame,text='Department',font=('arial',11,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)
        combo_dep=ttk.Combobox(upper_frame,font=('arial',12,'bold'),width=17,state='readonly')
        combo_dep['value']=('select Department','HR','Software Engineer','manager')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=6,pady=7,sticky=W)

        #Designation 
        
        lbl_des=Label(upper_frame,text='Designation',font=('arial',11,'bold'),bg='white')
        lbl_des.grid(row=1,column=0,padx=2,sticky=W)
        Text.des=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"))
        Text.des.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        #Address
        lbl_add=Label(upper_frame,text='Address',font=('arial',11,'bold'),bg='white')
        lbl_add.grid(row=2,column=0,padx=2,sticky=W)
        Text.add=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"))
        Text.add.grid(row=2,column=1,sticky=W,padx=2,pady=7)

         #DOB
        lbl_DOB=Label(upper_frame,text='DOB',font=('arial',11,'bold'),bg='white')
        lbl_DOB.grid(row=3,column=0,padx=2,sticky=W)
        Text.DOB=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"))
        Text.DOB.grid(row=3,column=1,sticky=W,padx=2,pady=7)

         #SELECT ID PROOF
        lbl_ID=Label(upper_frame,text='Select ID Proof',font=('arial',11,'bold'),bg='white')
        lbl_ID.grid(row=4,column=0,padx=2,sticky=W)

        combo_ID=ttk.Combobox(upper_frame,font=('arial',12,'bold'),width=17,state='readonly')
        combo_ID['value']=("select","Adhaar Card","Driving Licence","Pan Card","Other")
        combo_ID.current(0)
        combo_ID.grid(row=4,column=1,sticky=W,padx=2,pady=7)

       

        

         #NAME
        lbl_name=Label(upper_frame,text='Name',font=('arial',11,'bold'),bg='white')
        lbl_name.grid(row=0,column=5,padx=2,sticky=W)
        Text.name=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"))
        Text.name.grid(row=0,column=6,sticky=W,padx=2,pady=7)

         #EMAIL
        lbl_email=Label(upper_frame,text='Email',font=('arial',11,'bold'),bg='white')
        lbl_email.grid(row=1,column=5,padx=2,sticky=W)
        Text.email=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"))
        Text.email.grid(row=1,column=6,sticky=W,padx=2,pady=7)

         #Married Status
        lbl_married=Label(upper_frame,text='Married Status',font=('arial',11,'bold'),bg='white')
        lbl_married.grid(row=2,column=5,padx=2,sticky=W)
        combo_married=ttk.Combobox(upper_frame,font=('arial',12,'bold'),width=17,state='readonly')
        combo_married['value']=("select","Married","NOT Married")
        combo_married.current(0)
        combo_married.grid(row=2,column=6,sticky=W,padx=2,pady=7)

         #DOJ
        lbl_DOJ=Label(upper_frame,text='DOJ',font=('arial',11,'bold'),bg='white')
        lbl_DOJ.grid(row=3,column=5,padx=2,sticky=W)
        Text.DOJ=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"))
        Text.DOJ.grid(row=3,column=6,sticky=W,padx=2,pady=7)

         #GENDER
        lbl_GENDER=Label(upper_frame,text='Gender',font=('arial',11,'bold'),bg='white')
        lbl_GENDER.grid(row=4,column=5,padx=2,sticky=W)
        combo_GENDER=ttk.Combobox(upper_frame,font=('arial',12,'bold'),width=17,state='readonly')
        combo_GENDER['value']=("select","Male","Female","Other")
        combo_GENDER.current(0)
        combo_GENDER.grid(row=4,column=6,sticky=W,padx=2,pady=7)

         #phone no.
        lbl_PHONE=Label(upper_frame,text='Phone NO.',font=('arial',11,'bold'),bg='white')
        lbl_PHONE.grid(row=0,column=7,padx=2,sticky=W)
        Text.PHONE=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"))
        Text.PHONE.grid(row=0,column=8,sticky=W,padx=2,pady=7)

        #COUNTRY
        lbl_country=Label(upper_frame,text='Country',font=('arial',11,'bold'),bg='white')
        lbl_country.grid(row=1,column=7,padx=2,sticky=W)
        Text.country=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"))
        Text.country.grid(row=1,column=8,sticky=W,padx=2,pady=7)

        #SALARY(CTC)
        lbl_salary=Label(upper_frame,text='Salary(CTC)',font=('arial',11,'bold'),bg='white')
        lbl_salary.grid(row=2,column=7,padx=2,sticky=W)
        Text.salary=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"))
        Text.salary.grid(row=2,column=8,sticky=W,padx=2,pady=7)



        #button frame
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1290,y=10,width=170,height=210)

        
        btn_add=Button(button_frame,text="Save",font=("arial",15,"bold"),width=13,bg='#BFBFEF')
        btn_add.grid(row=0,column=0,padx=1,pady=5)

        btn_update=Button(button_frame,text="Update",font=("arial",15,"bold"),width=13,bg='#BFBFEF')
        btn_update.grid(row=1,column=0,padx=1,pady=5)

        
        btn_delete=Button(button_frame,text="Delete",font=("arial",15,"bold"),width=13,bg='#BFBFEF')
        btn_delete.grid(row=2,column=0,padx=1,pady=5)

        
        btn_clear=Button(button_frame,text="Clear",font=("arial",15,"bold"),width=13,bg='#BFBFEF')
        btn_clear.grid(row=3,column=0,padx=1,pady=5)



     
       



         #down frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Employee Information Table',font=('times new roman',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=280,width=1480,height=270)


       









        
if __name__=="__main__":
    root= Tk()
    obj=Employee(root)
    root.mainloop()