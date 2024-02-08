#!/usr/bin/python3

from argparse import ArgumentParser
import socket
from threading import Thread
from time import time

open_ports=[]

def prepare_args():
    """prepare argumemt
        return:
            args(args.Namespace)
    """
    parser = ArgumentParser(description="Python based code Scanner",usage="%(prog)s 192.168.1.2",epilog="Example : %(prog)s -s 20 -e 40000 -t 500 -V 192.168.1.2")
    parser.add_argument(metavar="IPv4",dest="ip",help="host/ip for scan")
    parser.add_argument("-s","--start",dest="start",metavar="",type=int,help="starting Value",default=1)
    parser.add_argument("-e","--end",dest="end",type=int,metavar="",help="ending port",default=65535)
    parser.add_argument("-t","--threads",dest="threads",metavar="",type=int,help="Thread to use",default=500)
    parser.add_argument("-V","--verbose",dest="verbose",action="store_true",help="verbose output")
    parser.add_argument("-v","--version",action="version",version="%(prog)s 1.0",help="display version")
    args = parser.parse_args()
    return args



def prepare_ports(start:int,end:int):
    """generator Function for ports

        arguments:
            start(int) -- starting port
            end(int) --   ending port
    """
    for port in range(start,end+1):
        yield port


def scan_port():
    """scan ports
    """
    while True:
        try:
            s = socket.socket()
            s.settimeout(1)
            port = next(ports)
            s.connect((arguments.ip,port))
            open_ports.append(port)
            if arguments.verbose:
                print(f"\r{open_ports}",end="")#f"\r{<var>}" clearscreen and print
        except (ConnectionRefusedError,socket.timeout):
            continue
        except StopIteration:
            break

def prepare_threads(threads:int):
    """create ,start threads

    argument:
    threads(int) - number of threads to use
    """
    thread_list = []
    for _ in range(threads+1):# use _ when there is no need of var
        thread_list.append(Thread(target=scan_port))

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

if __name__=="__main__":
    arguments = prepare_args();
    ports = prepare_ports(arguments.start,arguments.end)
    start_time = time()
    prepare_threads(arguments.threads)
    end_time=time()
    if arguments.verbose:
        print()
    print(f"Open Ports found - {open_ports}")
    print(f"Time Taken - {round(end_time-start_time,2)}")
