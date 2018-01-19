FROM resin/raspberrypi3-python

ENV INITSYSTEM on

RUN pip install --no-cache flask RPi.Gpio

COPY . /usr/src/app
WORKDIR /usr/src/app

EXPOSE 80

CMD ["python", "iot_light.py"]
