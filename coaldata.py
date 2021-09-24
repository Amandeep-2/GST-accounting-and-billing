from tkinter import *
import time,os,xmlfile
import bill,merge
''' This File creates Bill and takes data from owner
This file calls bill file.'''
def gener():
    root=Tk()
    btn=App(root,None)
    root.title("GST Bill Format")
    root.mainloop()
class App(Frame):
    def __init__(self,master,sel):
        self.master=master
        print(master)
        master.title("GST Bill")
        master.geometry("875x500+50+60")
        self.n=0
        self.gst=[]
        self.sel=sel
        if sel!=None:
            sel.pack_forget()
        Frame.__init__(self,master)
        self.pack(fill=BOTH,expand=True)
        self.dirr=merge.path+merge.init()+"/"
        print(self.dirr)
        if os.path.exists(self.dirr):
            pass
        else:
            os.makedirs(self.dirr)
        '''try:
            file=open(self.dirr+"billno.txt","r")
            for line in file:
                if line !="\n":
                    self.n=int(line.rsplit()[0])+1
            file.close()
        except Exception as er:
            print("Error in 36 "+str(er))'''
        try:
            self.n=int(xmlfile.readxml(self.dirr+"InvoiceDetail.xml","id"))+1                     
        except Exception as er:
            print("File cannot be read "+str(er))
        self.rev=["N","Y"]
        self.no=StringVar()
        self.no.set(str(self.n))
        self.pgst=StringVar()
        self.ms=StringVar()
        self.msad1,self.msad2=StringVar(),StringVar()
        self.amount=StringVar()
        self.ppno=StringVar()
        self.date,self.ewayno=StringVar(),StringVar()
        self.vno,self.chlnno=StringVar(),StringVar()
        self.rchrg,self.lrno=IntVar(),StringVar()
        self.tname=StringVar()
        self.variable=[]
        # First frame start
        ffrm=Frame(self,borderwidth=1)
        ffrm.pack(ipadx=2,ipady=2,padx=10,pady=10,expand=True)
        sfrm=Frame(ffrm)
        frm=Frame(sfrm)
        frm.pack(fill=BOTH)
        gstno="00AAAAA0000A0AA"
        mobno="99119XXXXX"
        compname="AAAA BBBB CCCC"
        compadd="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        try:
            name=merge.init()
            data=merge.finduser(name)
            for i in data:
                if i==None:
                    i="Not Avilable";
            self.gstno="GST No. "+data[0]
            try:
                mobno="Mob. "+data[2]
            except:
                print("Error in mob no")
            compname=data[1]
            compadd=data[3]+data[4]
            '''
            fill=open(self.dirr+"Users.txt","r")
            data=fill.read()
            fill.close()
            self.gstno="GST NO. "+data.split('~')[0].upper()
            mobno="Mob. "+data.split('~')[2].upper()
            compname=data.split('~')[1].upper()
            compadd=data.split('~')[3].upper()'''
        except Exception as ent:
            print(ent,"Error in 77")
        gstno=self.gstno
        Label(frm,text=gstno).pack(side=LEFT)
        Label(frm,text="Tax Invoice").pack(side=LEFT,expand=True,fill=BOTH)
        lbl2=Label(frm,text=mobno)
        lbl2.pack(side=RIGHT)
        lbl3=Label(sfrm,text=compname,font=("arial",24,"bold"))
        lbl3.pack(fill=BOTH)
        lbl4=Label(sfrm,text=compadd,font=("arial",16,"bold"))
        lbl4.pack(fill=BOTH)
        sfrm.pack(fill=BOTH)
        # First Frame end Second start
        afrm=Frame(ffrm,borderwidth=1,bg="black")
        frm2=Frame(afrm)
        afrm2=Frame(frm2)
        afrm2.pack(expand=True,side=LEFT)
        qfrm2=Frame(frm2)
        qfrm2.pack(side=LEFT,expand=True)
        Label(afrm2,text="Party GSTIN no:").pack(anchor=NW)
        #txt=Entry(qfrm2,textvariable=self.pgst)
        #txt.pack(anchor=NW,pady=1)
        self.autoinsertgst(qfrm2)
        Label(afrm2,text="M/s          ").pack(anchor=NW)
        Entry(qfrm2,textvariable=self.ms,width=30).pack(anchor=NW,pady=1)
        Label(afrm2,text="Address Line 1").pack(anchor=NW)
        Entry(qfrm2,textvariable=self.msad1,width=30).pack(anchor=NW,pady=1)
        Label(afrm2,text="Address Line 2").pack(anchor=NW)
        Entry(qfrm2,textvariable=self.msad2,width=30).pack(anchor=NW,pady=1)
        Label(afrm2,text="Eway Bill No.").pack(anchor=NW)        
        Entry(qfrm2,textvariable=self.ewayno,width=30).pack(anchor=NW,pady=2)
        #txt.bind("<FocusOut>",self.autoinsert)
        frm2.pack(side=LEFT,fill=BOTH,expand=True)
        #second frame end third start
        s1frm=Frame(afrm)
        s2frm=Frame(s1frm)
        frm3=Frame(afrm)
        frm=Frame(s2frm)
        frm.pack(pady=2)
        frm3.pack(side="left",fill=BOTH,expand=True)
        s2frm.pack(side="right",fill=BOTH,expand=True)
        Label(frm3,text="Invoice no ").pack(pady=3)
        Label(frm,textvariable=self.no).pack(side=LEFT,padx=5,pady=2)
        btn=Button(frm,text="+",width=2,command=lambda:self.inr()).pack(side=LEFT,pady=2,padx=5)
        btn=Button(frm,text="-",width=2,command=lambda:self.dcr()).pack(padx=5,pady=2)
        Label(frm3,text="Date:").pack(pady=3)
        entry=Entry(s2frm,textvariable=self.date)
        entry.pack(pady=2)
        self.date.set(time.strftime("%d-%b-%Y"))
        lbl8=Label(frm3,text="Challan No.")
        lbl8.pack(pady=3)
        entry1=Entry(s2frm,textvariable=self.chlnno)
        entry1.pack(padx=5,pady=2)
        lbl9=Label(frm3,text="Party P.O. No.:")
        lbl9.pack(pady=3)
        entry2=Entry(s2frm,textvariable=self.ppno)
        entry2.pack(padx=5,pady=2)
        s1frm.pack(side=RIGHT,expand=True,fill=BOTH)
        afrm.pack(fill=BOTH)
        #3rd end 4th start
        frm4=Frame(ffrm,bg="black")
        depfrm=Frame(frm4)
        depfrm.pack(fill=BOTH)
        self.eevn=[]
        widt=[5,25,8,12,8,15,8,10,8,15]
        texts=["Sr No.","Description","CESS","TCS/TDS","GST RATE","HSN No",
               " Quantity "," Rate "," per ","Taxable Amount"]
        for i in range(10):
            Label(depfrm,text=texts[i],width=widt[i]).pack(side=LEFT,fill=BOTH,expand=True)
        frm4.pack(fill=BOTH)
        self.drawlabel(frm4)
        btn=Button(frm4,text="NEW Data Row",bg="Blue",command=lambda:self.drawlabel(frm4))
        btn.pack(side=BOTTOM,anchor=SE,expand=True,fill=BOTH)
        #5th end 6th start
        lfrm=Frame(ffrm,borderwidth=1)
        rot=Frame(lfrm)
        rot.pack(expand=True)
        frm6=Frame(rot)
        frm6.pack(fill=BOTH,expand=True)
        Label(frm6,text="Vehicle No.").pack(expand=True,padx=3,side=LEFT)
        Label(frm6,text="Reverse Charge").pack(expand=True,padx=3,side=LEFT)
        Label(frm6,text="Transporter Detail").pack(expand=True,side=LEFT)
        Label(frm6,text="Transport Document No.").pack(expand=True,side=LEFT)
        frmd=Frame(rot)
        frmd.pack(fill=BOTH,expand=True)
        Entry(frmd,textvariable=self.vno,width=12).pack(expand=True,pady=1,padx=7,side=LEFT)
        Checkbutton(frmd,variable=self.rchrg,width=12).pack(expand=True,pady=1,padx=7,side=LEFT)
        Entry(frmd,textvariable=self.tname).pack(expand=True,pady=1,padx=5,side=LEFT)
        Entry(frmd,textvariable=self.lrno).pack(expand=True,pady=1,padx=5,side=LEFT)
        lfrm.pack(fill=BOTH,expand=True)
        self.chklbl=Label(self,text="Please Fill the Details")
        btn=Button(self,text="Reset",command=lambda:self.reset()).pack(expand=True)
        btn=Button(self,text="Generate Bill",command=lambda:self.check()).pack(expand=True)
        btn=Button(self,text="Back",command=lambda:self.show()).pack(expand=True)
    def drawlabel(self,frm):
        a=[]
        width=[5,25,8,8,8,15,8,10,8,12]
        for j in range(10):
            var=StringVar()
            a.append(var)
        a[2].set('0')
        a[3].set('0')
        sfrm4=Frame(frm,borderwidth=1,bg="black")
        sfrm4.pack(fill=BOTH,expand=True)
        Entry(sfrm4,textvariable=a[0],width=width[0]).pack(padx=1,side=LEFT,expand=True,fill=BOTH)
        Entry(sfrm4,textvariable=a[1],width=width[1]).pack(padx=1,side=LEFT,expand=True,fill=BOTH)
        Entry(sfrm4,textvariable=a[2],width=width[2]).pack(padx=1,side=LEFT,expand=True,fill=BOTH)
        Entry(sfrm4,textvariable=a[3],width=width[3]).pack(padx=1,side=LEFT,expand=True,fill=BOTH)
        Entry(sfrm4,textvariable=a[4],width=width[4]).pack(padx=1,side=LEFT,expand=True,fill=BOTH)
        Entry(sfrm4,textvariable=a[5],width=width[5]).pack(padx=1,side=LEFT,expand=True,fill=BOTH)
        text1=Entry(sfrm4,textvariable=a[6],width=width[6])
        text1.pack(padx=1,side=LEFT,expand=True,fill=BOTH)
        text2=Entry(sfrm4,textvariable=a[7],width=width[7])
        text2.pack(padx=1,side=LEFT,expand=True,fill=BOTH)
        Entry(sfrm4,textvariable=a[8],width=width[8]).pack(padx=1,side=LEFT,expand=True,fill=BOTH)
        text3=Entry(sfrm4,textvariable=a[9],width=width[9])
        text3.pack(padx=1,side=LEFT,expand=True,fill=BOTH)
        self.eevn.append([text1,text2,text3])
        try:
            text2.bind("<KeyRelease>",self.doshow)
            text1.bind("<KeyRelease>",self.doshow)
        except Exception as e:
            print(str(e)," 199 line")
        self.variable.append(a)
    def check(self):
        if self.ms.get()=="":
            self.chklbl.pack(expand=True)
            return
        self.detail=[self.ms.get().upper(),self.msad1.get().upper(),self.msad2.get().upper()
                     ,self.ppno.get().title(),self.pgst.get().upper()]
        self.billdetail=[self.no.get(),self.date.get(),self.chlnno.get(),self.ewayno.get().upper()
                  ,self.vno.get().upper(),self.rev[self.rchrg.get()],self.tname.get().title(),self.lrno.get().title()]
        self.gst=[]
        self.data=[]
        f=False
        try:
            if merge.findclient(self.ms.get()) is None:
                print("coaldata file :- adding client")
                merge.addclient([self.pgst.get().upper(),self.ms.get().upper(),self.msad1.get().title(),self.msad2.get().title(),self.ppno.get().title()])
            else:
                print("coaldata file :- ",merge.findclient(self.ms.get()))
        except Exception as ee:
            print(ee,"Error in 224")
        for i in self.variable:
            print(self.pgst.get(),self.gstno)
            if self.pgst.get()[:2]!=self.gstno[8:10] and self.pgst.get()!='':
                self.gst.append([0.0,0.0,float(i[4].get()),float(i[2].get()),float(i[3].get())])
            else:
                self.gst.append([float(i[4].get())/2,float(i[4].get())/2,0.0,float(i[2].get()),float(i[3].get())])
            value=False
            for j in i:
                if j.get()!="":
                    value=True
                if j.get()==""  and value and j!=i[2] and j!=i[2]:
                    self.chklbl.pack(expand=True)
                    return
            if value:
                self.data.append([j.get() for j in i])
        self.chklbl.pack_forget()
        if 'gst.css' in os.walk(self.dirr):
            pass
        else:
            file=open(self.dirr+"gst.css","w+")
            file.write("""table,tr,td{
            border:1px solid black;
            border-collapse:collapse;
            vertical-align:top;
            border-bottom:none;
            }
            .first tr
            {
            height:35px;
            }
            .noborder,.noborder tr,.noborder tr td{
            border:none;
            border-collapse:collapse;
            }
            .nobordertd,.nobordertd tr,.nobordertd td, .nobordertd tr td
            {
            border-top:none;
            border-bottom:none;
            border-collapse:collapse;
            }
            .noborder tr td{
            vertical-align:top;
            }
            .noborder tr{height:100%;}
            p{
            margin:0px;
            }
            #firstrow{
            text-align:center;
            border:1px solid black;
            }
            body
            {
            margin-left:25px;
            margin-right:25px;
            font-family:"Arial";
            font-size:16px;
            font-weight:normal;
            }""")
            file.close()
        self.mscheck1()
        bill.create(self.master,self)
        #print(self.gst,"\nData\n",self.data,"\nDetail\n",self.detail)
    def show(self):
        self.master.title("Goods and Service detail")
        #self.master.geometry("500x500+100+100")
        self.sel.pack(fill=BOTH,expand=True)
        self.destroy()
    def inr(self):
        self.n=self.n+1
        self.no.set(self.n)
        self.update()
    def dcr(self):
        self.n=self.n-1
        self.no.set(self.n)
        self.update()
    def autoinsert(self,event):
        if self.pgst.get()!='':
            try:
                file=open(self.dirr+"pgstms.txt","r")
            except:
                return
            for line in file:
                if self.pgst.get().upper()==line.split("~")[0]:
                    self.ms.set(line.split("~")[1])
                    self.msad1.set(line.split("~")[2])
                    self.msad2.set(line.split("~")[3])
                    self.ppno.set(line.split("~")[4])
            file.close()
        else:
            pass
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
                    s[2].insert(0,str(round(float(s[0].get())*float(s[1].get()),2)))
                except:
                    print("Error in 327")
    def autoinsertgst(self,fs):
        findd=StringVar()
        fr=Frame(fs)
        fr.pack()
        data=merge.allclient()
        if data is None:
            data=["None"]
        vall=StringVar()
        findd.set("Select A Client")
        nam=OptionMenu(fr,findd,*data,command=self.selection)
        nam.pack(side=LEFT)
        self.gststore=Entry(fr,textvariable=self.pgst,width=30)
        self.gststore.bind("<FocusOut>",self.mscheck)
        ls=[nam,self.gststore]
        if data==[]:
            ls.insert(0,nam)
            merge.do(ls)
        bt=Button(fr,text="+",command=lambda:self.newgstin(ls))
        bt.pack(side=RIGHT)
        ls.insert(0,bt)
    def mscheck(self,event):
        try:
            if len(self.pgst.get())!=15 or not str(self.pgst.get()[:2]).isdecimal() or not str(self.pgst.get()[2:7]).isalpha():
                messagebox.showinfo("Information","GSTIN is invalid please check,Length Should be 15 and First Two Character Must be digit")
                self.gststore.focus()
                return
            elif int(self.pgst.get()[:2])>38 or self.pgst.get().upper()[13]!="Z" or not self.pgst.get()[7:11].isdecimal():
                messagebox.showinfo("Invalid GSTIN","GSTIN is invalid please check,Length Should be 15 and First Two Character Must be digit")
                self.gststore.focus()
                return
        except Exception as er:
            print("Coaldata file:-",str(er))
    def mscheck1(self):
        try:
            if len(self.pgst.get())!=15 or not str(self.pgst.get()[:2]).isdecimal():
                #messagebox.showinfo("Information","Please write valid GSTIN No")
                self.gststore.focus()
                return
            elif int(self.pgst.get()[:2])>38 or self.pgst.get().upper()[13]!="Z" or not self.pgst.get()[7:11].isdecimal():
                messagebox.showinfo("Invalid GSTIN","GSTIN is invalid please check,Lenth Should be 15 and First Two Character Must be digit")
                self.gststore.focus()
                return
        except Exception as er:
            print("Coaldata file:-",str(er))
    def selection(self,value):
        lst=merge.findclient(value)
        if lst==[]:
            return
        self.pgst.set(lst[0])
        self.ms.set(lst[1])
        self.msad1.set(lst[2])
        self.msad2.set(lst[3])
        self.ppno.set(lst[4])
    def newgstin(self,ls):
        self.pgst.set('')
        self.ms.set('')
        self.msad1.set('')
        self.msad2.set('')
        self.ppno.set('')
        merge.do(ls)
if __name__=="__main__":
    gener()
