#add shebang line for launchd
from bs4 import BeautifulSoup
import os,requests,sys

request = requests.get('http://contest.newyorker.com/')
content = request.content
soup = BeautifulSoup(content,'html.parser')
soup.prettify
src = ''

img = soup.find('div',{'id':'DefaultTab'}).find('img')


if img == []:
    print('Cartoon could not be found.')
else:
    try:
        src = img.get('src')
        print('downloading image...')
        request = requests.get(src)
        request.raise_for_status()
    except OSError:
        pass

    try:
        os.makedirs('Golland_pics')
    except OSError:
        pass

img_file = open(os.path.join('Golland_pics',os.path.basename(src)),'wb')
for chunk in request.iter_content(100000):
    img_file.write(chunk)
img_file.close()

print('image downloaded')




import datetime,bs4,os,requests,sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage

# emailList = {'Jackson': 'Jackson.Gilman-Forlini@baltimorecity.gov','Berke':'Berke.Attila@baltimorecity.gov',
#             'Catherine':'Catherine.Burns2@baltimorecity.gov','Nick':'Nick.Fontanez@baltimorecity.gov',
#             'Willem':'Willem.Elsevier@baltimorecity.gov','Babila':'Babila.Lima@baltimorecity.gov',
#             'Varghese':'Varghese.Paranilam@baltimorecity.gov','Cole':'Coleman.Devries@baltimorecity.gov',
#             'Ben':'Benjamin.Brosch@baltimorecity.gov','Evan':'Evan.Cook@baltimorecity.gov',
#             'Troy':'Troy.Parrish@baltimorecity.gov','Terrence':'Terrence.Jennings@baltimorecity.gov',
#             'Ron':'Ronald.Christmas@baltimorecity.gov','Janice':'Janice.Hyatt@baltimorecity.gov',
#             'Ryan':'Ryan.Trout@baltimorecity.gov','Kay':'kagesta.campbell@baltimorecity.gov',
#             'Gary':'Gary.Holland@baltimorecity.gov'}

emailList = {'bl':'babila.lima30@gmail.com','babs':'babila.lima@baltimorecity.gov','btest':'gollandbot@gmail.com'}


for name,email in emailList.items():

    msg = MIMEMultipart()
    msg['To'] = email
    msg['From'] = 'GollandBot'
    msg['Subject'] = name + ' Timesheets--Golland : )'
    body = MIMEText(name + ',' + "\n\tThis is Golland, your friendly timesheet reminder. I'm a bot. My job is to remind you to submit a \
    completed timesheet to your supervisor. That\'s what I care abot. You know the clock is ticking on this task, so rather than send you an \
    image of a ticking clock, instead, I will shoot you the most recent caption contest image from the New Yorker Magazine.\n\nGet those \
    creative juices flowing! If you have a good idea for this week's caption contest, I encourage you to submit it and share with your \
    comrades.\n\nHand in your timesheet today by 10:00am, if you have not done so already and good luck with the caption contest.\
    \n\t\t\t\t\t\t\t\t--Gollandbot")
    msg.attach(body)

    if len(os.path.basename(src)) > 1:
        file = open(os.path.join('Golland_pics',os.path.basename(src)),'rb').read()
        attachment = MIMEImage(file, name = os.path.basename(src))
        msg.attach(attachment)
    else:
        pass

    smtpObj = smtplib.SMTP('smtp.gmail.com',587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.ehlo()
    smtpObj.login('gollandbot@gmail.com',sys.argv[1]) #add pass for launchd
    smtpObj.sendmail(msg['From'],msg['To'],msg.as_string())
    smtpObj.quit()
    print('Email sent to ' + name)
print('Emails Sent...')
