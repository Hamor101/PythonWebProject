import socket
import argparse
import filetransfer

parser = argparse.ArgumentParser(description="file send/receive program")

parser.add_argument("-s", "--send", action="store_true", help="Send file with specified filename to specified address")
parser.add_argument("-r", "--receive", action="store_true", help="Receive file and save to specified filename")
parser.add_argument("-a", "--address", type=str)
parser.add_argument("-p", "--port", type=int)
parser.add_argument("-f", "--filename", help="File name/path")
args = parser.parse_args()

t = filetransfer.Transferer(args)
# assert args.send ^ args.receive
if args.send:
    t.send()
elif args.receive:
    t.receive()