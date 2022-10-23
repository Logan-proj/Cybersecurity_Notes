# Netcat

## Description
Netcat is a networking utility used to read and write data across network connections.

**Can be used to:**
-   Establish reverse/bind shell access to a target machine to execute shell commands.

## Reverse Shells
1) Start a Netcat listener: `nc -lvnp <port-number>`
	- `-l` - listener
	- `-v` - verbose output
	- `-n` - not to resolve host names or use DNS
	- `-p` - port specification

## Bind Shells
1) Connect to a targets open port: `nc <target-ip> <chosen-port>`
	- Telling Netcat to make an outbound connection to the target `<target-ip>` on our chosen port `<chosen-port>`.

## Stabilise Netcat Shells
Converting a non-interactive shell into an interactive shell
### Python (Linux shells)
1) Run the following commands within the shell window:
	1) `python3 -c 'import pty;pty.spawn("/bin/bash")'` - Upgrades the look of your shell prompt
	2) `export TERM=xterm` - gives access to more commands such as `clear`
2) Background the shell (`Ctrl + Z`) and enter the following command in your terminal: `stty raw -echo; fg`
	- Allows access to tab autocompletes, the arrow keys, and Ctrl + C to kill processes.
3) Perform `nc -lvnp <port-number>` again to get back into shell
- **Note:** If the shell dies, any input in your terminal will not be visible (as a result of having disabled terminal echo). Type `reset` and press enter to fix this.

### rlwrap (Windows shells)
gives us access to history, tab autocompletion, and the arrow keys upon receiving a shell.
1) On your machine, install rlwrap: `sudo apt install rlwrap`
2) Use rlwrap to invoke the nc listener: `rlwrap nc -lvnp <port>`

### Change terminal size
1) Open another terminal and run `stty -a`
2) In your reverse/bind shell, type in: 
	- `stty rows <number>` - change rows
	- `stty cols <number>` - change columns
