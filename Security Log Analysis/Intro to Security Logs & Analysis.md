# Intro to Security Logs & Analysis

## Log Files & Thier Uses
- Log files record events and how users and software interact with the system. 
- Security logs provide an audit trail of actions performed on the system and warning of suspicious activity. In addition, they can help answer What, When, Where, Who, and Outcome questions.
- It is crucial that log configuration and files be made tamper-proof.

## Information Log Files Can Contain
- Timestamp of events
- Service or Application name the log file is generated from
- Event details, including type of event failure and network/system information (i.e, Invalid user authentication from IP 10.0.0.1, port 1234)

## Log File Locations
- **Windows** log files can be located within their **Event Viewer** application. A central place to view different types of log files, including:
	- Application logs for documenting when services or applications are started/stopped and why.
	- Security logs for documenting when a user accessed the system and what credentials were used.
	- Setup logs for documenting events related to system maintenance and windows updates.
	- System logs for documenting changes to the system, including power states and connected devices.
- **Linux (Ubuntu/Debian)** log files can be located within the `/var/log` directory and viewed with the `ls` command. Linux log files can contain the following:
	- Authentication logs (auth.log): documents all login attempts (remote & physical).
	- Package Management (dpkg.log): documents events related to installing new software.
	- System logs (syslog): documents events related to background processes such as crontabs and other automatic services.
	- Kernel (kern.log): documents events related to changes with the OS kernel, output from networking or physical devices.

## Linux Commands for Log Analysis
### Grep
#### About
`grep <option> <file>` ; Linux search command for finding patterns within a file.
#### Options
##### Pattern syntax
- `-E, --extended-regexp` ; Performs a regular expression search by determining what patterns to search. For example, you can search for lines that contain either "EST" or "Eastern Standard Time."
	- Example: `grep -e "EST|Eastern Standard Time" log.txt`
##### Matching Control
- `-i, --ignore-case` ; Ignores match case differences. "helloworld" and "HELLOWORLD" will return the same results.
	- Example: `grep -i "helloworld" log.txt`
##### File and Directory Selection
- `-r, --recursive` ; Searches all files under each directory for search value.
	- Example: `grep -r "helloworld" mydirectory`
