FROM python:3.11

RUN apt-get update && apt-get install -y cron

WORKDIR /ex_1

ADD ./src/count.py .
ADD ./src/shell_file.sh .

RUN pip install pandas


CMD [ "/bin/bash", "shell_file.sh" ]

