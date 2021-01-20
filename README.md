# multi-ssh

Script is useful to perform remote execution of commands on multiple hosts at once and store results in file for future reference .

Program comes with few options below

usage: app.py [-h] [-f FILE] -i INCIDENT -c COMMAND [-v | -p]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File name containing sever list
  -i INCIDENT, --incident INCIDENT
                        Incident/Change No
  -c COMMAND, --command COMMAND
                        Command to execute
  -v, --verbose         Display all results on screen
  -p, --progress        Show overall progress and store result in file



Authentication

Password is currently hardcoded , but to avoid doing that 

1) Password can be store in enviorment variable and read it from there

    os.envioron['my_password']
    
2) Or setup , SSH - passwordless authentication across network for user who will run command 


