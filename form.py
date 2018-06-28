import cgi
form = cgi.FieldStorage()
name =  form.getvalue('name')


f = open('file.txt', 'w')
print f

f.write('the test worked')

print(f)




# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
fp = open(textfile, 'rb')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')

# s.sendmail(me, [you], msg.as_string())
s.quit()


###################################################################################################

# import smtplib
#
# gmail_user = 'you@gmail.com'
# gmail_password = 'P@ssword!'
#
# sent_from = gmail_user
# to = ['me@gmail.com', 'bill@gmail.com']
# subject = 'OMG Super Important Message'
# body = 'Hey, what's up?\n\n- You'
#
# email_text = """\
# From: %s
# To: %s
# Subject: %s
#
# %s
# """ % (sent_from, ", ".join(to), subject, body)
#
# try:
#     server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     server.ehlo()
#     server.login(gmail_user, gmail_password)
#     server.sendmail(sent_from, to, email_text)
#     server.close()
#
#     print 'Email sent!'
# except:
#     print 'Something went wrong...'
