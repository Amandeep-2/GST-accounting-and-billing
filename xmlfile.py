import os,webbrowser,tkinter
import  xml.etree.ElementTree as et
def createxml(filepath,stag="Element",atag=[],datatag=[],idd=None,val=None):
    '''
    This method creates xml file with stag as Starting tag, atag as all sub tag,
    datatag contains data for stag if atag is empty or data for atag'''
    name=filepath
    for i in range(len(datatag)):
        datatag[i]=str(datatag[i])
    if not os.path.exists(name):
        print("File not Exist")
        file=open(name,"w+")
        data=et.Element("Data")
        #data.set("id","1")
        file.write(et.tostring(data).decode("ascii"))
        file.close()
    file=et.parse(name)
    data=file.getroot()
    try:
        if idd is not None:
            data.set(idd,val)
    except:
        print("No attribute exist")
    #no=int(data.attrib['id'])
    #data.attrib["id"]=str(no+1)
    cl=et.SubElement(data,stag)
    #cl.set("id",str(no))
    print(datatag[0],name)
    if len(atag)==0:
        cl.text=datatag[0]
        data.append(cl)
        print(et.tostring(cl).decode("ascii"))
        file.write(name)
        return
    print(atag,datatag)
    for i in range(len(atag)):
        try:
            et.SubElement(cl,atag[i]).text=datatag[i]
        except:
            et.SubElement(cl,atag[i]).text=''
    print(et.tostring(data).decode("ascii"))
    file.write(name)
    webbrowser.open(name)
def readxml(name,attr):
    try:
        file=et.parse(name)
        data=file.getroot()
    except:
        print("File not exist")
        return 0
    return data.attrib[attr]
def readxmldata(filename):
    try:
        file=et.parse(filename)
        data=file.getroot()
    except:
        print("File not exist")
        #tkinter.messagebox.showinfo("Error","File Not Found")
        return []
    return [j.text for j in data]
