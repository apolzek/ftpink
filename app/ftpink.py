from ftplib import FTP
from logzero import logger
import time
import settings


def conn():
    try:
        ftp = FTP(
            # pylint: disable=maybe-no-member
            host=settings.FTP_HOST,
            user=settings.FTP_LOGIN,  
            passwd=settings.FTP_PASSWD,  
            acct='',
            timeout=None,
        )
        logger.info(ftp.welcome)
        return ftp

    except Exception:
        logger.error('FTP connection failed.')
        exit(1)


def run():

    ftp_con = conn()
    ftp_con.cwd('/')
    filenames = ftp_con.nlst()

    for filename in filenames:
        try:
            with open(filename, 'wb') as file:
                ftp_con.retrbinary('RETR %s' % filename, file.write)
        except Exception:
            pass
