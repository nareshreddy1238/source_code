import logging
import logging.config
import add
import os

# Get the current directory of the main.py file (custom_config)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the configuration file in util/config
config_file_path = os.path.join(current_dir, '..', 'util', 'configs', 'logging_to_file.conf')

# Configure logging using the configuration file
logging.config.fileConfig(config_file_path)


def main():
    a,b = input("Enter Two numbers:").split()
    output = add.add2Num(a, b)
    print("Output-" + str(output))
    logging.error("Log ended on this line from module-"+ __name__)

if __name__ == "__main__":
    logging.error("Log started on this line from module-"+ __name__)
    main()

