FROM python:3.8


RUN apt update

WORKDIR /opt

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . . 

ENV FLASK_APP "app.py"
ENV SERVER_IP "0.0.0.0"

ENV SERVER_PORT "5000"

EXPOSE ${SERVER_PORT}

CMD ["python", "app.py"]

