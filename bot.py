# initial test of a Python worker for deployment to Heroku

import time
import logging

def main():
    """Main loop"""
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    while (True):
        logging.info("I'm awake and logging")
        time.sleep(2)

if __name__ == "__main__":
    main()
