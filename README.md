# multi-ssh

Script is useful to perform remote execution of commands on multiple hosts at once and store results in file for future reference .

Program comes with few options below

![ScreenShot](https://raw.github.com/{Rohitkuru}/{multi-ssh}/{main}/{multissh_help.png})



Authentication

Password is currently hardcoded , but to avoid doing that 

1) Password can be store in enviorment variable and read it from there

    os.envioron['my_password']
    
2) Or setup , SSH - passwordless authentication across network for user who will run command 


# how to install on linux.

1) python -m venv env
2) cd env
3) git clone repository
4) source bin/activate
5) pip install -r requirements.txt
6) python multi-ssh.py -i <incident_no> -f <file_name> -v 
7) OR
8) python multi-ssh.py -i <incident_no> -f <file_name> -p
9)  -p is for progress

