import smtplib

MyServer = smtplib.SMTP("smtp.gmail.com", 587)

MyServer.starttls()

MyServer.login("parasverma0527@gmail.com", "jelbsrkbwmjmgvae")

MyServer.sendmail("parasverma0527@gmail.com", "nitinempire07@gmail.com", "Hyy this message send from a python program, did you receive this or not")

