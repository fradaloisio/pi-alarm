from lib.log import logger
import re

global active
active = False

def setActive(new):
    #if(newStatus is False or newStatus is "False" or newStatus is "false" or newStatus is 0 or newStatus is "0"):
    if re.search("false", str(new)):
        status = False
        logger.info("Alarm deactivated")
    #elif(newStatus is True or newStatus is "True" or newStatus is "true" or newStatus is 1 or newStatus is "1"):
    elif re.search("true", str(new)):
        status = True
        logger.info("Alarm activated")
    else:
        logger.warn("Invalid status %s" %(new))
        return
    global active
    active = status
def getActive():
    global active
    logger.info("active status %s" %(str(active)))
    return active