#!/usr/bin/env python3

import argparse
import faulthandler
import logging
import os
import sys

from datetime import datetime
from pprint import pprint

MY_PATH = os.path.normpath(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(MY_PATH, 'python')))

logging.basicConfig(level=logging.INFO)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import _test as test

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def runTest():
    test.init()

    assert(test.getGlobalName() == '')
    test.setGlobalName('Test Global Name')
    assert(test.getGlobalName() == 'Test Global Name')

    assert(test.getGlobalBuffer() == b'')
    test.setGlobalBuffer(b'54321')
    #print(test.getGlobalBuffer())
    assert(test.getGlobalBuffer() == b'54321')

    g = test.Gimmick()
    assert(g.getName() == '')
    g.setName('Test Name')
    assert(g.getName() == 'Test Name')

    assert(g.getBuffer() == b'')
    g.setBuffer(b'12345')
    #print(g.getBuffer())
    #g.printBuffer()
    assert(g.getBuffer() == b'12345')

    assert(g.counter == 0)
    g.counter = 10
    assert(g.counter == 10)
    assert(g.moveCounter(g.DIR_UP) == 11)
    assert(g.moveCounter(g.DIR_DOWN) == 10)
    assert(g.moveCounter(g.DIR_DOWN) == 9)
    assert(g.counter == 9)

    test.destroy()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Dump logging output with colors

class ColorStderr(logging.StreamHandler):
    def __init__(self, fmt=None):
        class AddColor(logging.Formatter):
            def __init__(self):
                super().__init__(fmt)
            def format(self, record: logging.LogRecord):
                msg = super().format(record)
                # Green/Cyan/Yellow/Red/Redder based on log level:
                color = '\033[1;' + ('32m', '36m', '33m', '31m', '41m')[min(4,int(4 * record.levelno / logging.FATAL))]
                return color + record.levelname + '\033[1;0m: ' + msg
        super().__init__(sys.stderr)
        self.setFormatter(AddColor())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

LOG_FILE_FORMAT = "[%(levelname)s] [%(pathname)s:%(lineno)d] [%(asctime)s] [%(name)s]: '%(message)s'"
LOG_CONSOLE_FORMAT = "[%(pathname)s:%(lineno)d] [%(asctime)s]: '%(message)s'"
LOG_GUI_FORMAT = "[%(levelname)s] %(message)s"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--quiet', help='set logging to ERROR',
                        action='store_const', dest='loglevel',
                        const=logging.ERROR, default=logging.INFO)
    parser.add_argument('-d', '--debug', help='set logging to DEBUG',
                        action='store_const', dest='loglevel',
                        const=logging.DEBUG, default=logging.INFO)
    parser.add_argument('--log', action=argparse.BooleanOptionalAction)
    parser.add_argument('test', nargs=argparse.REMAINDER)
    args = parser.parse_args()

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.handlers = []

    log_console_handler = ColorStderr(LOG_CONSOLE_FORMAT)
    log_console_handler.setLevel(args.loglevel)
    logger.addHandler(log_console_handler)

    if args.log:
        now = datetime.now()
        logs_dir = os.path.abspath(os.path.join(MY_PATH, 'logs', f"{now.strftime('%Y%m%d')}"))
        os.makedirs(logs_dir, exist_ok=True)
        log_filename = f"{now.strftime('%Y%m%d')}_{now.strftime('%H%M%S')}.txt"
        log_file_handler = logging.FileHandler(os.path.join(logs_dir, log_filename))
        log_formatter = logging.Formatter(LOG_FILE_FORMAT)
        log_file_handler.setFormatter(log_formatter)
        log_file_handler.setLevel(logging.DEBUG)
        logger.addHandler(log_file_handler)
        logging.info(f"Storing log into '{logs_dir}/{log_filename}'")

    if not args.test:
        tests = [ 'test' ]
    else:
        tests = args.test

    for test in tests:
        logging.info(f"Running test: {test}")
        if test == 'test':
            runTest()
        else:
            logging.warning(f"Unknown test: {test}")

    return 0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    faulthandler.enable()
    sys.exit(main())
