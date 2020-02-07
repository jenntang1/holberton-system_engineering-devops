# Overview #
The program codes contained in this directory is to help learn and understand Bash, specifically loops, conditions and parsing.  

# General #
0. How to create SSH keys?  
In order to create a SSH key pair, run the following command.  
```bash
ssh-keygen -t rsa
```

1. What is the advantage of using #!/usr/bin/env bash over #!/bin/bash?  
Both specifies the interpreter to use.  The former uses env to find bash in PATH which is a security risk because malware would have access to the user's PATH.  The latter assumes bash is always in bin but that's not always the case.  

2. How to use while, until and for loops?  

Using while:
```bash
count=1
while [ $count -le 5 ]
do
	echo "Uploading $count second"
	count=$(( $count + 1 ))
done
```

Using until:
```bash
until upload &> /dev/null
do
	echo "Uploading..."
	sleep 1
done
```

Using for:
```bash
for count in {1..5}
do
	echo "Uploading $count second"
done
```

3. How to use if, else, elif and case condition statements?  
```bash
read -p "Enter a value:" n

if [ $n -eq 5 ]
then
	echo "Value is 5"
elif [ $n -eq 10 ]
then
	echo "Value is 10"
else
	echo "Value is not equal to 5 or 10"
fi
```

4. How to use the cut command?  
The following is an example using the cut command to display the Unix login names of all users in the system.  

```bash
cut -d: -f1 /etc/passwd
```

5. What are files and other comparison operators, and how to use them?  
The following are a few files and comparison operators.  
-a file checks if file exists  
-d file checks if file exists and if it's a directory  
-f file checks if file exists and if it's a regular file  
-h file checks if file exists and if it's a symbolic link  
-eq checks if integers are equal to each other  
-ne checks if integers are not equal to each other  
== checks if strings are the same  
!= checks if strings are not equal  

# Resources #
0. Man pages of:  
    a. env  
	b. cut  
	c. for  
	d. while  
	e. until  
	f. if  

1. Shellcheck  
https://github.com/koalaman/shellcheck  

2. How do I set up SSH authentication keys?  
https://askubuntu.com/questions/61557/how-do-i-set-up-ssh-authentication-keys  

3. What is a data center?  
https://www.youtube.com/watch?v=iuqXFC\_qIvA&feature=youtu.be&t=46  

4. Bash Guide for Beginners  
http://tldp.org/LDP/Bash-Beginners-Guide/html/sect\_09\_01.html  

5. Advanced Bash-Scripting Guide:  
http://tldp.org/LDP/abs/html/ops.html  
http://tldp.org/LDP/abs/html/comparison-ops.html  
http://tldp.org/LDP/abs/html/fto.html  

6. Make Linux/Unix Script Portable With #!/usr/bin/env As a Shebang  
https://www.cyberciti.biz/tips/finding-bash-perl-python-portably-using-env.html  

7. SSH login without password  
http://linuxproblem.org/art\_9.html  

8. Easiest way to copy ssh keys to another machine?  
https://askubuntu.com/questions/4830/easiest-way-to-copy-ssh-keys-to-another-machine/4833#4833  

9. What is the difference if I start bash with "/bin/bash" or "/usr/bin/env bash"?  
https://unix.stackexchange.com/questions/206350/what-is-the-difference-if-i-start-bash-with-bin-bash-or-usr-bin-env-bash/206366  

10. Why is #!/usr/bin/env bash superior to #!/bin/bash?  
https://stackoverflow.com/questions/21612980/why-is-usr-bin-env-bash-superior-to-bin-bash  

# Contributor #
Jennifer Tang  
