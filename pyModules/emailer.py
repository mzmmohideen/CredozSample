import smtplib

class Gmail(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.server = 'smtp.gmail.com'
        self.port = 587
        session = smtplib.SMTP(self.server, self.port)        
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.email, self.password)
        self.session = session

    def send_message(self, subject, body):
        ''' This must be removed '''
        headers = [
            "From: " + self.email,
            "Subject: " + subject,
            "To: " + "mohideen@botvfx.com",
            "MIME-Version: 1.0",
           "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        self.session.sendmail(
            self.email,
            "mohideen@botvfx.com",
            headers + "\r\n\r\n" + body)

def sendmail():
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login('credosamplemail@gmail.com', 'mohideen123')
    # incase of error goto https://myaccount.google.com/lesssecureapps turn less secure off into
    smtp.sendmail('credosamplemail@gmail.com', ['vignesh.sea97@gmail.com', 'mohideen@botvfx.com'], "This is a Sample Mail")

sendmail()
# gm = Gmail('credosamplemail@gmail.com', 'mohideen123')
# gm.send_message('Subject', 'Message')