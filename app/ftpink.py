from ftplib import FTP
from logzero import logger
import time
import settings


def run():
    try:
        while True:
            ftp = FTP(
                host=settings.FTP_HOST,
                user=settings.FTP_LOGIN,
                passwd=settings.FTP_PASSWD,
                acct='',
                timeout=None,
            )

            logger.info(ftp.welcome)
            ftp.cwd('/')
            logger.info(ftp.nlst())

            filenames = ftp.nlst()
            for filename in filenames:

                with open(filename, 'wb') as file:
                    ftp.retrbinary('RETR %s' % filename, file.write)

            ftp.quit()
            time.sleep(settings.TIME_SLEEP)
    except Exception:
        logger.error('530 Login incorrect.')
        pass
