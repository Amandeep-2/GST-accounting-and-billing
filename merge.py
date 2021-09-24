'''
<User id="3"><GSTIN>24AAFCV6687A1Z9</GSTIN><User_Name>VASUKI TRADE LINK PVT. LTD.</User_Name><Mobile_No>9925422288</Mobile_No><Address_Line_1>501-Fifth Floor, Nakshtra Heights, Opp. Raiya Telephone Exchange</Address_Line_1><Address_Line_2>150 ft Ring Road, Rajkot, Gujarat</Address_Line_2><Bank_Name>THE KARUR VYSYA BANK LTD.</Bank_Name><Account_No>2203280000001711</Account_No><IFSC_Code>KVBL0002203</IFSC_Code><Branch_Name>DR. YAGNIK ROAD, RAJKOT</Branch_Name></User>
<User id="2"><GSTIN>24AARCA7840C1ZP</GSTIN><User_Name>AAGAM MINERALS PRIVATE LIMITED</User_Name><Mobile_No> aagam.commotrade@gmail.com</Mobile_No><Address_Line_1>2ND FLOOR, OFFICE NO. 213, KUTCH ARCADE PLATINUM, MITHI ROHAR,</Address_Line_1><Address_Line_2> SURVEY NO 234/1 AND235, GANDHIDHAM, Kachchh, Gujarat, 370201</Address_Line_2><Bank_Name /><Account_No /><IFSC_Code /><Branch_Name /></User>
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
def main():
    lis=[]
    p=int(input("Enter Array Size"))
    for i in range(p):
        lis.append(int(input()))
    mergeSort(lis)
    print("merge file :- "+"Sorted list:- ",lis)
main()

'''
from tkinter import *
from tkinter import messagebox
import os,gstproject,datetime,time
import xml.etree.ElementTree as et
path="C:/Users/"+os.getlogin()+"/Desktop/GST Data/"
USER_NAME=''
def init():
    global path
    global USER_NAME
    path="C:/Users/"+os.getlogin()+"/Desktop/GST Data/"
    try:
        USER_NAME=open(path+"temp.sys","r").read()
        return USER_NAME
    except:
        USER_NAME=''
        return USER_NAME
def addclient(lst):
    if findclient(lst[1])!=None:
        return messagebox.showinfo("Client Info","Client Already Exist Restart Software")
    global path
    global USER_NAME
    #print("merge file :- "+"In client ",path,USER_NAME)
    path=path+USER_NAME+"/"
    #print("merge file :- "+path)
    fname="Clients.xml"
    if fname not in os.listdir(path):
        #print("merge file :- "+"File not Exist")
        file=open(path+fname,"w+")
        data=et.Element("Data")
        data.set("id","0")
        file.write(et.tostring(data).decode("ascii"))
        file.close()
    #print(path)
    file=et.parse(path+fname)
    data=file.getroot()
    no=int(data.attrib['id'])+1
    data.attrib["id"]=str(no)
    cl=et.Element("Client")
    gst=et.SubElement(cl,"GSTIN")
    cn=et.SubElement(cl,"Client_Name")
    cad1=et.SubElement(cl,"Address_line_1")
    cad2=et.SubElement(cl,"Address_line_2")
    pos=et.SubElement(cl,"Place_of_supply")
    cl.set("id",str(no))
    gst.text=lst[0]
    cn.text=lst[1]
    cad1.text=lst[2]
    cad2.text=lst[3]
    pos.text=lst[4]
    data.append(cl)
    file.write(path+fname)
    fnam="Client.xml"
    if fnam not in os.listdir(path):
        #print("merge file :- ",path,"File not exist")
        file=open(path+fnam,"w+")
        data=et.Element("Data")
        data.set("id","1")
        file.write(et.tostring(data).decode("ascii"))
        file.close()
    file=et.parse(path+fnam)
    data=file.getroot()
    data.attrib["id"]=str(no+1)
    cl=et.Element("Client_Name")
    cl.set("id",str(no))
    cl.text=lst[1]
    data.append(cl)
    file.write(path+fnam)
    messagebox.showinfo("Client Info","Client Info has been Stored")
