#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Week 5 Assignment."""

import urllib2
import argparse
import csv

class Server:
    """Current Task."""
    def __init__(self):
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_len()

class Request:
    def __init__(self, request):
        self.timestamp = int(request[0])
        self.processTime = int(req[2])

    def get_len(self):
        return self.timestamp

    def get_pages(self):
        return self.processTime

    def wait_time(self, current_time):
        return current_time - self.timestamp


class Queue:
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def simulateOneServer(filename):
    server = Server()
    queue = Queue()
    wait_time = 0

    for request in filename:
        request = int(request[0])
        queue.enqueue(request)

    while not queue.isempty():
        request = queue.dequeue()
        while request.timestamp > server.time_remaining:
            server.tick()
        server.start_next(request)
        wait_time += request.wait_time(server.time_remaining)
        average = sum(wait_time)/len(wait_time) * 0.001
    print("The average waiting time is %2.2f secs for %3d requests."
          %(average, Queue.size))


def main():
    url_parser = argparse.ArgumentParser()
    url_parser.add_argument("--file", help='Enter a url to csv file', type=str)
    args = url_parser.parse_args()

    if args.file:
        try:
            filename = csv.reader(urllib2.urlopen(args.file))
            simulateOneServer(filename)

        except:
            print "url not valid."
    else:
        print "Enter a valid url csv file --file. "


if __name__ == "__main__":
    main()
