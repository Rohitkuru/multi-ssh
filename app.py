import paramiko
from tqdm import tqdm
import argparse
import os

def ssh_execute(hostname):

    try:
        ssh_client.connect(hostname=hostname, username="rkurdukar", password="Arjun@me123",timeout=10)
        stdin, stdout, stderr = ssh_client.exec_command(args.command)
        output = stdout.readlines() + stderr.readlines()
    except Exception as e:
        output = []
        output.append("Error Occured {}".format(e))
    finally:
       if args.verbose:
          print("======== Result for {} ======== ".format(hostname))
          for line in output:
             print(line.strip("\n"))
       elif args.progress:
          file_name = args.incident + "_output"
          f = open(file_name,'a')
          f.write("======== Result for {} ======== ".format(hostname))
          f.write("\n")
          for line in output:
             f.write(line.strip("\n"))
             f.write("\n")


if __name__ == '__main__':

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ap = argparse.ArgumentParser()
    ap.add_argument('-f','--file',help="File name containing sever list")
    ap.add_argument('-i','--incident',help="Incident/Change No",required=True)
    ap.add_argument('-c','--command',help="Command to execute",required=True)

    group = ap.add_mutually_exclusive_group()
    group.add_argument('-v','--verbose',action="store_true",help="Display all results on screen")
    group.add_argument('-p','--progress',action="store_true",help="Show overall progress and store result in file")

    args = ap.parse_args()


    if args.file:
        try:
           f = open(args.file,'r')
           content = f.readlines()
           if args.progress:
              for line in tqdm(content,desc="Processing"):
                 each = line.strip("\n")
                 ssh_execute(each)
              print("Done")
           elif args.verbose:
              for line in content:
                 each = line.strip("\n")
                 ssh_execute(each)
        except FileNotFoundError as e:
           print("[ERROR]: File {} not found ".format(args.file))

    else:
       print("Enter the list of server names... Type 'done' at the end'")
       content = []

       while True:
          try:
             line = input()
             if line == "exit" or line == "quit":
                sys.exit(0)
             elif line == "done":
                break
          except KeyboardInterrupt as e:
                print("'cntl + c' is disabled , please type 'exit' or 'quit' to leave without save")
          except EOFError as e:
                print("Wrong Input")
          if line not in content:
                content.append(line)
       if args.progress:
          for each in tqdm(content,desc="Processing"):
             ssh_execute(each)
       else:
          for each in content:
             ssh_execute(each)

       print("Done")
