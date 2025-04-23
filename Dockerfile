FROM python:3.10.12
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install -y wget

RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

RUN apt-get update && apt-get -y install google-chrome-stable

RUN useradd -m chromeuser
USER chromeuser

CMD ["python3", "main.py"]