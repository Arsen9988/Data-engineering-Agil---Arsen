# Använd en basimage som innehåller Python
FROM python:3.10.12-alpine

# Kopiera nödvändiga filer till containern
ADD aa.html .
COPY ./main.py ./main.py

# Exponera porten som Flask-appen kommer att köras på
EXPOSE 8070

# Installera Flask
RUN pip install Flask

# Starta Flask-appen
CMD ["python", "./main.py"]