def adduser(lst):
    if finduser(lst[1])!=None:
        return messagebox.showinfo("User Info","User Already Exist Restart Software")
    messagebox.showinfo("User Limit","Maximum of Two Users Can be added")
    init()
    path="C:/Users/"+os.getlogin()+"/Desktop/GST Data/"
    fname="Users.xml"
    if fname not in os.listdir(path):
        print("merge file :- "+"File not Exist")
        file=open(path+fname,"w+")
        data=et.Element("Data")
        data.set("id","0")
        file.write(et.tostring(data).decode("ascii"))
        file.close()
    file=et.parse(path+fname)
    data=file.getroot()
    no=int(data.attrib['id'])
    if no is 2:
        messagebox.showinfo("Error","Users Limit Reached. Maximum of 2 Users Can be added")
        return
    data.attrib["id"]=str(no+1)
    cl=et.Element("User")
    cl.set("Day",time.strftime("%d"))
    cl.set("Month",time.strftime("%m"))
    cl.set("Year",time.strftime("%Y"))
    gst=et.SubElement(cl,"GSTIN")
    cn=et.SubElement(cl,"User_Name")
    mb=et.SubElement(cl,"Mobile_No")
    cad1=et.SubElement(cl,"Address_Line_1")
    cad2=et.SubElement(cl,"Address_Line_2")
    bn=et.SubElement(cl,"Bank_Name")
    an=et.SubElement(cl,"Account_No")
    ifc=et.SubElement(cl,"IFSC_Code")
    brn=et.SubElement(cl,"Branch_Name")
    cl.set("id",str(no))
    try:
        gst.text=lst[0]
        print("merge file :- "+gst.text+"\n")
    except:
        print("merge file :- "+"returning")
        return ;
    try:
        cn.text=lst[1]
        print("merge file :- "+cn.text+"\n")
    except:
        cn.text=''
        print("merge file :- "+"User Name is empty")
    try:
        mb.text=lst[2]
        print("merge file :- "+mb.text+"\n")
    except:
        mb.text=''
        print("merge file :- "+"Mobile No is empty")
    try:
        cad1.text=lst[3]
    except:
        cad1.text=''
        print("merge file :- "+"Address Line 1 is Empty")
    try:
        cad2.text=lst[4]
    except:
        cad2.text=''
        print("merge file :- "+"Address Line 2 is Empty")
    try:
        bn.text=lst[5]
    except:
        bn.text=''
        print("merge file :- "+"Bank Name is Empty")
    try:
        an.text=lst[6]
    except:
        an.text=''
        print("merge file :- "+"Account No is Empty")
    try:
        ifc.text=lst[7]
    except:
        ifc.text=''
        print("merge file :- "+"IFSC Code is Empty")
    try:
        brn.text=lst[8]
    except:
        brn.text=''
        print("merge file :- "+"Branch Name is Empty")
    data.append(cl)
    os.makedirs(path+lst[1])
    #print("merge file :- "+et.tostring(cl))
    #print("merge file :- "+et.tostring(data))
    file.write(path+fname)
    messagebox.showinfo("User info","User info Has been Stored")
def findclient(text):
    init()
    try:
        file=et.parse(path+init()+"/Clients.xml")
    except:
        return None
    root=file.getroot()
    for i in root:
        if i[1].text in text:
            return [i[j].text for j in range(len(i))]
    return None
def removeclient(text):
    init()
    file=et.parse(path+init()+"/Clients.xml")
    root=file.getroot()
    for i in root:
        if i[1].text==text:
            root.remove(i)
            file.write(path+init()+"/Clients.xml")
            break
    file=et.parse(path+init()+"/Client.xml")
    root=file.getroot()
    no=int(root.attrib["id"])
    for i in root:
        if i[0].text==text:
            root.attrib['id']=str(no-1)
            file.write(path+init()+"/Client.xml")
            messagebox.showinfo("Client removed",text+" has been removed")
            break
def removeuser(text):
    init()
    file=et.parse(path+"/Users.xml")
    root=file.getroot()
    no=int(root.attrib["id"])
    for i in root:
        try:
            print(i.attrib["Day"])
        except:
            continue
        day=int(i.attrib["Day"])
        month=int(i.attrib["Month"])
        year=int(i.attrib["Year"])
        dif=abs(datetime.date(year,month,day)-datetime.date.today()).days
        if i[1].text==text and dif > 365:
            root.remove(i)
            root.attrib["id"]=str(no-1)
            file.write(path+"/Users.xml")
            messagebox.showinfo("User Removed",text+" Has been removed")
            return
        else:
            messagebox.showinfo("Information","User cannot be removed")
def allclient():
    init()
    try:
        file=et.parse(path+init()+"/Client.xml")
    except:
        return None          
    root=file.getroot()
    return [j.text for j in root]
def alluser():
    init()
    file=et.parse(path+"/Users.xml")
    root=file.getroot()
    return [j[1].text for j in root]
def finduser(user):
    init()
    if user=="Test":
        print("merge file :- "+user)
        lst=["00AAAAA0000A0AA","XYZ Company","00000000","No Location ","Required","UnknownBank","000","UnknownIFSC","Space"]
        return lst
    path="C:/Users/"+os.getlogin()+"/Desktop/GST Data/"
    try:
        file=et.parse(path+"Users.xml")
    except:
        return None
    root=file.getroot()
    for i in root:
        if i[1].text in user:
            return [i[j].text for j in range(len(i))]
    return None
