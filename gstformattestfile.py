import time,os,pdfkit,webbrowser,shutil
import newworkbook,merge,bill,xmlfile
def create(master):
    dirr=master.dirr
    x=str(master.billdetail[0])[:5]+master.detail[0][:12]
    path=dirr+master.billdetail[1][3:]+"/Back up HTML/"
    path1=dirr+master.billdetail[1][3:]+"/Invoice PDF/"
    code=[" ","Jammu & Kashmir","Himachal Pradesh","Punjab","Chandigarh","Uttarakhand","Haryana","Delhi","Rajasthan",
                     "Uttar Pradesh","Bihar","Sikkim","Arunachal Pradesh","Nagaland","Manipur","Mizoram","Tripura","Meghalaya",
                     "Assam","West Bengal","Jharkhand","Odisha","Chhattisgarh","Madhya Pradesh","Gujarat","Daman & Diu",
                     "Dadra & Nagar Haveli","Maharashtra","Karnataka","Goa","Lakshdweep","Kerala","Tamil Nadu","Puducherry",
                     "Andaman & Nicobar Islands","Telangana","Andhra Pradesh","Other Territory"]
    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.exists(path1):
        os.makedirs(path1)
    try:
        if "gst.css" in os.walk(path):
            pass
        else:
            shutil.copy2(dirr+"gst.css",path+"gst.css")
    except Exception as e:
        print("GSTformattest file :- "+str(e))
    gstno="24BPXPS7371P1ZL"
    mobno="9911930288"
    compname="BHAGYALAXMI COAL"
    compadd="Shop No14, SN 44, Varsana TA, Anjar,Kachchh,Gujarat, 370240"
    try:
        name=merge.init()
        print("GSTformattest file :- "+name,"28 line")
        data=merge.finduser(name)
        print("GSTformattest file :- ",data,"30 line")
        gstno=data[0]
        mobno=data[2]
        compname=data[1]
        compadd=data[3]+data[4]
        '''
        fill=open(dirr+"Users.txt","r")
        data=fill.read()
        fill.close()
        gstno=data.split('~')[0].upper()
        mobno=data.split('~')[2].upper()
        compname=data.split('~')[1].upper()
        compadd=data.split('~')[3].upper()'''
    except Exception as e:
        print(e,"GSTformattest file :- "+"Error in Data Addition")
    val=bill.amount(round(master.igst+master.cgst+master.cessu+master.sgst))
    file=open(path+x+".html","w+")
    sub,tcstst='',''
    dada=round(round(master.gtotal)-master.gtotal,2)
    if dada>0:
        dada="(+)"+str(dada)
    elif dada<0:
        dada="(-)"+str(dada)[1:]
    else:
        dada=str(dada)
    if master.tcst:
        sub=""
        tcstst="""
        <tr class=nobordertd>
        <td width=2%></td>
        <td width=55% style="text-align:right"><b><i>TCS</i></b></p></td>
        <td width=5% style="text-align:center"></td>
        <td width=8% style="text-align:center"></td>
        <td width=5% style="text-align:center">"""+str(master.tcs)+"""</td>
        <td width=5% style="text-align:center">%</td>
        <td width=15% style="text-align:right"><b>"""+str(master.tcst)+"""</b></td>
        </tr>"""
    cessstr,cessstr1,cessstr2,cessstr3,cgststr,cgststr1,cgststr2,cgststr3='','','','','','','',''
    sgststr,sgststr1,sgststr2,sgststr3,igststr,igststr1,igststr2,igststr3='','','','','','','',''
    igstst,sgstst,cgstst,cessst='','','',''
    xyzval=20
    if master.cessu:
        cessst="""
        <tr class=nobordertd>
        <td width=2%></td>
        <td width=55% style="text-align:right"><b><i>GST COMP. CESS</i></b></p></td>
        <td width=5% style="text-align:center"></td>
        <td width=8% style="text-align:center"></td>
        <td width=5% style="text-align:center">"""+str(master.gst[0][3])+"""</td>
        <td width=5% style="text-align:center">"""+str(master.data[0][8])+"""</td>
        <td width=15% style="text-align:right"><b>"""+str(master.cessu)+"""</b></td>
        </tr>"""
        cessstr='<td colspan=2 width=20% style="vertical-align:middle">Cess</td>'
        cessstr1='<td width=10% style="text-align:center">'''+str(int(master.gst[0][3]))+'/'+str(master.data[0][8])+'</td><td width=10% style="text-align:center">'+str(master.cessu)+'</td>'
        cessstr2='<td width=10%></td><td width=10% style="text-align:center"><b>'+str(master.cessu)+'</b></td>'
        cessstr3="<td width=10%>Rate</td><td width=10%>Amount</td>"
    if master.cgst:
        xyzval=20
        cgstst="""<tr class=nobordertd>
        <td width=2%></td>
        <td width=55% style="text-align:right"><b><i>CGST</i></b></td>
        <td width=5% style="text-align:center"></td>
        <td width=8% style="text-align:center"></td>
        <td width=5% style="text-align:center">"""+str(master.gst[0][0])+"""</td>
        <td width=5% style="text-align:center">%</td>
        <td width=15% style="text-align:right"><b>"""+str(master.cgst)+"""</b></td>
        </tr>"""
        cgststr='<td colspan=2 width=20% style="vertical-align:middle">Central GST</td>'
        cgststr1='<td width=5% style="text-align:center">'+str(master.gst[0][0])+'</td><td width=5% style="text-align:center">'+str(master.cgst)+'</td>'
        cgststr2='<td width=10%></td><td width=10% style="text-align:center"><b>'+str(master.cgst)+'</b></td>'
        cgststr3="<td width=10%>Rate</td><td width=10%>Amount</td>"
    if master.igst:
        xyzval=40
        igstst="""<tr class=nobordertd>
        <td width=2%></td>
        <td width=55% style="text-align:right"><b><i>Integrated GST</i></b></td>
        <td width=5% style="text-align:center"></td>
        <td width=8% style="text-align:center"></td>
        <td width=5% style="text-align:center">"""+str(master.gst[0][2])+"""</td>
        <td width=5% style="text-align:center">%</td>
        <td width=15% style="text-align:right"><b>"""+str(master.igst)+"""</b></td>
        </tr>"""
        igststr='<td colspan=2 width=20% style="vertical-align:middle">Integated GST</td>'
        igststr1='<td width=5% style="text-align:center">'+str(master.gst[0][2])+'</td><td width=10% style="text-align:center">'+str(master.igst)+'</td>'
        igststr2='<td width=10%></td><td width=10% style="text-align:center"><b>'+str(master.igst)+'</b></td>'
        igststr3="<td width=10%>Rate</td><td width=10%>Amount</td>"
    if master.sgst:
        sgstst="""
        <tr class=nobordertd>
        <td width=2%></td>
        <td width=55% style="text-align:right"><b><i>SGST</i></b></td>
        <td width=5% style="text-align:center"></td>
        <td width=8% style="text-align:center"></td>
        <td width=5% style="text-align:center">"""+str(master.gst[0][1])+"""</td>
        <td width=5% style="text-align:center">%</td>
        <td width=15% style="text-align:right"><b>"""+str(master.sgst)+"""</b></td>
        </tr>"""
        sgststr='<td colspan=2 width=20% style="vertical-align:middle">State GST</td>'
        sgststr1='<td width=5% style="text-align:center">'+str(master.gst[0][1])+'</td><td width=5% style="text-align:center">'+str(master.sgst)+'</td>'
        sgststr2='<td width=10%></td><td width=10% style="text-align:center"><b>'+str(master.sgst)+'</b></td>'
        sgststr3="<td width=10%>Rate</td><td width=10%>Amount</td>"
    p="""<!DOCTYPE HTML>
    <html>
    <head>
    <title>GST Invoice Display</title>
    <link href="gst.css" type="text/css" rel="stylesheet"></link>
    </head>
    <body>
    <h4 style="text-align:center">Tax Invoice</h4>
    <table class=first width=100%>
    <tr width=100%>
    <td class=line rowspan=3,colspan=2 width=50%>
    <table class=noborder width=100%>
    <tr><td style="font-size:16px;font-weight:bold">"""+compname+"""</td></tr>
    <tr><td style="font-size:14px">"""+compadd+"""</td></tr>
    <tr><td style="font-size:14px">GSTIN		:"""+gstno
    try:
        p=p+"""</td></tr>
        <tr><td style="font-size:14px">STATE NAME	:"""+code[int(gstno[:2])]+""", CODE	:"""+gstno[:2]+"""</td></tr>"""
    except:
        pass
    p=p+"""
    <tr><td style="font-size:14px">MOBILE/Email	:"""+mobno+"""</td></tr>
    <tr><td style="font-size:14px">PAN NO.          :"""
    try:
        p=p+gstno[2:-3]
    except:
        pass
    p=p+"""</td></tr>
    </table>
    </td>
    <td class=line width=25%>
    <table class=noborder width=100%>
    <tr>
    <td style="text-align:left">Invoice No.</td>
    <td style="text-align:right">e-Way Bill No.</td>
    </tr>
    <tr>
    <td style="text-align:left;font-weight:bold"><b>"""+str(master.billdetail[0])+"""</b></td>
    <td style="text-align:right;font-weight:bold"><b>"""+str(master.billdetail[3])+"""</b></td>
    </tr>
    </table>
    </td>
    <td width=25%>
    <table class=noborder width=100%>
    <tr>
    <td >Dated</td>
    </tr>
    <tr>
    <td ><b>"""+str(master.billdetail[1])+"""</b></td>
    </tr>
    </table>
    </td>
    </tr>
    <tr>
    <td width=25%><table class=noborder width=100%>
    <tr>
    <td >Delivery Note</td>
    </tr>
    <tr>
    <td ></td>
    </tr>
    </table></td>
    <td width=25%><table class=noborder width=100%>
    <tr>
    <td >Mode/Terms of Payment</td>
    </tr>
    <tr>
    <td ></td>
    </tr>
    </table></td>
    </tr>
    <tr>
    <td width=25%><table class=noborder width=100%>
    <tr>
    <td >Supplier Reference</td>
    </tr>
    <tr>
    <td >2019/20</td>
    </tr>
    </table></td>
    <td width=25%><table class=noborder width=100%>
    <tr>
    <td>Other References</td>
    </tr>
    <tr>
    <td>"""+master.billdetail[2]+"""</td>
    </tr>
    </table></td>
    </tr>
    <tr width=100%>
    <td class=line rowspan=3,colspan=2 width=50%>
    <table class=noborder width=100%>
    <tr>
    <td style="font-size:16px;">Consignee</td>
    </tr><tr>
    <td style="font-size:14px;text-align:justify"><b>"""+str(master.detail[0])+"""</b></td>
    </tr>
    <tr>
    <tr>
    <td style="font-size:14px;text-align:justify"><b>"""+str(master.detail[1])+"""</b></td>
    </tr>
    <tr><tr>
    <td style="font-size:14px;text-align:justify"><b>"""+str(master.detail[2])+"""</b></td>
    </tr>
    <tr>
    <td style="font-size:14px">GSTIN		:<b>"""+master.detail[-1]+"""</b></td>
    </tr>
    <tr>
    <td style="font-size:14px">STATE NAME 		:<b>"""+code[int(master.detail[-1][:2])]+"""</b>, CODE :<b>"""+master.detail[-1][:2]+"""</b></td>
    </tr>
    <tr>
    <td style="font-size:14px">PAN/IT No. 		:<b>"""+master.detail[-1][2:-3]+"""</b></td>
    </tr>
    </table>
    </td>
    <td class=line width=25%>
    <table class=noborder width=100%>
    <tr>
    <td style="text-align:left">Buyer's Order No.</td>
    </tr>
    <tr>
    <td style="text-align:left"></td>
    </tr></table>
    </td>
    <td width=25%>
    <table class=noborder width=100%>
    <tr>
    <td >Dated</td>
    </tr>
    <tr>
    <td ></td>
    </tr>
    </table>
    </td>
    </tr>
    <tr>
    <td width=25%><table class=noborder width=100%>
    <tr>
    <td >Despatched Through</td>
    </tr>
    <tr>
    <td ><b>"""+str(master.billdetail[-3])+"""</b></td>
    </tr>
    </table></td>
    <td width=25%><table class=noborder width=100%>
    <tr>
    <td >Delivery Note Date</td>
    </tr>
    <tr>
    <td ></td>
    </tr>
    </table></td>
    </tr>
    <tr>
    <td width=25%><table class=noborder width=100%>
    <tr>
    <td >Dispatch Document No.</td>
    </tr>
    <tr>
    <td ></td>
    </tr>
    </table>
    </td>
    <td width=25%><table class=noborder width=100%>
    <tr>
    <td >Destination</td>
    </tr>
    <tr>
    <td ><b>"""+str(master.detail[-2])+"""</b></td>
    </tr>
    </table></td>
    </tr>
    <tr width=100%>
    <td class=line rowspan=3,colspan=2 width=50%>
    <table class=noborder width=100%>
    <tr>
    <td style="font-size:16px;">Buyer(If Other than consignee)</td>
    </tr>
    </table>
    </td>
    <td class=line width=25%>
    <table class=noborder width=100%>
    <tr>
    <td style="text-align:left">Bill of Landing/LR-RR No.</td>
    </tr>
    <tr>
    <td style="text-align:left;font-weight:bold">
    <b>"""+master.billdetail[-2]+"""</b></td>
    </tr></table>
    </td>
    <td width=25%>
    <table class=noborder width=100%>
    <tr>
    <td >Motor Vehicle NO.</td></tr>
    <tr><td ><b>"""+str(master.billdetail[-5])+"""</b></td></tr>
    </table>
    </td>
    </tr>
    <tr>
    <td colspan=2 rowspan=2 style="vertical-align:top" ><table class=noborder width=100%>
    <tr >
    <td >Terms of Delivery</td>
    </tr>
    <tr>
    <td colspan=3 ></td>
    </tr></table>
    </td></tr><tr></tr></table>"""
    p=p+"""</b>	
    <table width=100%>
    <tr id=firstrow>
    <td width=4%>Sr. No</td>
    <td width=55%>Description of Goods</td>
    <td width=4%>HSN/SAC</td>
    <td width=8%>Quantity</td>
    <td width=8%>Rate</td>
    <td width=8%>per</td>
    <td width=15%>Amount</td>
    </tr>"""
    for i in master.data:
        p=p+"""
        <tr class=nobordertd>
        <td width=2% style="text-align:center"><b>"""+i[0]+"""</b></td>
        <td width=55%><p><b>"""+i[1]+"""</b><sub style="font-size:9px"><b>"""+sub+"""</b></sub></p></td>
        <td width=5% style="text-align:center">"""+i[5]+"""</td>
        <td width=8% style="text-align:center"><b>"""+str(i[6]+i[8])+"""</b></td>
        <td width=5% style="text-align:center">"""+str(i[7])+"""</td>
        <td width=5% style="text-align:center">"""+i[8]+"""</td>
        <td width=15% style="text-align:right"><b>"""+str(i[9])+"""</b><br/></td>
        </tr>"""
    p=p+"""
    <tr class=nobordertd>
    </tr>
    """+cgstst+sgstst+igstst+cessst+tcstst+"""
    <tr class=nobordertd>
    <td width=2% style="text-align:center"></td>
    <td width=55%  style="text-align:right"></td>
    <td width=5% style="text-align:center"></td>
    <td width=8% style="text-align:center"></td>
    <td width=5% style="text-align:center"></td>
    <td width=5% style="text-align:center"></td>
    <td  width=5% style="text-align:right;border-top:1px solid black">"""+str(round(master.gtotal,2))+"""</td>
    </tr>
    <tr class=nobordertd>
    <td width=2% style="text-align:center"></td>
    <td width=55% style="text-align:right"><b>ROUND OFF</b></td>
    <td width=5% style="text-align:center"></td>
    <td width=8% style="text-align:center"></td>
    <td width=5% style="text-align:center"></td>
    <td width=5% style="text-align:center"></td>
    <td width=15% style="text-align:right"><b>"""+dada+"""
    </b><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/></td>
    </tr>
    <tr>
    <td width=2% style="text-align:center"></td>
    <td width=55% style="text-align:right"><b>Total</b></td>
    <td width=5% style="text-align:center"></td>
    <td width=8% style="text-align:center"><b>"""+str(master.data[0][6])+str(master.data[0][8])+"""</b></td>
    <td width=5% style="text-align:center"></td>
    <td width=5% style="text-align:center"><b>"""+str(master.data[0][8])+"""</b></td>
    <td width=15% style="text-align:right"><b>"""+str(round(master.gtotal))+"""</b></td>
    </tr>
    <tr><td colspan=7>
    <table width=100% class=noborder>
    <tr class=nobordertd>
    <td>Amount Chargeable(In Words):-</td>
    </tr>
    <tr class=nobordertd>
    <td colspan=7><b>"""+"INR "+master.billdetail[-1]+"""</b></td>
    </tr>
    </table>
    </td>
    </tr>
    </table>"""
    p=p+"""
    <table width=100% style="text-align:center;border:1px solid black;border-bottom:none;">
    <tr >
    <td rowspan=2 width="""+str(xyzval)+"""% style="vertical-align:middle">HSN/SAC</td>
    <td rowspan=2 width=10% style="vertical-align:middle">Taxable Value</td>
    """+cgststr+sgststr+igststr+cessstr+"""
    <td rowspan=2 style="vertical-align:middle">Total Tax Amount</td>
    </tr>
    <tr>
    <b>"""+cgststr3+sgststr3+igststr3+cessstr3+"""</b>
    </tr>
    <tr>
    <td width="""+str(xyzval)+"""%>"""+str(master.data[0][5])+"""</td>
    <td width=10% style="text-align:center">"""+str(master.total)+"""</td>
    """+cgststr1+sgststr1+igststr1+cessstr1+"""
    <td width=10% style="text-align:center">"""+str(round(master.cgst+master.sgst+master.igst+master.cessu,2))+"""</td>
    </tr>
    <tr>
    <td width="""+str(xyzval)+"""%>Total</td>
    <td width=10% style="text-align:center"><b>"""+str(master.total)+"""</b></td>
    <b>"""+cgststr2+sgststr2+igststr2+cessstr2+"""</b>
    <td style="text-align:center"><b>"""+str(round(master.cgst+master.sgst+master.igst+master.cessu))+"""</b></td>
    </tr>
    <tr>
    <td colspan=9 style="text-align:left">
    <table class=noborder>
    <tr>
    <td >Tax Amount In Words:-<b>"""+"INR "+val+"""</b></td></tr><tr><td><br/><br/><br/><br/><br/><br/><br/>Company Pan: <b>"""+gstno[2:-3]+"""</b></td>
    </tr>
    </table>
    </td></tr></table>
    <table width=100% class=noborder style="border-bottom:1px solid black;">
    <tr class=nobordertd><td width=45% style="text-align:left;border-left:1px solid black"><u>Declaration:-</u>
            <br/>We declare that this invoice shows the actual price of the goods described and that all particulars are true and correct.</td>
    <td style="border:1px solid black;position:relative">
            <p style="top:0px;position:absolute;right:0px;">For """+compname+"""</p>
            <p style="bottom:0px;position:absolute;right:0px;">Authorised Signatory</p></td></tr></table><br/>
    <p style="text-align:center;font-size:14px;">THIS IS A COMPUTER GENERATED INVOICE<br/>SUBJECT TO GURUGRAM JURISDICTION</p></p>
            </body>
    </html>"""
    file.write(p)
    file.close()
    dataobj=newworkbook.wordbook()
    dataobj.insert(master)
    pdfkit.from_file(path+x+".html",path1+x+".pdf")
    xmlfile.createxml(dirr+"InvoiceDetail.xml",stag="Invoice_Detail",atag=["Invoice_No","Client","Date","Invoice_Value"],datatag=[master.billdetail[0],master.detail[0],master.billdetail[1],round(master.gtotal)],idd="id",val=master.billdetail[0])
    #webbrowser.open_new_tab(path1+x+".pdf")
