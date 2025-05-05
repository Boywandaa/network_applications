from ftplib import FTP

ftp = FTP()
ftp.connect("209.51.188.20", 21)  # Use IPv4 directly
ftp.login()
print(ftp.getwelcome())
files = ftp.nlst()
for f in files:
    print(f)
# ftp.retrlines("LIST")
ftp.quit()