def selection(e):
    init()
    nam=e.widget
    a=nam.curselection()
    for i in a:
        print(findclient(nam.get(i)))
def do(ls):
    ls[0].pack_forget()
    ls[1].pack_forget()
    ls[-1].pack()
def drawgstin(fr):
    findd=StringVar()
    nam=Listbox(fr,height=1,width=20)
    sc=Scrollbar(fr,command=nam.yview,width=20)
    en=Entry(fr,textvariable=findd)
    ls=[nam,sc,en]
    Button(fr,text="+",command=lambda:do(ls)).pack(side=RIGHT)
    data=allclient()
    for i in range(len(data)):
        nam.insert(i+1,data[i])
    nam.pack(side=LEFT)
    nam.configure(yscrollcommand=sc.set)
    sc.pack(side=RIGHT,fill=Y)
    nam.bind("<ButtonRelease-1>",selection)
def setusername(name,root):
    #print("merge file :- "+e.widget,e.master)
    init()
    open(path+"temp.sys","w+").write(name)
    root.master.pack_forget()
    gstproject.Dove(root.master,None)
def drawuserselect(frm):
    frm.master.geometry("500x500+100+100")
    frm.pack(expand=True,fill=BOTH)
    frm.master.title("Choose User")
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)
    if "Users.xml" in os.listdir(path):
        pass
    else:
        file=open(path+"Users.xml","w+")
        data=et.Element("Data")
        data.set("id","0")
        file.write(et.tostring(data).decode("ascii"))
        file.close()
    thi=Frame(frm)
    thi.pack(fill=BOTH,expand=True,ipadx=10,ipady=10)
    no=IntVar()
    no.set(0)
    lst=[]
    try:
        lst=alluser()
    except:
        print("merge file :- "+"Error no user detail")
    s=Button(thi,text="Test Software",pady=5,font=("Arial","16","normal"),command=lambda:setusername("Test",thi))
    s.pack(fill=X,expand=True)
    for i in lst:
        s=Button(thi,text=i,pady=5,font=("Arial","16","normal"),command=lambda i=i:(setusername(i,thi),print("merge file :- "+"Hello")))
        s.pack(fill=X,expand=True)
    Button(thi,text="New User",pady=5,font=("Arial","16","normal"),command=lambda:insertuser(frm,thi)).pack(fill=X,expand=True)
    Button(thi,text="Edit User",pady=5,font=("Arial","16","normal"),command=lambda:edituser(frm,thi)).pack(fill=X,expand=True)
    Button(thi,text="Delete User",pady=5,font=("Arial","16","normal"),command=lambda:deletuser(frm,thi)).pack(fill=X,expand=True)
def insertuser(frm1,thi):
    thi.pack_forget()
    frm=Frame(frm1)
    frm1.master.geometry("500x550+100+100")
    gstin,username,mobno=StringVar(),StringVar(),StringVar()
    userad1,userad2=StringVar(),StringVar()
    bname,bano,ifsc,branch=StringVar(),StringVar(),StringVar(),StringVar()
    frm.pack(fill=Y,expand=True)
    Label(frm,text="GSTIN",font=("Arial","16","normal"),borderwidth=1).grid(row=0,column=1,sticky=N,pady=10)
    Entry(frm,textvariable=gstin,font=("Arial","16","normal")).grid(row=0,column=2,sticky=N,pady=10,padx=5)
    Label(frm,text="Company Name",font=("Arial","16","normal")).grid(row=2,column=1,sticky=N,pady=10)
    Entry(frm,textvariable=username,font=("Arial","16","normal")).grid(row=2,column=2,sticky=N,pady=10,padx=5)
    Label(frm,text="Mobile No",font=("Arial","16","normal")).grid(row=3,column=1,sticky=N,pady=10)
    Entry(frm,textvariable=mobno,font=("Arial","16","normal")).grid(row=3,column=2,sticky=N,pady=10,padx=5)
    Label(frm,text="Address line 1",font=("Arial","16","normal")).grid(row=4,column=1,sticky=N,pady=10)
    Entry(frm,textvariable=userad1,font=("Arial","16","normal")).grid(row=4,column=2,sticky=N,pady=10,padx=5)
    Label(frm,text="Address line 2",font=("Arial","16","normal")).grid(row=5,column=1,sticky=N,pady=10)
    Entry(frm,textvariable=userad2,font=("Arial","16","normal")).grid(row=5,column=2,sticky=N,pady=10,padx=5)
    Label(frm,text="Bank Name",font=("Arial","16","normal")).grid(row=6,column=1,sticky=N,pady=10)
    Entry(frm,textvariable=bname,font=("Arial","16","normal")).grid(row=6,column=2,sticky=N,pady=10,padx=5)
    Label(frm,text="Account No",font=("Arial","16","normal")).grid(row=7,column=1,sticky=N,pady=10)
    Entry(frm,textvariable=bano,font=("Arial","16","normal")).grid(row=7,column=2,sticky=N,pady=10,padx=5)
    Label(frm,text="IFSC Code",font=("Arial","16","normal")).grid(row=8,column=1,sticky=N,pady=10)
    Entry(frm,textvariable=ifsc,font=("Arial","16","normal")).grid(row=8,column=2,sticky=N,pady=10,padx=5)
    Label(frm,text="Branch Name",font=("Arial","16","normal")).grid(row=9,column=1,sticky=N,pady=10)
    Entry(frm,textvariable=branch,font=("Arial","16","normal")).grid(row=9,column=2,sticky=N,pady=10,padx=5)
    Button(frm,text="Insert",font=("Arial","16","normal"),command=lambda:adduser([gstin.get().upper(),username.get().upper(),mobno.get(),userad1.get(),userad2.get(),bname.get().upper(),bano.get(),ifsc.get().upper(),branch.get()])).grid(columnspan=3)
    Button(frm,text="Back",font=("Arial","16","normal"),command=lambda:do([frm,frm,thi])).grid(columnspan=3)
