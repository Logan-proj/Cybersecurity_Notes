#### [Documentation](https://nmap.org/)
# Nmap
## Description
A utility to quickly scan large networks and single hosts for discovery and security auditing. 

**Can be used to determine:**
* Network Hosts
* Services (application name and version)
* Operating systems (and OS versions)
* Type of packet filters/firewalls

## Scan Techniques

#### Commands
 -  `-sS` ; TCP SYN Scan. The default scan option performs a scan without completing the TCP three-way handshake allowing for a quick and stealthy scan of thousands of ports.
	 - `nmap -sS <IP Address>`
- `-sN` ; Scans host without checking for port services
	- `nmap -sN <IP Address>`


## ## Service & Version Detection
Version detection helps you obtain the version number for specified servers which helps in determining which exploits a server is vulnerable to.

**Can be used to determine:**
* Service protocol (e.g. FTP, SSH, Telnet, HTTP)
* Application name (e.g., ISC BIND, Apache HTTP, Solaris telnet)
* Version number
* Hostname
* Device type (e.g., printer, router)
* OS family (e.g., Windows, Linux)

#### Commands
* `-sV` ; Enables version detection 


## Script Scan
Allows users to use scripts to automate networking tasks. Scripts are executed in parallel to increase speed and efficiency.

**Can be used for:**
* Network discovery
* Version detection
* Vulnerability detection/exploitation

#### Commands
* `-sC` ; (Performs a script scan using the default set of scripts. Shorthand for `--script=default`. All scripts are loaded, including intrusive scripts, and **should not** be run against a target network without permission)
	* Use `nmap --script "not intrusive"` to load every script except for those in the `intrusive` category.

## OS Detection
OS detection is used to find the operating system for target ports by sending TCP and UDP packets to the target and compares the results to a database of over 2600 known OS fingerprints.

#### Commands
- `-O` ; Enables OS detection
	- `nmap -O <IP Address>`


## OUTPUT
Used to specify Nmap output methods

#### Commands
* `-oN <file name>` (standard output) Requests that standard output be directed to the given filename. As discussed above, this differs slightly from `interactive output`.


## Examples
#### Initial NMAP Scans
* `nmap -sC -sV -oN nmap_initial <target ip>
	* `-sC` - runs a basic script scan on the target
	* `-sV` - detects the version
	* `-oN nmap_initial` - outputs results into file named *nmap/initial*
	* `<target ip>` - target IP 
#### SMB Enumeration
- `nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse <target ip>`
	- `-p` - specifies what port to scan
	- `--script=smb-enum-shares.nse,smb-enum-users.nse` - runs smb script for enumerating shares
#### NFS Scan
- `nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.127.239`
	- `-p` - specifies what port to scan
	- `--script=nfs-ls,nfs-statfs,nfs-showmount` - runs nfs scan
