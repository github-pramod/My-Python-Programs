import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pandas

list = []

response = requests.get("https://www.century21.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")  # to crawl through the link given
content = response.text  # convert the html content to readable text

soup = BeautifulSoup(content, "html.parser")  # this is used to crawl through the html file so that we can extract the contents from web
apartments = soup.find("div").find_all(class_="property-card-primary-info")

# below code involves extracting data from web

for apt in apartments:
    d = {}
    d["Price"] = apt.find("a").text.replace(" ", "").replace("\n", "")

    d["Address"] = apt.find("div", {"class": "property-address-info"}, recursive=True).text.replace("\n", "")\
        .replace("                        Rock", ", Rock").replace("  ", "")

    beds = apt.find("div", {"class": "property-beds"})
    if beds is None:
        pass
    else:
        d["Beds"] = beds.text.replace(" ", "").replace("\n", "").replace("beds", "")

    baths = apt.find("div", {"class": "property-baths"}, recursive=True)
    if baths is None:
        pass
    else:
        d["Baths"] = baths.text.replace(" ", "").replace("\n", "").replace("baths", "").replace("bath", "")

    list.append(d)
df = pandas.DataFrame(list)
df.to_csv("Apartments_details.csv", index=False)


# sends an email to the user with Output.csv as the attachment

from_email = "pramoddghadge30@gmail.com"
to_email = "gpramod1994@gmail.com"
subject = "Apartment details"

msg = MIMEMultipart()
msg["From"] = from_email
msg["To"] = to_email
msg["Subject"] = subject

body = "Hi There,\nPlease find attached few Apartment's details in Rock Springs WY 82901. Kindly reach out to us on 123455 if interested." \
       "\nThanks,\nPramod"

msg.attach(MIMEText(body, "plain"))

file_name = "Apartments_details.csv"
attachment = open(file_name, "r")

part = MIMEBase("application", "octet-stream")
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header("Content-Disposition", "attachment; filename="+file_name)
msg.attach(part)

text_string = msg.as_string()

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(from_email, "***********")  # password goes in here


server.sendmail(from_email, to_email, text_string)
server.quit()
