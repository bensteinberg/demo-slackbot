# initial test of a Python worker for deployment to Heroku

import time
import sys

def main():
    """Main loop"""
    while (True):
        print("I'm awake")
        sys.stdout.flush()
        time.sleep(2)

if __name__ == "__main__":
    main()
