FROM python:latest
RUN apt -qq update && pip3 -q install pika
ADD emisor.py /
ADD sleep.sh /
RUN chmod 777 sleep.sh
EXPOSE 5672
CMD ["./sleep.sh"]

