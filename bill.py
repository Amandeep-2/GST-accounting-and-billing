from tkinter import *
import insertbill,gstformattestfile,os,merge,xmlfile
from tkinter import messagebox
import xml.etree.ElementTree as et
''' Class to confirm the Details of Bill no.
So that the Bill can be created and stored in a directory.'''
def insert(self,btn,master):
    '''try:
        file=open(master.dirr+"billno.txt","a+")
        file.write(str(master.n)+"\t"+self.detail[0][:12]+str(self.gtotal)[:3]+"\t"+master.date.get()+"\n")
        file.close()
    except:
        file=open(master.dirr+"billno.txt","w+")
        file.write(str(master.n)+"\t"+self.detail[0][:12]+str(self.gtotal)[:3]+"\t"+master.date.get()+"\n")
        file.close()'''
    gstformattestfile.create(self)
    btn["state"]="disabled"
def amount(value):
    ones=[" Zero"," One"," Two"," Three"," Four"," Five"," Six"," Seven",
              " Eight"," Nine"]
    tens=["P","W"," Twenty"," Thirty"," Forty"," Fifty"," Sixty"," Seventy",
                  " Eighty"," Ninty"]
    te=[" Ten"," Eleven"," Twelve"," Thirteen"," Fourteen"," Fifteen",
        " Sixteen"," Seventeen"," Eighteen"," Ninteen"]
    vale,name=[" Arab"," Karore"," Lakh"," Thousand"," Hundred"," and"],[]
    aman,p="",-1
    no,on=[],[]
    value=str(int(value))
    if len(value)==1:
        return ones[int(value)]+" Only"
    elif len(value)==2:
        if value[0]=='1':
            return te[int(value[1])]+" Only"
        elif value[1]=='0':
            return tens[int(value[0])]+" Only"
        else:
            return tens[int(value[0])]+ones[int(value[1])]+" Only"
    if len(value)%2==0:
        value="0"+value
    if len(value)==3:
        value="00"+value
    if len(value)>3:
        name.insert(0,value[-2:])
        name.insert(0,value[-3])
        for i in range(-4,-1*len(value),-2):
            name.insert(0,value[i-1:i+1])
    for i in name:
        if int(i)==0:
            a=" Zero"
        if int(i)<10:
            a=ones[int(i)]
        elif int(i)>=20:
            a=tens[int(i[0])]
            if int(i[1])!=0:
                a=a+ones[int(i[1])]
        else :
            a=te[int(i[1])]
        no.append(a)
    for i in range(-1,-1*len(no)-1,-1):
        on.insert(0,vale[i])
        on.insert(0,no[i])
        if no[i]==" Zero":
            del(on[0])
            del(on[0])
    on.append(" Only")
    try:
        if on[-2]==" and":
            del on[-2]
    except:
        print("bill file :- "+"Error in 72 Bill.py")
    try:
        if on[-3] in vale:
            on.insert(-2," and")
    except Exception as e:
        print("bill file :- "+e,"Error in 74 value")
    aman=aman.join(on)
    return aman

