import csv,merge
import openpyxl as op
import os
class csvd():
    def __init__(self):
        pass
        self.states=[" ","01-Jammu & Kashmir","02-Himachal Pradesh","03-Punjab","04-Chandigarh","05-Uttarakhand","06-Haryana","07-Delhi","08-Rajasthan",
                     "09-Uttar Pradesh","10-Bihar","11-Sikkim","12-Arunachal Pradesh","13-Nagaland","14-Manipur","15-Mizoram","16-Tripura","17-Meghalaya",
                     "18-Assam","19-West Bengal","20-Jharkhand","21-Odisha","22-Chhattisgarh","23-Madhya Pradesh","24-Gujarat","25-Daman & Diu",
                     "26-Dadra & Nagar Haveli","27-Maharashtra","29-Karnataka","30-Goa","31-Lakshdweep","32-Kerala","33-Tamil Nadu","34-Puducherry",
                     "35-Andaman & Nicobar Islands","36-Telangana","37-Andhra Pradesh","97-Other Territory"]
    def HSN(self,file):
        '''
        data=["HSN",'Descripiton','UQC','Total Quantity','Total Value','Taxable Value','Integrated Tax Amount','Central Tax Amount','State/UT Tax Amount','Cess Amount']
        d=0
        dirr="C:/Users/"+str(os.getlogin())+"/Desktop/GST Data/"+file[:-5]+"/"
        if os.path.exists(dirr):
            pass
        else:
            os.mkdirs(dirr)
        wb=load_workbook(file)
        try:
            wb.remove(wb['Sheet'])
            wb.remove(wb['Sheet1'])
        except:
            pass
        for sheet in wb:
            for row in sheet:
                val=None
                    if int(float(row[12].value))>2000:
                        val="NOS-NUMBERS"
                    elif int(float(row[12].value))<70:
                        val="MTS-METRIC TONNES"
                    else:
                        val="SQF-SQUARE FEET"
                    #print(ad)
                    if val[:6]+".csv" in os.listdir(dirr):
                        fil=open(dirr+val[:6]+".csv","w",newline="")
                        writer=csv.writer(fil)
                    else:
                        fil=open(dirr+val[:6]+".csv","w",newline="")
                        writer=csv.writer(fil)
                        writer.writerow(data)
                    try:
                        newdata=[int(row[11].value),row[7].value,val,float(row[12].value),float(row[21].value),float(row[14].value),float(row[20].value),float(row[18].value),float(row[19].value),float(row[24].value)]
                    except:
                        newdata=[int(row[11].value),row[7].value,val,float(row[12].value),float(row[21].value),float(row[14].value),float(row[20].value),float(row[18].value),float(row[19].value),0.0]
                    writer.writerow(newdata)
                    fil.close()
        hsnval=[]
        for fille in os.listdir(dirr):
            tquant,tval,taxval,igst,cgst,sgst,cess=0.0,0.0,0.0,0.0,0.0,0.0,0.0
            fil=open(dirr+fille,"r")
            reader=csv.reader(fil)
            line=None
            for line in reader:
                print(line)
                try:
                    tquant,tval,taxval,igst,cgst,sgst,cess=tquant+float(line[3]),tval+float(line[4]),taxval+float(line[5]),igst+float(line[6]),cgst+float(line[7]),sgst+float(line[8]),cess+float(line[9])
                except Exception as err:
                    print(str(err))
            hsnval.append([line[0],line[1],line[2],tquant,tval,taxval,igst,cgst,sgst,cess])
            fil.close()
        fil=open("C:/Users/"+str(os.getlogin)+"/Desktop/GST Data/"+file.split("/")[-1][:-5]+"/"+file.split("/")[-1][:-5]+hsn"+".csv","w+",newline="")
        writer=csv.writer(fil)
        writer.writerow(data)
        for i in hsnval:
            writer.writerow(i)
        fil.close()'''
    def csvfilecreate(self,file):
        wb=op.load_workbook(file)
        path="C:/Users/"+os.getlogin()+"/Desktop/GST Data/"+merge.init()+"/"
        fil=path+file.split("/")[-1][:-5]+"/"+file.split("/")[-1][:-5]+".csv"
        self.csvdata=["GSTIN/UIN of Recipient","Receiver Name","Invoice Number","Invoice date","Invoice Value","Place Of Supply","Reverse Charge","Invoice Type","E-Commerce GSTIN","Rate","Applicable % of Tax Rate","Taxable Value","Cess Amount"]
        #newdata=[master.tax[1],master.tax[0],round(master.tax[2]),master.tax[3],master.gtotal,master.tax[5],"N","Regular","",5,"",master.total,master.cess]
        fill=open(fil,"w+",newline='')
        dtl=csv.writer(fill,delimiter=",")
        dtl.writerow(self.csvdata)
        for sheet in wb:
            try:
                pos=self.states[int(sheet[2][4].value[:2])]
                invalue=float(sheet[2][18].value)-float(sheet[2][17].value)-float(sheet[2][16].value)-float(sheet[2][15].value)-float(sheet[2][14].value)-float(sheet[2][13].value)
                newdata=[sheet[2][4].value,sheet[2][0].value,sheet[2][5].value,sheet[2][6].value,round(float(sheet[2][18].value)),pos,sheet[2][10].value,"Regular",'',sheet[4][4].value,'',invalue,sheet[2][16].value]
                dtl.writerow(newdata)
            except Exception as err:
                print(str(err))
        fill.close()    
