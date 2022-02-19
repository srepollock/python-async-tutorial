#!/usr/bin/env python3
# encoding: utf-8
#
# By: Spencer Pollock <spencer at spollock dot ca>
# Date: 2022 

'''
Python Standard Libraries
'''
import argparse
import asyncio
import configparser
import datetime
import glob
import json
import hmac
import hashlib
import logging
import multiprocessing
import io
import random
import shlex
import subprocess
import sys
import time
import threading
import traceback
import os

'''
Libraries
'''
#import requests
#from dotenv import load_dotenv, find_dotenv

'''
Local Modules
'''

'''
Script Environment Set Up
'''
#load_dotenv(find_dotenv())

'''
Global variables
'''
DEBUG = False
VERBOSE = False

LOG_FILE='{}.log'.format(os.path.basename(__file__).split('.')[0])
DEFAULT_CONFIG_FILE='default.cfg'

'''
Functions
'''
async def count():
    logging.log(logging.INFO, '[**] One')
    await asyncio.sleep(1)
    logging.log(logging.INFO, '[**] Two')


'''
Classes
'''
class ExampleClass:
    def __init__(self):
        pass

'''
Main runners
'''
def get_args():
    '''
    A good Python example script.
    '''
    parser = argparse.ArgumentParser(description='A fancy description goes here for your script.')
    parser.add_argument('--config', dest='configfile', type=str, default=DEFAULT_CONFIG_FILE, help='Config file to use. DEFAULT_CONFIG_FILE to \'{}\'.'.format(DEFAULT_CONFIG_FILE))
    parser.add_argument('--debug', dest='debug', action='store_true', help='Runs debug statements and checks without processing.')
    parser.add_argument('--verbose', dest='verbose', action='store_true', help='Runs the script in verbose mode.') 
    return parser.parse_args()

async def main(args):
    '''
    Main function for running.
    '''
    global DEBUG
    global VERBOSE
    DEBUG = args.debug
    VERBOSE = args.verbose
    if (VERBOSE):
        print ('Verbose is {}'.format(VERBOSE))
        logging.debug('Verbose is {}'.format(VERBOSE))
    if (args.configfile == DEFAULT_CONFIG_FILE):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), DEFAULT_CONFIG_FILE)))
    else:
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), args.configfile)))
    # Start main
    await asyncio.gather(count(), count(), count())
    # End main
    return 0

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(message)s', filename=LOG_FILE, level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')
    args = get_args()
    s = time.perf_counter()
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(args))
    finally:
        loop.close()
    elapsed = time.perf_counter() - s
    logging.log(logging.INFO, f'[**] {__file__} executed in {elapsed:0.2f} seconds.')
    logging.shutdown()