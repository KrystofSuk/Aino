from os.path import isdir
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time
import shutil

from config import *


def check_extension(file):
    extension = '.' + file.split('.')[-1]
    if(extension in filters):
        return filters[extension]
    return None

def construct_path(file, destination, override = True):
    #print(file, destination)
    destination_path = destination + '/' + file    
    i = 1


    while os.path.isfile(destination_path):
        if override != True:
            return None

        split = file.split('.')
        extension = '.' + split[-1]
        name = file[0: -len(split[-1]) - 1] + '(' + str(i) + ')'
        destination_path = destination + '/' + name + extension
        i += 1
    
    return destination_path


def main():
    #loop through tracked directory
    for directory in tracked_directory:
        for file in os.listdir(directory):
            destination = check_extension(file)
            if destination != None:
                path = construct_path(file, destination)
                if path != None:
                    destination_directory = path[:-len(path.split('/')[-1]) - 1]
                    if os.path.isdir(destination_directory) == False:
                        os.makedirs(destination_directory)
                    shutil.move(directory + '/' + file, path)

if __name__ == '__main__':
    main()