#### [Documentation]()

# John The Ripper
## Description
[Hash](obsidian://open?vault=CyberSecurity&file=Cryptography%2FHashing) cracking tool that compaires hashed data against a dictionary of other hashed data to find its corresponding [plaintext](obsidian://open?vault=CyberSecurity&file=Cryptography%2FHashing) value.


**Can be used to:**
- Crack password hashes

## Syntax
`john [options] [path to file]`


## Options
`--wordlist=[path to wordlist]` - Specifies wordlist to use during the attack
`--format=[format]` - Specifies hash file format
`--show`  - Shows cracked hashes from pot file



## EXAMPLES
### Wordlist mode
Performs an attack using default or specified wordlist
- `john --list=formats | grep -iF "md5"` (Search John for format options)
- `john --wordlist=[path to wordlist] [path to file]` (Basic - will try to detect the type of hash given and try cracking using the worklist provided)
- `john --format=[format] --wordlist=[path to wordlist] [path to file]` (Attempts to crack a specific hash type using wordlist)
- `john --show --format=[format] [path to file]` (Show cracked password)


### Single Crack
Performs cracking, assuming the password is derived from the user: login name, full name, username, or other personal info. 
- Hash data used in single crack mode must include the username (or other names) at the beginning of the hash separated by a colon ":"
	- Example: "mike:1efee03cdcb96d90ad48ccc7b8666033"
- `john --single --format=[format] [path to file]` - Performs attack in single crack mode


### Cracking Hashes from /etc/shadow
**Unshadowing passwords using John requires two files:**
1) Entire /etc/passwd file (or line for the target machine, example: `root:x:0:0::/root:/bin/bash`)
2) Entire /etc/shadow file (or line from the target machine, example: `root:$6$2nwjN454g.dv4HN/$m9Z/r2xVfweYVkrr.v5Ft8Ws3/YYksfNwq96UL1FX0OJjY1L6l.DS3KEVsZ9rOVLB/ldTeEL/OIhJZ4GMFMGA0:18576::::::`)

**The process for unshadowing a password using John is as follows:**
1) `unshadow [path to passwd] [path to shadow] > [output file].txt` - formats file for John to better understand the data.
	- `unshadow` - Tells John to perform unshadow process
	- `[path to passwd]` - Location of /etc/passwd file taken from the target machine
	- `[path to shadow]` - Location of /etc/shadow file you've taken from the target machine.
	- `>` - Tells John to write output to a new file
	- `[output file].txt` - Specifies output file name
2) `john --format=sha512crypt unshadowed.txt` - Perform cracking from newly created unshadow file
	- `--format=sha512crypt` - Specifies file format
	- `unshadowed.txt` - Specifies the file to crack


### Cracking Password Protected Zip Files
zip2john is used to convert a .zip file into a hash file format that John can crack.
1) `zip2john [path to zip file] > [output file].txt` - Performs zip2john conversion
	- `zip2john` - Tells john to perform conversion on the protected zip file
	- `[path to zip file]` - Specifies path to zip file
	- `>` - Tells John to write output to a new file
	- `[output file].txt` - Specifies output file name
2) `john zip_hash.txt` - After converting the file into a hash, crack it using John


### Cracking a Password-Protected RAR Archive
rar2john is used to convert RAR archive files created by the Winrar archive manager into a hash format that John can crack.
1) `rar2john [rar file] > [output file].txt` - Performs zip2john conversion
	- `rar2john` - Tells john to perform conversion on the RAR archive file
	- `[rar file]` - Specifies path to RAR file
	- `>` - Tells John to write output to a new file
	- `[output file].txt` - Specifies output file name
2) `john rar_hash.txt` - After converting the file into a hash, crack it using John


### Cracking SSH Keys
ssh2john is used to crack the password to set up SSH keys by converting the id_rsa private key that you use to log in to the SSH session into a hash format that John can crack.
1) `ssh2john [id_rsa private key file] > [output file].txt` - Performs ssh2john conversion
	- `ssh2john` - Tells john to perform conversion on id_rsa file
	- `[id_rsa private key file]` - Specifies path to id_rsa file
	- `>` - Tells John to write output to a new file
	- `[output file].txt` - Specifies output file name
2) `john id_rsa_hash.txt` - After converting the file into a hash, crack it using John