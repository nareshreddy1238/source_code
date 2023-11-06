import logging
import logging.config
import add

# Configure logging using the configuration file
logging.config.fileConfig("util/configs/logging_to_console.conf")

def main():
    a,b = input("Enter Two numbers:").split()
    output = add.add2Num(a, b)
    print("Output-" + str(output))
    logging.error("Log ended on this line from module-"+ __name__)

if __name__ == "__main__":
    logging.error("Log started on this line from module-"+ __name__)
    main()

