FROM ubuntu

# Install dependencies
RUN apt-get update && apt-get -y install python3 python3-pip
RUN pip install flask

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /
COPY / .

ENTRYPOINT ["python3", "app.py"]
