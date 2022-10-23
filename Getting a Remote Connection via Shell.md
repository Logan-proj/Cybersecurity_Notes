# Getting a Remote Connection via Shell
## Definitions
- **Shell:** the interface used to interact with a Command Line environment (CLI).
- **Reverse shell:** occurs when a pentester gets a target to execute code that connects back to their computer and gives them command line access to the machine. 
	- This is achieved by setting up a listener on your machine and then sending the connection from the target.
- **Bind shell:** occurs when a pentester opens a port on a server that they can connect to and send commands. 
	- Opposite of a reverse shell; a bind shell is achieved by setting up a listener on the target machine and then sending a connection from your machine.
- **Interactive shell:** a shell that allows the pentester to interact with programs after executing them.
- **Non-Interactive shell:** a shell that limits the pentester to only use programs that require no user interaction.

## Tools
Tools used to interface with, receive, and send reverse/bind shells:
- [Netcat](https://github.com/Logan-proj/Cybersecurity_Notes/blob/main/Kali%20Tools/Netcat.md) 
- [Metasploit (multi/handler)](https://github.com/Logan-proj/Cybersecurity_Notes/blob/main/Kali%20Tools/Metasploit.md)
- [MSFvenom](https://github.com/Logan-proj/Cybersecurity_Notes/blob/main/Kali%20Tools/Metasploit.md)
- [Payloads all the Things](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md)
- [PentestMonkey Reverse Shell Cheatsheet](https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)
- [SecLists repo](https://github.com/danielmiessler/SecLists)
