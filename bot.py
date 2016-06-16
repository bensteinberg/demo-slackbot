# initial test of a Python worker for deployment to Heroku

import time
import logging

def main():
    """Main loop"""
    while (True):
        logging.warning("I'm awake and logging")
        time.sleep(2)

if __name__ == "__main__":
    main()
