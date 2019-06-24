import smtplib


#Rondinelli Castilho
print ("")
print ("##########################")
dest = raw_input("destinatario: ")
ug = raw_input("Usuario do gmail: ")
pg = raw_input("Senha do gmail: ")
print ("##########################")
print ("")
to = (dest)
gmail_user = (ug)
gmail_pwd = (pg)
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)
header = 'Para:' + to + '\n' + 'De: ' + gmail_user + '\n' + 'Subject:testing \n'
print header
msg = header + '\n mensagem de teste \n\n'
smtpserver.sendmail(gmail_user, to, msg)
print 'Feito!'
smtpserver.close()

