#### [Nmap Website](https://nmap.org/)

# Nmap
## Description
A utility to quickly scan large networks and single hosts for network discovery and security auditing. 

**Can be used to determine:**
* Network Hosts
* Services (application name and version)
* Operating systems (and OS versions)
* Type of packet filters/firewalls

## SERVICE/VERSION DETECTION
Version detection helps you obtain the version number for specified servers which helps in determining which exploits a server is vulnerable to.

**Can be used to determine:**
* Service protocol (e.g. FTP, SSH, Telnet, HTTP)
* Application name (e.g., ISC BIND, Apache httpd, Solaris telnetd)
* Version number
* Hostname
* Device type (e.g., printer, router)
* OS family (e.g., Windows, Linux)

#### Commands
* `-sV` (Version detection)


## SCRIPT SCAN
Allows users to use scripts to automate networking tasks. Scripts are executed in parallel to increase speed and efficiency.

**Can be used for:**
* Network discovery
* Version detection
* Vulnerability detection/exploitation

#### Commands
* `  -sC` (Performs a script scan using the default set of scripts. Shorthand for `--script=default`. All scripts are loaded, including intrusive scripts, and **should not** be run against a target network without permission)
	* Use `nmap --script "not intrusive"` to load every script except for those in the `intrusive` category.


## OUTPUT
Used to specify Nmap output methods

#### Commands
* `-oN <filespec>` (normal output) Requests that normal output be directed to the given filename. As discussed above, this differs slightly from `interactive output`.


## EXAMPLES
* `nmap -sC -sV -oN nmap/initial 10.10.16.17` (Useful for initial Nmap scans)
