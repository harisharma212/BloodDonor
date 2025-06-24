import smtplib, ssl
import requests
import urllib.parse
import haversine
from haversine import Unit

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(name, mail, phone, address, blood_group, date, receiver_email={}):
    """
    Method to send an email
    Added one more commit
    TAG_1
    TAG_2
    """
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "Your Gmail Account"
    receiver_email = receiver_email
    password = "Your Password"

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = " ".join(receiver_email)

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    Hope ypu are doing great."""

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        for donorName, r_mail in receiver_email.items():
            html = f"""\
                <html>
                  <body bgcolor='orange'>
                    <p>Hi {donorName},<br>
                       We have a blood donation request<br>
                       Please find the below details and do the needful at the earliest.
                       <table border="1" align="center">
                            <tr>
                                <th>Name</th>
                                <td>{name}</td>
                            </tr>
                            <tr>
                                <th>Blood Group</th>
                                <td>{blood_group}</td>
                            </tr>
                            <tr>
                                <th>Phone</th>
                                <td>{phone}</td>
                            </tr>
                            <tr>
                                <th>Email</th>
                                <td>{mail}</td>
                            </tr>
                            <tr>
                                <th>Address</th>
                                <td>{address}</td>
                            </tr>
                            <tr>
                                <th>Required By</th>
                                <td>{date}</td>
                            </tr>
                       </table>
                    </p>
                  </body>
                </html>
                """
                # Turn these into plain/html MIMEText objects
            part1 = MIMEText(text, "plain")
            part2 = MIMEText(html, "html")

            # Add HTML/plain-text parts to MIMEMultipart message
            # The email client will try to render the last part first
            message.attach(part1)
            message.attach(part2)
            server.sendmail(
                sender_email, r_mail, message.as_string()
            )

def get_latlong(location):
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(location) +'?format=json'

    response = requests.get(url).json()
    return (float(response[0]["lat"]), float(response[0]["lon"]))

def calculate_distance(source, destination):  
    loc1 = get_latlong(source)
    loc2 = get_latlong(destination)
    return (haversine.haversine(loc1,loc2,unit=Unit.METERS) / 1000)
