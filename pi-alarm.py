
from lib.log import logger
import lib.util as active
import lib.api as api

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
    # while True:
    #     pass
        #main loop
        # while active.getActive():
        #     #do stuff
        #     pass


        #in store insert deactivation





if __name__ == '__main__':
    main()