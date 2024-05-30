# Använd officiell Python 3.9-bild som bas
FROM python:3.9

# Installera de angivna paketen
RUN pip install matplotlib

# Ange arbetsmappen i containern
WORKDIR /Exercises_1

ADD ./src/ex1_0_setup.py .

ADD ./src/pip_packages.sh .

# Kommando för att köra applikationen 
CMD ["/bin/bash", "pip_packages.sh"]