def deletuser(frm1,thi):
    thi.pack_forget()
    frm=Frame(frm1)
    frm1.master.geometry("500x550+100+100")
    frm.pack(fill=BOTH,expand=True)
    username=StringVar();
    Label(frm,text="Choose User to Delete").grid(row=0,column=0)
    OptionMenu(frm,username,*alluser()).grid(row=0,column=1)
    Button(frm,text="Delete",command=lambda username=username:removeuser(username.get())).grid(row=1,column=1,sticky=NSEW)
    Button(frm,text="Back",command=lambda:do([frm,frm,thi])).grid(row=2,column=1,sticky=NSEW)
def upda(frm,lsttbl,alllst,user):
    perform(frm,lsttbl,alllst,user)
    print("merge file :- "+"Hello")
    frm.update();
def edituserdata(user,detail,store):
    file=et.parse(path+"Users.xml")
    root=file.getroot()
    detaillst={"GSTIN":0,"User_Name":1,"Mobile_No":2,"Address_Line_1":3,"Address_Line_2":4,"Bank_Name":5,"Account_No":6,"IFSC_Code":7,"Branch_Name":8}
    for i in root:
        if i[1].text in user.get():
            i[detaillst[detail.get()]].text=store.get()
    file.write(path+"Users.xml")
def edituser(frm1,thi):
    thi.pack_forget()
    frm=Frame(frm1)
    user,detail,store=StringVar(),StringVar(),StringVar()
    frm1.master.geometry("500x550+100+100")
    frm.pack(expand=True,fill=BOTH)
    user.set("Select User")
    detail.set("Select Info")
    lst=alluser()
    alllst={i:finduser(i) for i in lst}
    lsttbl=["Mobile_No","Address_Line_1","Address_Line_2","Bank_Name","Account_N0","IFSC_Code","Branch_Name"]
    Label(frm,text="Editing User Info",font=("Arial","16","bold")).grid(row=0,sticky=N)
    Label(frm,text="Select User and Detail").grid(row=1,column=0)
    OptionMenu(frm,user,*lst).grid(row=1,column=1)
    OptionMenu(frm,detail,*lsttbl).grid(row=2,column=1,sticky=EW)
    Entry(frm,textvariable=store).grid(row=3,column=1,sticky=EW)
    Button(frm,text="Change Info",command=lambda user=user,detail=detail : edituserdata(user,detail,store)).grid(row=4,column=1)
    frmdata=Frame(frm1)
    lsttbl=["GSTIN","User Name"]+lsttbl
    frmdata.pack(expand=True,fill=BOTH)
    for i in range(len(lsttbl)):
        Label(frmdata,text=lsttbl[i],borderwidth=2,fg="black").grid(row=i+1,column=0)
    for i in alllst:
        Label(frmdata,text=i,width=20,borderwidth=2).grid(row=0,column=lst.index(i)+1)
        for j in range(9):
            Label(frmdata,text=alllst[i][j],width=20,borderwidth=1).grid(row=j+1,column=lst.index(i)+1)
    Button(frmdata,text="Back",command=lambda :do([frm,frmdata,thi])).grid()
if __name__=="__main__":
    root=Tk()
    root.title("Choose User")
    frm=Frame(root)
    frm.pack(expand=True,fill=BOTH)
    drawuserselect(frm)
    root.mainloop()
    try:
        os.remove(path+"temp.sys")
    except:
        print("merge file :- "+"File Not found")
