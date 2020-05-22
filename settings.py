import os

FTP_HOST = os.getenv("FTP_HOST", "<host>")
FTP_LOGIN = os.getenv("FTP_LOGIN", "<ftp_user>")
FTP_PASSWD = os.getenv("FTP_PASSWD", "<ftp_pass>")
TIME_SLEEP = os.getenv("TIME_SLEEP", int("10"))
