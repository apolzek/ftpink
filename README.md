ftpink
======

Default:

```
docker run -e FTP_HOST='<host>' -e FTP_LOGIN='<ftp_user>' -e FTP_PASSWD='<ftp_pass>"' apolzek/ftpink:latest
```

Example:

```
docker network create -d bridge ftptest

docker run --rm -it --net=ftptest -p 21:21 -p 4559-4564:4559-4564 -e FTP_USER=guest -e FTP_PASSWORD=pass docker.io/panubo/vsftpd:latest

```

```
docker run --network=ftptest -e FTP_HOST=172.24.0.2 -e FTP_LOGIN=guest -e FTP_PASSWD=pass apolzek/ftpink:latest
```


<img src="https://i.imgur.com/3JvgReJ.png">
