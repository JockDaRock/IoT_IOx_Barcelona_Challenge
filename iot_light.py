from flask import Flask
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

app = Flask(__name__)

@app.route('/light1on')
def light1on():
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(18, GPIO.LOW)
    return "light 1 is on light 2 is off"


@app.route('/light2on')
def light2on():
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(15, GPIO.LOW)
    return "light 2 is on light 1 is off"


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=80, debug=True)
    except KeyboardInterrupt:
        GPIO.cleanup()
