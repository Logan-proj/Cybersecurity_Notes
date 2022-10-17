#### [Documentation](https://hashcat.net/hashcat/)

# Hashcat
## Description
Hashcat is a password cracker/ recovery tool.


**Can be used to:**
* Crack password hashes


## Core Attack Modes
`-a 0` (Dictionary Attack Mode: tries all words within a wordlist)


## Options
`-m [hash type]` (Specifies hash type)
`-o [filename]` (Specifies output filename)


## EXAMPLES
* `hashcat hashfile.txt` (check for matching hash modes)
	* Runs hashcat scan to detect possible matching hash modes based on the structure of your input hash. 
	* Pentesters can use these hash modes to attack the hash file along with a wordlist
* `hashcat -m 3200 -a 0 -o cracked.txt hashfile.txt /usr/share/wordlists/rockyou.txt` (decrypt using bycript mode)
	* `-m 3200` - Specify the hash type
	* `-a 0` - Specify attack type
	* `-o cracked.txt` - Output result into new text document "cracked" 
	* `hashfile.txt` - Specify the hash file being cracked
	* `/usr/share/wordlists/rockyou.txt` - Specify wordlist
- `hashcat hashfile.txt -m [hash-number] --show` (Shows previously cracked hash)
	- Use when you get the message "INFO: All hashes found in potfile! Use --show to display them."