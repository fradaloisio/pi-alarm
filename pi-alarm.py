import time
import RPi.GPIO as GPIO                           #Import GPIO library


from lib.log import logger
import lib.util as active
import lib.api as api
import lib.sender as sender



def store():
    pass
    #store entry in db

def email():
    pass
    #send email

def main():
    #main

    # activate API
    if api.lunch():
        logger.info("API started")
    else:
        logger.error("API failed start")

    GPIO.setmode(GPIO.BOARD)
    pir = 26
    GPIO.setup(pir, GPIO.IN)
    logger.info("Application started")
    while True:
        while active.getActive():
            if GPIO.input(pir):
                time.sleep(1)
                if GPIO.input(pir):
                    active.setDetection("true")
                    sender.emailAlert()
                    active.setDetection("false")
                    time.sleep(0.2)

if __name__ == '__main__':
    main()