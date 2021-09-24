from openpyxl import *
import time,os,csv
def HSN(master):
    data=["HSN","Description","UQC","Total Quantity","Total Value","Taxable Value","Integrated Tax Amount","Central Tax Amount","State/UT Tax Amount","Cess Amount"]
    today=master.tax[3][3:]+".csv"
    path="C:/Users/"+os.getlogin()+"/Desktop/GST Data/"
    if today in os.listdir(path=path):
        wb=open(path+today,"a+",newline='')
        writer=csv.writer(wb)
    else:
        wb=open(path+today,"w",newline='')
        writer=csv.writer(wb)
        writer.writerow(data)
    for i in master.data:
        if int(master.data[i][6])>2000:
            val="NOS-NUMBERS"
        elif int(master.data[i][6])<100:
            val="MTS-METRIC TONNES"
        else:
            val="SQF-SQUARE FEET"
        insert=[i[5],i[1],val,i[6],float(i[8])+round(float(i[8])*5/100),i[8],round(float(i[8])*5/100),0,0,master.cess]
        writer.writerow(insert)
    wb.close()
def insert(master):
    data=["GSTIN OF Supplier","Invoice Number","Invoice date","Invoice Value","Place of Supply","Reverse Charge",
               "Invoice Type","Rate","Taxable Value","Integrated Tax Paid","Central Tax Paid","State/UT Tax Paid","Cess Paid",
               "Eligibilty","Availed ITC Integrated Tax","Availed ITC Central Tax","Availed ITC State/UT Tax","Availed ITC Cess"]
    today=master.tax[3][3:]+".csv"
    path="C:/Users/"+os.getlogin()+"/Desktop/GST Data/"
    if today in os.listdir(path=path):
        wb=open(path+today,"a+",newline='')
        writer=csv.writer(wb)
    else:
        wb=open(path+today,"w",newline='')
        writer=csv.writer(wb)
        writer.writerow(data)
    insert=[master.tax[1],master.tax[2],master.tax[3],master.gtotal,"08-Rajasthan","N","Regular",5,round(master.total),master.igst,master.cgst,
            master.sgst,master.cess,"Ineligible",0,0,0,0]
    writer.writerow(insert)
    wb.close()
    HSN(master)
