import time


from lib.log import logger
import lib.util as active
import lib.api as api
import lib.sender as sender



def store():
    #store entry in db
    pass

def email():
    #send email
    pass

def main():
    #main

    # activate API
    if api.lunch():
        logger.info("API started")
    else:
        logger.error("API failed start")


    logger.info("Application started")
    while True:
       #main loop
        while active.getActive():
            if active.getDetection():
                sender.emailAlert()
                active.setDetection("false")
                time.sleep(60)


        #in store insert deactivation





if __name__ == '__main__':
    main()