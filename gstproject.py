from tkinter import *
from tkinter import filedialog
import newworkbook,csvdata,insertbill,coaldata,merge
class Dove(Frame):
    def __init__(self,root,sel):
        if sel!=None:
            sel.pack_forget()
        try:
            master=root.master
            master.geometry("500x500+100+100")
            master.title("Choose What you want to do")
        except:
            master=root
            master.geometry("500x500+100+100")
            master.title("Choose What you want to do")
        Frame.__init__(self,master)
        self.pack(expand=True,fill=BOTH,ipadx=10,ipady=10)
        mainframe=Frame(self,bg="yellow",pady=5)
        mainframe.pack(fill=BOTH,expand=True)
        frame=Frame(mainframe)
        self.frm1=frame
        self.mnfrm=mainframe
        frame.pack(fill=BOTH,expand=True)
        btn=Button(frame,text="Create a Bill",pady=5,font=("arial",15,"normal"),width=15,command=lambda:self.create(master))
        btn.pack(expand=True)
        btn=Button(frame,text="Insert Seller Data",pady=5,font=("arial",15,"normal"),width=15,command=lambda:insertbill.App(master,self))
        btn.pack(expand=True)   
        btn=Button(frame,text="Calculate GST",width=15,pady=5,font=("arial",15,"normal"),command=lambda:self.calgst())
        btn.pack(expand=True)
        btn=Button(frame,text="Arrange Data",width=15,pady=5,font=("arial",15,"normal"),command=lambda:self.arrngdata())
        btn.pack(expand=True)
        btn=Button(frame,text="Back",width=15,pady=5,font=("arial",15,"normal"),command=lambda:self.back(root))
        btn.pack(expand=True)
    def back(self,sel):
        sel.pack(fill=BOTH,expand=True,ipadx=10,ipady=10)
        self.pack_forget()
    def create(self,master):
        coaldata.App(master,self)
        '''self.frm1.pack_forget()
        frame2=Frame(self.mnfrm)
        frame2.pack(fill=BOTH,expand=True)
        self.frame2=frame2
        btn=Button(frame2,text="Create a Bill",pady=5,font=("arial",15,"normal"),width=15,command=lambda:test.App(master,self))
        btn.pack(expand=True)
        btn=Button(frame2,text="Bill For Coal",pady=5,font=("arial",15,"normal"),width=15,command=lambda:coaled.App(master,self))
        btn.pack(expand=True)
        btn1=Button(frame2,text="Back",width=15,pady=5,font=("arial",15,"normal"),command=lambda:self.forset(frame2))
        btn1.pack(side=BOTTOM,expand=True)'''
    def openabill(self):
        self.frm1.pack_forget()
        frame2=Frame(self.mnfrm)
        frame2.pack(fill=BOTH,expand=True)
        self.frame2=frame2
        btn1=Button(frame2,text="Back",width=15,pady=5,font=("arial",15,"normal"),command=lambda:self.forset(frame2))
        btn1.pack(side=BOTTOM,expand=True)
    def forset(self,frm):
        frm.pack_forget()
        self.frm1.pack(fill=BOTH,expand=True)
    def abill(self):
        try:
            filename=filedialog.askopenfilename(title="Select A File")
        except:
            filename=filedialog.askopenfilename(title="Select A File")
        if filename!="":
            return filename
        else:
            pass
    def insertdata(self):
        self.frm1.pack_forget()
        frame2=Frame(self.mnfrm)
        frame2.pack(fill=BOTH,expand=True)
        wo=csvdata.csvd()
        try:
            btn=Button(frame2,text="Create HSN File",width=15,pady=5,font=("arial",15,"normal"),command=lambda:wo.HSN(self.abill()))
            btn.pack(expand=True)
        except:
            pass
        btn1=Button(frame2,text="Back",width=15,pady=5,font=("arial",15,"normal"),command=lambda:self.forset(frame2))
        btn1.pack(side=BOTTOM,expand=True)
    def calgst(self):
        self.frm1.pack_forget()
        frame2=Frame(self.mnfrm)
        frame2.pack(fill=BOTH,expand=True)
        wb=newworkbook.wordbook()
        btn=Button(frame2,text="Calculate GST",width=15,pady=5,font=("arial",15,"normal"),command=lambda:wb.calgst(self.abill()))
        btn.pack(expand=True)
        btn1=Button(frame2,text="Back",width=15,pady=5,font=("arial",15,"normal"),command=lambda:self.forset(frame2))
        btn1.pack(side=BOTTOM,expand=True)
    def arrngdata(self):
        self.frm1.pack_forget()
        wb=newworkbook.wordbook()
        frame2=Frame(self.mnfrm)
        frame2.pack(fill=BOTH,expand=True)
        btn=Button(frame2,text="Arrange Data",width=15,pady=5,font=("arial",15,"normal"),command=lambda:wb.arngdata(merge.init()))
        btn.pack(expand=True)
        btn1=Button(frame2,text="Back",width=15,pady=5,font=("arial",15,"normal"),command=lambda:self.forset(frame2))
        btn1.pack(side=BOTTOM,expand=True)
if __name__=="__main__":
    root=Tk()
    me=Dove(root,None)
    root.title("Goods and Service Tax")
    root.mainloop()
