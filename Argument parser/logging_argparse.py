"""
python logging_argparse.py --help : will return the description of how to execute this script, including the help message specified in the parser arguments
python logging_argparse.py --artifact_name "Model1" --optional_arg 10 : execute this script with specified value on parser arguments
"""

import logging
import argparse
"""
 In reality, you should make the "level of the logging" an argument of your script (for example using argparse) 
 so the user can tweak the verbosity of the output from the command line.
"""
logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s") #If not specify the path of log file, the loggin message will print out
"""
Creating a specified logger with a specific name, to separate logs from different parts of 
the application, and send to various destinations (handlers)

Direct logging (EX: using logging.info): Logs all messages under the root logger.
"""
logger = logging.getLogger() #retun root logger in default


def go(args):
    # Mark the message as "debug" importance
    # NOTE: since we put level=logging.INFO in the config,
    # the following message will NOT be printed. It will be
    # printed if we change level=logging.DEBUG
    logger.debug("This is a debug message")
    # Mark the message as "info" importance
    logger.info("This is an info message")
    # Mark the message as "warning" importance
    logger.warning("This is a warning")
    # Mark the message as "error" importance
    logger.error("This is an error")
    logger.info(f"This is {args.artifact_name}")
    logger.info(f"This is {args.optional_arg}")

if __name__ == '__main__':
    #Set up an argument parser
    parser = argparse.ArgumentParser(description='This is a tutorial argument parser')
    #Add argument "--artifact_name", cast input to type string, 
    parser.add_argument("--artifact_name", type = str, help = 'Name and version of W&B artifact', required= True)
    parser.add_argument("--optional_arg", type = float, help = 'An optional argument', required=False, default=2.3)
    args = parser.parse_args()
    go(args)
