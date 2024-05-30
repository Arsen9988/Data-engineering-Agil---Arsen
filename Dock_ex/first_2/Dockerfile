FROM python:3.11.5

# host container
ADD index.html .

COPY ./main.py ./main.py

EXPOSE 8060

RUN pip install Flask  

CMD ["python", "./main.py"]

