


# EMAIL HAS 1 ATTACHMENTS AND IS FROM ET




import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime, time, sys

def send_email(subject, body, sender, recipient, password, name, encodeHtml):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    if encodeHTML:
        body="<html><head></head><body>"+body+"</body></html>"
        msg.attach(MIMEText(body, 'html'))
    else:
        msg.attach(MIMEText(body, 'plain'))
    for i in name:
        attachment = open(i, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        ind=0
        for j in range(len(i)-1,0,-1):
            if i[j]=='/':
                ind=len(i)-(j+1)
                break        
        p.add_header('Content-Disposition', "attachment", filename=i[-ind:])
        msg.attach(p)
    context = ssl.create_default_context()
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender,password)
    session.sendmail(sender,recipient,msg.as_string())
    session.quit()



#format of rawData
# funding
#   contact name \t contact email
# outreach
#   recipient's name (teacher / first name) \t recipient's school \t recipient's club \t recipient email \n ...


#format of template
#   line 1 - index of where recipient shows up in the array rawData
#   line 2 - subject line
#   $x$ where x is a position in the array rawData (ie a field for someone in the spreadsheet)




''''''
''''''
#PICK LETTER WANT TO SEND
letter = input("what letter do you want to send\n")
''''''
''''''




if letter == "test":
    send_email("hi test", "this is a test<br><b>multi line</b><br><br>hiiiiiiiiiiii<br>mz", "mzhang0213@gmail.com", "mzhang0213@gmail.com", "nyttoksinrsxpubl", [], True)
    sys.exit()


rawData=open("C:/Users/Michael Zhang/Desktop/Enginuity-Tech/Hippo Hack/data/"+letter+".txt","r", encoding="UTF-8").readlines()
template=open("C:/Users/Michael Zhang/Desktop/Enginuity-Tech/Hippo Hack/templates/"+letter+".txt","r", encoding="UTF-8").readlines()
body=""

recipientPos=int(template[0][:-1])
encodeHTML = bool(template[1][:-1])
subject = template[2][:-1]

template.pop(0)
template.pop(0)
template.pop(0)
template="".join(template)

for i in range(len(rawData)):
    if rawData[i][-1:]=="\n":
        rawData[i]=rawData[i][:-1]
    rawData[i]=rawData[i].split("\t")
sender = "enginuitytech@gmail.com"
password = "yeklvbfuwxaehvgk" #generated "App Password" from myaccount.google.com/apppasswords
#michael's password is nyttoksinrsxpubl
#enginuity's password is yeklvbfuwxaehvgk


#get date want to send
mm=input("input month you want to send:\n")
if mm=="":mm=datetime.datetime.now().strftime("%m")
dd=input("input day you want to send:\n")
if dd=="":dd=datetime.datetime.now().strftime("%d")
yy=datetime.datetime.now().strftime("%Y")
print("time time now is: "+datetime.datetime.now().strftime("%m/%d/%Y, %I:%M:%S %p"))
hrs=input("input @ what hrs you want to send include am or pm after number:\n")
if hrs[-2:]=="am":
    hrs=hrs[:-2]
else:
    hrs=str(12+int(hrs[:-2]))
mins=input("input @ what mins you want to send:\n")

sendDate = datetime.datetime(int(yy),int(mm),int(dd),int(hrs),int(mins))
finalConfirm=input("\nschedule sending for "+sendDate.strftime("%c")+". ABORT TYPE IN \"N\"\n")
if finalConfirm=="N":
    print("abort mission")
    sys.exit()


#confirm email msgs
names=["C:/Users/Michael Zhang/Desktop/Enginuity-Tech/Hippo Hack/Hippo Hack Prospectus.pdf"]
#file names of all attachments, on this drive
#loaded rn: 1 flyer

print("reviewing messages, starting on following line:\n\n")
for i in range(len(rawData)):
    
    body=template
    for j in range(len(body)-1,1,-1):
        if body[j]=="$" and body[j-2]=="$":
            body=body[0:j-2]+rawData[i][int(body[j-1])]+(body[j+1:] if j<len(body) else "")
    print()
    print()
    print("recipient: "+rawData[i][recipientPos])
    print(body)
    print()
    finalconfirmation=input("DO YOU ACTUALLY WANT TO SEND, N TO DECLINE (any key accept)\n")
    if finalconfirmation=="N":
        print("abort mission")
        sys.exit()


#delay
print("delaying, as of "+ str(time.strftime("%I:%M %p")) +" going to send "+ str(len(rawData)) +" messages with "+ str(len(names))+" attachments in "+ str((sendDate.timestamp()-time.time())/60)[:5] +" mins, ctrl c if want to stop")
time.sleep(sendDate.timestamp()-time.time())


#send emails
print("ok ready to go, sending in 3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("sending in process...")

for i in range(len(rawData)):
    
    if encodeHTML:
        for j in range(len(template)-1,0,-1):
            if template[j]=="\n":
                template=template[0:j]+"<br>"+template[j+1:len(template)]
    body=template
    for j in range(len(body)-1,1,-1):
        if body[j]=="$" and body[j-2]=="$":
            body=body[0:j-2]+rawData[i][int(body[j-1])]+(body[j+1:] if j<len(body) else "")
    
    recipient = rawData[i][recipientPos]
    send_email(subject, body, sender, recipient, password, names, encodeHTML)
print("finished sending :)")

#confirmation
body="SENT EMAIL ON  " + sendDate.strftime("%c") + "\nheres the last (sample) message:\n\n--------------------------------------------\n\n"+body
send_email("confirmation sent "+str(len(rawData))+" emails each w/ "+str(len(names))+" attachments | "+subject, body, sender, "24zhangm@abschools.org", password, names, False)