class create(Frame):
    def __init__(self,sel,master):
        if master!=None:
            master.pack_forget()
        Frame.__init__(self,sel)
        self.pack(fill=BOTH,expand=True)
        self.gst=master.gst
        self.tcs=master.gst[0][4]
        self.total,self.cgst=0,0
        self.sgst,self.igst=0,0
        self.cessu,self.tcst=0,0
        self.data,self.detail=master.data,master.detail
        self.gtotal=0
        self.dirr=master.dirr
        try:
            self.billdetail=master.billdetail
            for i in master.data:
                self.total=round(self.total + float(i[9]),2)
            # First frame start
            for i in range(len(master.gst)):
                s=float(master.data[i][9])/100+round(master.gst[i][4]*float(master.data[i][9])/100,2)
                print("bill file :- ",str(s),str(master.gst[i][2]*s))                
                self.cessu=round(self.cessu+master.gst[i][3]*float(master.data[i][6]),2)
                self.tcst=round(self.tcst+master.gst[i][4]*float(master.data[i][9])/100,2)
                self.cgst=round(self.cgst+master.gst[i][0]*round(float(master.data[i][9])+master.gst[i][4]*float(master.data[i][9])/100,2)/100,2)
                self.sgst=round(self.sgst+master.gst[i][1]*round(float(master.data[i][9])+master.gst[i][4]*float(master.data[i][9])/100,2)/100,2)
                self.igst=round(self.igst+master.gst[i][2]*round(float(master.data[i][9])+master.gst[i][4]*float(master.data[i][9])/100,2)/100,2)   
            self.gtotal=round(self.total+self.cgst+self.igst+self.sgst+self.cessu+self.tcst,2)
            self.billdetail.append(str(amount(round(self.gtotal))))
        except Exception as e:
            messagebox.showinfo(title="Error Message",message="Bill File 108 There is Error "+str(e)+" Please try Again")
        ffrm=Frame(self,borderwidth=1,bg="black")
        ffrm.pack(ipadx=2,ipady=2,padx=10,pady=10,expand=True)
        # First Frame end Second start
        afrm=Frame(ffrm,borderwidth=1,bg="black")
        frfm=Frame(afrm)
        frfm.pack(side=LEFT,fill=BOTH,expand=True)
        frm2=Frame(frfm)
        Label(frm2,text="M/s ").pack(side=LEFT,anchor=NW)
        Label(frm2,text=self.detail[0]).pack(side=LEFT,anchor=N)
        frm2.pack(fill=BOTH,expand=True)
        frm0=Frame(frfm)
        Label(frm0,text="Party GSTIN No.").pack(side=LEFT,anchor=NW)
        Label(frm0,text=self.detail[-1]).pack(side=LEFT,anchor=N)
        frm0.pack(fill=BOTH,expand=True)
        #second frame end third start
        s1frm=Frame(afrm)
        s2frm=Frame(s1frm)
        frm3=Frame(s1frm)
        frm3.pack(fill=BOTH,expand=True)
        s2frm.pack(fill=BOTH,expand=True)
        lbl6=Label(frm3,text="Invoice no "+str(master.n))
        lbl6.pack(side=LEFT)
        lbl7=Label(frm3,text="Date:").pack(side=RIGHT,anchor=N)
        Label(frm3,text=master.date.get()).pack(side=RIGHT,anchor=NE)
        Label(s2frm,text="Challan No.").pack(side=LEFT)
        Label(s2frm,text=master.chlnno.get()).pack(side=RIGHT)
        Label(s1frm,text="Party P.O. No.:").pack(side=LEFT,anchor=NW)
        Label(s1frm,text=master.ppno.get()).pack(side=RIGHT,anchor=N)
        Label(s1frm,text="Vehicle No").pack(side=LEFT,anchor=NW)
        Label(s1frm,text=master.vno.get()).pack(side=RIGHT,anchor=N)
        Label(s1frm,text="E-way No").pack(side=LEFT,anchor=NW)
        Label(s1frm,text=master.ewayno.get()).pack(side=RIGHT,anchor=N)
        s1frm.pack(side=RIGHT,fill=BOTH)
        afrm.pack(fill=BOTH)
        #3rd end 4th start
        frm4=Frame(ffrm,bg="black")
        sfrm4=Frame(frm4)
        dfrm4=Frame(frm4)
        dfrm4.pack(fill=X,expand=True)
        sfrm4.pack(fill=BOTH,expand=True)
        Label(dfrm4,text="Sr No.").grid(row=1,column=0,padx=5)
        Label(dfrm4,text="Description of Goods").grid(row=1,column=1,padx=5)
        Label(dfrm4,text="CESS").grid(row=1,column=2,padx=5)
        Label(dfrm4,text="TCS/TDS").grid(row=1,column=3,padx=5)
        Label(dfrm4,text="GST RATE").grid(row=1,column=4,padx=5)
        Label(dfrm4,text="HSN No").grid(row=1,column=5,padx=5)
        Label(dfrm4,text="Quantity").grid(row=1,column=6,padx=5)
        Label(dfrm4,text="Rate").grid(row=1,column=7,padx=5)
        Label(dfrm4,text="per").grid(row=1,column=8,padx=5)
        Label(dfrm4,text="Taxable Amount").grid(row=1,column=9,padx=5)
        width=[8,30,10,10,10,10,8,8,8,15]
        for j in self.data:
            fdrm=Frame(sfrm4)
            fdrm.pack(fill=BOTH)
            for i in range(10):
                ama=j[i]
                text1=Label(dfrm4,text=ama)
                text1.grid(row=2,column=i,padx=5)
        frm4.pack(fill=BOTH)
        #4th frame end 5th start
        frm5=Frame(ffrm,borderwidth=1,bg="black")
        sdfrm=Frame(frm5)
        dsfrm=Frame(frm5)
        sdfrm.pack(fill=BOTH)
        dsfrm.pack(fill=BOTH,expand=True)
        labl6=Label(sdfrm,text="Amount in Words :")
        labl6.pack(side=LEFT,fill=BOTH)
        ama=self.detail[-1]
        if len(ama)>width[i]:
                    ama=ama[:width[i]]+"\n"+ama[width[i]:]
        Label(sdfrm,text=ama,width=30).pack(side=LEFT,fill=BOTH,pady=5)
        Label(sdfrm,text="Transporter Details:").pack(side=LEFT,fill=BOTH)
        Label(sdfrm,text=master.tname.get()).pack(side=LEFT,fill=BOTH)
        Label(sdfrm,text="Reverse Charge").pack(side=LEFT,fill=BOTH)
        Label(sdfrm,text=master.rev[master.rchrg.get()]).pack(side=LEFT,fill=BOTH)        
        frm5.pack(side=LEFT,fill=BOTH,expand=True)
        #5th end 6th start
        lfrm=Frame(ffrm)
        frm6=Frame(lfrm,borderwidth=1,bg="black")
        try:
            Label(frm6,text="Total:                                      "+str(self.total)).pack(fill=BOTH,expand=True)
            Label(frm6,text="CGST @       "+str(master.gst[0][0])+"      "+str(self.cgst)).pack(fill=BOTH,expand=True)
            Label(frm6,text="SGST @       "+str(master.gst[0][1])+"      "+str(self.sgst)).pack(fill=BOTH,expand=True)
            Label(frm6,text="IGST @       "+str(master.gst[0][2])+"      "+str(self.igst)).pack(fill=BOTH,expand=True)
            Label(frm6,text="Cess @       "+str(master.gst[0][3])+"      "+str(self.cessu)).pack(fill=BOTH,expand=True)
            Label(frm6,text="TCS/TDS @      "+str(master.gst[0][4])+"      "+str(self.tcst)).pack(fill=BOTH,expand=True)
            Label(frm6,text="GST Total:                               "+str(self.gtotal)).pack(fill=BOTH,expand=True)
            frm6.pack(fill=BOTH,expand=True)
        except Exception as e:
            messagebox.showinfo(title="Error Message",message="Bill File 198 There is Error "+str(e)+" Please try Again")
        lfrm.pack(side=RIGHT,fill=BOTH,expand=True)
        btn=Button(self,text="Insert Data",command=lambda:insert(self,btn,master))
        btn.pack(expand=True)
        btn1=Button(self,text="Back",command=lambda:self.show(master))
        btn1.pack(expand=True)
    def show(self,master):
        self.pack_forget()
        master.pack(fill=BOTH,expand=True)
