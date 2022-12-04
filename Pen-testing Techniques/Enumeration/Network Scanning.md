# Network Scanning
## About Network Scanning

Network scanning is finding and identifying network information like hosts, ports, services, OS, etc., for attack vectors of a target system.

## Scanning Types
### Intrusive
Also known as active scanning, it probes the device config using a network connection with the target. It does not stop at detecting a vulnerability but also uses vulnerabilities to gain access to the system.
- Consumes more bandwidth/risks crashing the target of the scan or causing an outage.
- Used more for penetration testing than automated scanning.
### Non-intrusive
Also known as passive scanning, it analyzes indirect evidence, such as network captures, and tries to identify policy deviations or CVE matches.
- Least impact on the network and host, but less likely to identify vulnerabilities
- Use passive scanning when active scanning poses a risk to system stability

## Scanning Techniques
### Network Scanning
Scanning for hosts, IP ranges, and routes between networks to map out the structure of the target network.
### Port Scanning
Scanning for network ports to find open and capable of sending and receiving data. Port scanning will return the status of a scanned port range as closed, open, or filtered.
- **Closed Ports:** Indicates the port cannot receive any data.
- **Open Ports:** indicates the port can send and receive data. The host can accept connections to this port.
- **Filtered Ports:** indicates the port is open but does not accept connections that are not whitelisted.
### Vulnerability Scanning
Scanning for vulnerabilities to find potential attack vectors that can be exploited for access.

## Scanning Tools
### [NMAP](https://github.com/Logan-proj/Cybersecurity_Notes/blob/main/Kali%20Tools/Nmap.md) 
A utility to quickly scan large networks and single hosts for discovery and security auditing. 

**Can be used to determine:**
* Network Hosts
* Services (application name and version)
* Operating systems (and OS versions)
* Type of packet filters/firewalls

### [Nikto](https://github.com/Logan-proj/Cybersecurity_Notes/blob/main/Kali%20Tools/Nikto.md)
A web server scanner to find potential problems and security vulnerabilities
**Nikto scans will show in log files or to an IPS/IDS**

**Can be used to determine:**
-   Server and software misconfigurations
-   Default files and programs
-   Insecure files and programs
-   Outdated servers and programs
-   Pointers to lead a human tester to better manual testing
