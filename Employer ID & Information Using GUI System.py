#Employer ID & Information Using GUI System
#Programmer: Rishi Patel
#Date: 21/06/2021
#Version: 1.0

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import string
import sys

window = Tk()
window.geometry("400x300")
window.resizable(False, False)

lbl1=Label(window,text="Employee ID")
lbl1.grid(row=0,column=0,pady=5,padx=20)

txt1=Entry(window,width=30)
txt1.grid(row=0,column=1,sticky="NEWS",pady=5)

lbl2=Label(window,text="First Name")
lbl2.grid(row=1,column=0,pady=5,padx=20)

txt2=Entry(window,width=30)
txt2.grid(row=1,column=1,sticky="NEWS",pady=5)

lbl3=Label(window,text="Last Name")
lbl3.grid(row=2,column=0,pady=5,padx=20)

txt3=Entry(window,width=30)
txt3.grid(row=2,column=1,sticky="NEWS",pady=5)

lbl4=Label(window,text="Date of Birth")
lbl4.grid(row=3,column=0,pady=5,padx=20)

frame1=Frame(window)
frame1.grid(row=3,column=1)

combo1=ttk.Combobox(frame1,width=9,state="readonly")
combo1.grid(row=0,column=0)
combo1["values"]=("Select One",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
combo1.current(0)

combo2=ttk.Combobox(frame1,width=9,state="readonly")
combo2.grid(row=0,column=1,padx=5)
combo2["values"]=("Select One","January","Febuary","March","April","May","June","July","August","September","October","November","December")
combo2.current(0)

combo3=ttk.Combobox(frame1,width=9,state="readonly")
combo3.grid(row=0,column=2)
combo3["values"]=("Select One",1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,
                  1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,
                  2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021)
combo3.current(0)

lbl5=Label(window,text="Email ID")
lbl5.grid(row=4,column=0,pady=5,padx=20)

txt4=Entry(window,width=30)
txt4.grid(row=4,column=1,sticky="NEWS",pady=5)

lbl6=Label(window,text="Passport Holder")
lbl6.grid(row=5,column=0,pady=5,padx=20)

frame2=Frame(window)
frame2.grid(row=5,column=1)

a=IntVar()
radiobutton1=Radiobutton(frame2,text="Yes",value=1,variable=a)
radiobutton1.grid(row=0,column=0)

radiobutton2=Radiobutton(frame2,text="No",value=2,variable=a)
radiobutton2.grid(row=0,column=1)

def submit():
    s=txt1.get()
    digits=string.digits
    if len(s)==7:
        if s[0]!="P":
            messagebox.showerror("Error","Invalid Employee ID")
            txt1.focus()
            return
        else:
            for i in range(1,7):
                if s[i] not in digits:
                    messagebox.showerror("Error","Invalid Employee ID")
                    txt1.focus()
                    return     
    else:
        messagebox.showerror("Error","Invalid Employee ID")
        txt1.focus()
        return
    
    if txt2.get()=="":
        messagebox.showerror("Error","Blank First Name Entry")
        txt2.focus()
        return
    if txt3.get()=="":
        messagebox.showerror("Error","Blank Last Name Entry")
        txt3.focus()
        return

    if combo1.current()==0:
        messagebox.showerror("Error","Select a Date")
        combo1.focus()
        return
    if combo2.current()==0:
        messagebox.showerror("Error","Select a Month")
        combo2.focus()
        return
    if combo3.current()==0:
        messagebox.showerror("Error","Select a Year")
        combo3.focus()
        return

    s1=txt4.get()
    letters=string.ascii_lowercase
    up_letters=string.ascii_uppercase
    if len(s1)==15:
        if (s1[0] not in letters) or (s1[1] not in letters) or (s1[2] not in letters):
            messagebox.showerror("Error","Invalid Email ID Entry")
            txt4.focus()
            return
        if s1[3] not in up_letters:
            messagebox.showerror("Error","Invalid Email ID Entry")
            txt4.focus()
            return
        if (s1[4] not in letters) or (s1[4] not in letters) or (s1[6] not in letters) or (s1[7] not in letters):
            messagebox.showerror("Error","Invalid Email ID Entry")
            txt4.focus()
            return
        if s1[8]!="@":
            messagebox.showerror("Error","Invalid Email ID Entry")
            txt4.focus()
            return
        if (s1[9] not in up_letters) or (s1[10] not in up_letters) or (s1[11] not in up_letters):
            messagebox.showerror("Error","Invalid Email ID Entry")
            txt4.focus()
            return
        if s1[12]!=".":
            messagebox.showerror("Error","Invalid Email ID Entry")
            txt4.focus()
            return
        if (s1[13] not in digits) or (s1[14] not in digits):
            messagebox.showerror("Error","Invalid Email ID Entry")
            txt4.focus()
            return

        if (a.get()!=1) and (a.get()!=2):
            messagebox.showerror("Error","Are you a passport holder?")
            radiobutton1.focus()
            return
    else:
        messagebox.showerror("Error","Invalid Email ID Entry?")
        radiobutton1.focus()
        return

    messagebox.showinfo("Success","Employee Information Saved!")
    window.destroy()
    sys.exit()
        
    

btn1=Button(window,text="Submit",width=10,height=2,command=submit)
btn1.grid(row=6,column=0,sticky="E",pady=20)

def cancel():
    window.destroy()
    sys.exit()

btn1=Button(window,text="Cancel",width=10,height=2,command=cancel)
btn1.grid(row=6,column=1,sticky="W",pady=20,padx=20)

window.mainloop()

#Teacher's Solution

"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import string
import sys

window = Tk()
window.title("Sample GUI form")
window.geometry("330x180")
window.resizable(False, False)

lbl1=Label(window,text="Employee ID:",font=("arial black",10))
lbl1.grid(row=0,column=0,ipadx=5,sticky="e")
empid=StringVar()
txt1=Entry(window,width=20,font=("arial black",10),textvariable=empid)
txt1.grid(row=0,column=1,sticky="w")



lbl2=Label(window,text="First Name:",font=("arial black",10))
lbl2.grid(row=1,column=0,ipadx=5,sticky="e")
fname=StringVar()
txt2=Entry(window,width=20,font=("arial black",10),textvariable=fname)
txt2.grid(row=1,column=1,sticky="w")


lbl3=Label(window,text="Last Name:",font=("arial black",10))
lbl3.grid(row=2,column=0,ipadx=5,sticky="e")
lname=StringVar()
txt3=Entry(window,width=20,font=("arial black",10),textvariable=lname)
txt3.grid(row=2,column=1,sticky="w")


frame1=Frame(window)
frame1.grid(row=3,column=1,sticky="w")
lbl4=Label(window,text="Date of Birth:",font=("arial black",10))
lbl4.grid(row=3,column=0,ipadx=5,sticky="e")
daycombo=ttk.Combobox(frame1,state="readonly",width=5)
daycombo.grid(row=0,column=0,sticky="w")
v=[]
v.append("Day")
for i in range(1,32):
    v.append(i)
daycombo["values"]=v    
daycombo.current(0)

monthcombo=ttk.Combobox(frame1,state="readonly",width=10)
monthcombo.grid(row=0,column=1,sticky="w")
monthcombo["values"]=("Month","January","Fenruary","March","April","May","June","July","August",
                    "september","October","November","december")
monthcombo.current(0)

yearcombo=ttk.Combobox(frame1,state="readonly",width=5)
yearcombo.grid(row=0,column=2,sticky="w")
v=[]
v.append("Year")
for i in range(1950,2022):
    v.append(i)
yearcombo["values"]=v    
yearcombo.current(0)

lbl5=Label(window,text="Email ID:",font=("arial black",10))
lbl5.grid(row=4,column=0,ipadx=5,sticky="e")
emailid=StringVar()
txt4=Entry(window,width=20,font=("arial black",10),textvariable=emailid)
txt4.grid(row=4,column=1,sticky="w")

lbl6=Label(window,text="Passport Holder:",font=("arial black",10))
lbl6.grid(row=5,column=0,ipadx=5,sticky="e")
frame2=Frame(window)
frame2.grid(row=5,column=1,sticky="w")
yesno=IntVar()
rb1=Radiobutton(frame2,text="Yes",variable=yesno,value=1)
rb1.grid(row=0,column=0)

rb2=Radiobutton(frame2,text="No",variable=yesno,value=2)
rb2.grid(row=0,column=1)

frame3=Frame(window)
frame3.grid(row=6,column=0,columnspan=2,sticky="EW")

def errormsg(s):
    messagebox.showerror("Error",s)
    return

def validemailid():
    s=emailid.get().strip()
    if len(s)!=15:
        return False

    if not s[3] in string.ascii_uppercase:
        return False
    a=s[:3]+s[4:8]
    for i in range(len(a)):
        if not a[i] in string.ascii_lowercase:
            return False
    
def dosubmit():
    s=empid.get().strip()
    if s=="":
        errormsg("Invalid Employee ID")
        txt1.focus()
        return
    
    s=fname.get().strip()
    if s=="":
        errormsg("Invalid First Name")
        txt2.focus()
        return
    
    s=lname.get().strip()
    if s=="":
        errormsg("Invalid Last Name")
        txt3.focus()
        return

    if daycombo.current()==0:
        errormsg("Pick a Day")
        daycombo.focus()
        return

    if monthcombo.current()==0:
        errormsg("Pick a Month")
        monthcombo.focus()
        return

    if yearcombo.current()==0:
        errormsg("Pick a Year")
        yearcombo.focus()
        return

    if not validemailid:
        errormsg("Invalid Email ID")
        txt4.focus()
        return

submit=Button(frame3,text="Submit",font=("arial black",10),command=dosubmit)
submit.grid(row=0,column=0,sticky="E",padx=5)

def docancel():
    if messagebox.askyesno("Warning","You will lose all the information. Are you sure?"):
        window.destroy()
        sys.exit()
    else:
        return

cancel=Button(frame3,text="Cancel",font=("arial black",10),command=docancel)
cancel.grid(row=0,column=1,sticky="W",padx=5)
frame3.columnconfigure(0,weight=1)
frame3.columnconfigure(1,weight=1)

txt1.focus()
window.eval("tk::PlaceWindow . center")
window.mainloop()
"""
