

#REMOVE THE TESTING MESSAGE IN SUBJECT LINE



#REMOVE THE TESTING MESSAGE IN SUBJECT LINE



#REMOVE THE TESTING MESSAGE IN SUBJECT LINE


#BEFORE SENDING, DO A) A TEST WITH MZ DIDI ACC B) HIGHLIGHT sendData.txt INSPECT FOR WHITE SPACES AND ANYTHING WEIRD OTHER THAN \t STUFF




import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime, time, sys

def send_email(subject, body, sender, recipient, password, name):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    if encodeHTML:
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


#use one of the code snippits below to test a send
#the latter uses a schedule send flow, the former sends and then will take you through the flow but just abort with ctrl c or disobeying prompts
'''
subject = "Hippo Hack - hackathon for your students!1"
sender = "mzhang0213@gmail.com"
body="HIIIIIIII"
password = "nyttoksinrsxpubl" #generated "App Password" from myaccount.google.com/apppasswords
#michael's password is nyttoksinrsxpubl
#enginuity's password is rysemsfrldxnhder
recipient = "mzhang0213@gmail.com"
arrg=["C:/Users/Michael Zhang/Desktop/pooped on p2.png","C:/Users/Michael Zhang/Desktop/CorpSearchView.pdf"]
send_email(subject, body, sender, recipient, password, arrg)


rawData = open("./sendData - outreach.txt","r").readlines()
for i in range(len(rawData)):
    if rawData[i][-1:]=="\n":
        rawData[i]=rawData[i][:-1]
    rawData[i]=rawData[i].split("\t")
subject = "Hippo Hack - hackathon for your students! TESTING TESTING TESTING"
sender = "enginuitytech@gmail.com"
password = "rysemsfrldxnhder" #generated "App Password" from myaccount.google.com/apppasswords
#michael's password is nyttoksinrsxpubl
#enginuity's password is rysemsfrldxnhder

'''


#get date want to send
mm=input("input month you want to send:\n")
dd=input("input day you want to send:\n")
yy=datetime.datetime.now().strftime("%Y")
mins=input("input @ what min you want to send:\n")
secs=input("input @ what sec you want to send:\n")

sendDate = datetime.datetime(yy,mm,dd,mins,secs)
finalConfirm=input("\nschedule sending for "+sendDate.strftime("%c")+". ABORT TYPE \"N\"\n")
if finalConfirm=="N":
    print("abort mission")
    sys.exit()


#confirm email msgs
body=""
for i in range(len(rawData)):
    
    body = (
    	
    )
    
    print("Message starting on following line:\n")
    print(body)
    print()
    finalconfirmation=input("DO YOU ACTUALLY WANT TO SEND, N TO DECLINE (any key accept)\n")
    if finalconfirmation=="N":
        print("abort mission")
        sys.exit()


#delay
print("delaying, ctrl c if want to stop")
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
    
    body = (
    	
    )
    recipient = rawData[i][3]
    names=[] #file names of all attachments, on this drive
    send_email(subject, body, sender, recipient, password, names)
print("finished sending :)")

#confirmation
body="SENT EMAIL ON '" + sendDate.strftime("%c") + "'\nheres the last (sample) message:\n\n--------------------------------------------------\n\n"+body
send_email(subject, body, sender, "24zhangm@abschools.org", password, names)