import os

FTP_HOST = os.getenv("FTP_HOST", "192.168.100.8")
FTP_LOGIN = os.getenv("FTP_LOGIN", "vsftp")
FTP_PASSWD = os.getenv("FTP_PASSWD", "pass")
TIME_SLEEP = os.getenv("TIME_SLEEP", int("10"))
