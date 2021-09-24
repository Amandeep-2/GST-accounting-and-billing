from tkinter import *
import time,xmlfile,merge,newworkbook
'''This file inserts bill of Seller".It calls Bill File"'''
def gener():
    root=Tk()
    btn=App(root,None)
    root.title("GST Bill Format")
    root.mainloop()
class App(Frame):
    def __init__(self,master,sel):
        self.master=master
        master.title("GST Bill")
        master.geometry("700x500+100+100")
        self.sel=sel
        if sel!=None:
            sel.pack_forget()
        Frame.__init__(self,master)
        self.pack(fill=BOTH,expand=True)
        self.no,self.msad1=StringVar(),StringVar()
        self.pgst=StringVar()
        self.ms=StringVar()
        self.amount=StringVar()
        self.ppno=StringVar()
        self.date=StringVar()
        self.eway,self.vno=StringVar(),StringVar()
        self.gst,self.owner=StringVar(),StringVar()
        self.variable=[]
        user=StringVar()
        userdata=merge.alluser()
        # First frame start
        ffrm=Frame(self,borderwidth=1,bg="black")
        ffrm.pack(ipadx=2,ipady=2,padx=10,pady=10,expand=True)
        # First Frame end Second start
        afrm=Frame(ffrm,borderwidth=1,bg="black")
        frm2=Frame(afrm)
        afrm2=Frame(frm2)
        afrm2.pack(expand=True,side=LEFT)
        qfrm2=Frame(frm2)
        qfrm2.pack(side=LEFT,expand=True)
        lbl5=Label(afrm2,text="Sender Name")
        lbl5.pack(anchor=NW)
        txt=Entry(qfrm2,textvariable=self.ms,width=30)
        txt.pack(anchor=NW)
        lbl5=Label(afrm2,text="Address Line")
        lbl5.pack(anchor=NW)
        txt=Entry(qfrm2,textvariable=self.msad1,width=30)
        txt.pack(anchor=NW)
        lbl5=Label(afrm2,text="Sender GSTIN no:")
        lbl5.pack(anchor=NW)
        txt=Entry(qfrm2,textvariable=self.pgst,width=30)
        txt.pack(anchor=NW)
        txt.bind("<FocusOut>",self.autoinsert)
        frm2.pack(side=LEFT,fill=BOTH,expand=True)
        #second frame end third start
        s1frm=Frame(afrm)
        s2frm=Frame(s1frm)
        frm3=Frame(s1frm)
        frm3.pack(fill=BOTH,expand=True)
        s2frm.pack(fill=BOTH,expand=True)
        lbl6=Label(frm3,text="Invoice no ").pack(side=LEFT)
        lbl6=Entry(frm3,textvariable=self.no).pack(side=LEFT)
        lbl7=Label(frm3,text="Date: ")
        entry=Entry(frm3,textvariable=self.date)
        entry.pack(side=RIGHT)
        Label(s1frm,text="e-Way Bill No.").pack(fill=BOTH,expand=True)
        Entry(s1frm,textvariable=self.eway).pack(side=RIGHT,anchor=NE)
        self.date.set(time.strftime("%d-%b-%Y"))
        lbl7.pack(side=RIGHT,anchor=N)
        s1frm.pack(side=RIGHT,expand=True,fill=BOTH)
        afrm.pack(fill=BOTH)
        #3rd end 4th start
        frm4=Frame(ffrm,bg="black")
        self.eevn=[]
        widt=[5,30,7,8,8,12,8,8,8,15]
        texts=["Sr No."," Description ","CESS","TCS/TDS","GST",
               " HSN No. ","Quantity"," Rate ","per Unit","Taxable Amount"]
        frm=Frame(frm4,borderwidth=1,bg="black")
        frm.pack(fill=BOTH,expand=True)
        for i in range(10):
            Label(frm,text=texts[i],width=widt[i]).pack(side=LEFT,fill=BOTH,expand=True)
        self.newrow(frm4)
        Button(frm4,text="New Row",command=lambda:self.newrow(frm4)).pack(side=BOTTOM,fill=BOTH,expand=True)
        frm4.pack(fill=BOTH)
        #4th frame end 5th start
        frm5=Frame(ffrm,borderwidth=1,bg="black")
        Label(frm5,text="Vehicle no").pack(side=LEFT,fill=BOTH,expand=True)
        Entry(frm5,textvariable=self.vno).pack(side=LEFT,fill=BOTH,expand=True)
        Label(frm5,text="Transporter/Vehicle Owner").pack(side=LEFT,fill=BOTH,expand=True)
        Entry(frm5,textvariable=self.owner).pack(side=LEFT,fill=BOTH,expand=True)
        frm5.pack(side=LEFT,fill=BOTH,expand=True)
        #5th end 6th start
        lfrm=Frame(ffrm,borderwidth=1,bg="black")
        rot=Frame(lfrm)
        rot.pack(expand=True,fill=BOTH)
        #6th end 7th start
        lfrm.pack(side=RIGHT,fill=BOTH,expand=True)
        self.chklbl=Label(self,text="Please Fill the Details")
        btn=Button(self,text="Reset",command=lambda:self.reset()).pack(expand=True)
        btn=Button(self,text="Generate Bill",command=lambda:self.check()).pack(expand=True)
        btn=Button(self,text="Back",command=lambda:self.show()).pack(expand=True,fill=X)
    def newrow(self,frm):
        var=[]
        for i in range(10):
            var.append(StringVar())
            if i==2 or i==3:
                var[-1].set('0')
        self.variable.append(var)
        i=-1
        width=[5,30,9,9,9,9,9,10,6,15]
        sfrm4=Frame(frm)
        sfrm4.pack(fill=BOTH,expand=True)
        Entry(sfrm4,textvariable=self.variable[i][0],width=width[0]).pack(side=LEFT,expand=True,fill=BOTH)
        Entry(sfrm4,textvariable=self.variable[i][1],width=width[1]).pack(side=LEFT,expand=True,fill=BOTH)
        Entry(sfrm4,textvariable=self.variable[i][2],width=width[2]).pack(side=LEFT,expand=True,fill=BOTH)
        Entry(sfrm4,textvariable=self.variable[i][3],width=width[3]).pack(side=LEFT,expand=True,fill=BOTH)
        Entry(sfrm4,textvariable=self.variable[i][4],width=width[4]).pack(side=LEFT,expand=True,fill=BOTH)
        Entry(sfrm4,textvariable=self.variable[i][5],width=width[5]).pack(side=LEFT,expand=True,fill=BOTH)
        text1=Entry(sfrm4,textvariable=self.variable[i][6],width=width[6])
        text1.pack(side=LEFT,expand=True,fill=BOTH)
        text2=Entry(sfrm4,textvariable=self.variable[i][7],width=width[7])
        text2.pack(side=LEFT,expand=True,fill=BOTH)
        Entry(sfrm4,textvariable=self.variable[i][8],width=width[8]).pack(side=LEFT,expand=True,fill=BOTH)
        text3=Entry(sfrm4,textvariable=self.variable[i][9],width=width[9])
        text3.pack(side=LEFT,expand=True,fill=BOTH)
        self.eevn.append([text1,text2,text3])
        try:
            text1.bind("<KeyRelease>",self.doshow)
            text2.bind("<KeyRelease>",self.doshow)
        except Exception as e:
            print(e)
    def check(self):
        try:
            xmlfile.createxml("C:/Users/"+os.getlogin()+"/Desktop/GST Data/sellerinvoice.xml","Seller",["Invoice_No","Seller_Name","Date"],[self.no.get(),self.ms.get().upper(),self.date.get()])
        except:
            print("Error in File")
        try:
            self.detail=[str(self.ms.get()).upper(),self.msad1.get().upper(),str(self.pgst.get()).upper()]
            self.billdetail=[self.no.get(),self.date.get(),self.eway.get(),self.vno.get(),self.owner.get()]
        except:
            print("Error in Data")
        self.data=[]
        self.gstt=[]
        if self.ms.get()=="":
            self.chklbl.pack(expand=True)
            return
        for i in self.variable:
            tcss=round(float(i[3].get())*float(i[9].get())/100,2)
            ces=round(float(i[2].get())*float(i[6].get()),2)
            daa=round(float(i[4].get())*float(i[9].get())/100,2)
            if self.pgst.get()[:2]!=merge.finduser(merge.init())[1][:2] and self.pgst.get()!='':
                self.gstt.append([0.0,0.0,daa,ces,tcss])
            else:
                self.gstt.append([daa/2,daa/2,0.0,ces,tcss])
            value=False
            for j in i:
                if j.get()!="":
                    value=True
                if j.get()==""  and value and j!=i[2] and j!=i[3]:
                    self.chklbl.pack(expand=True)
                    return
            if value:
                self.data.append([j.get() for j in i])
        self.chklbl.pack_forget()
        for i in self.gstt:
            for j in i:
                round(j,2)
        newworkbook.wordbook.insertdata(self.master,self)
    def autoinsert(self,event):
        try:
            file=open("C:/Users/"+os.getlogin()+"/Desktop/GST Data","r")
            for line in file:
                if self.pgst.get().upper()==line.split("~")[0]:
                    self.ms.set(line.split("~")[1])
            file.close()
        except:
            pass
    def show(self):
        self.master.title("Goods and Service Tax")
        self.master.geometry("500x500+100+100")
        self.sel.pack(fill=BOTH,expand=True)
        self.destroy()
    def reset(self):
        self.update()
        for i in self.variable:
            for j in i:
                j.set('')
    def doshow(self,event):
        for i in range(len(self.eevn)):
            s=self.eevn[i]
            if s[0]==event.widget or s[1]==event.widget:
                try:
                    s[2].delete(0,END)
                    s[2].insert(0,str(float(s[0].get())*float(s[1].get())))
                except:
                    pass
if __name__=="__main__":
    gener()
