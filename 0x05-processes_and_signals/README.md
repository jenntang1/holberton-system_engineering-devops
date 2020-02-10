# Overview #
The program codes contained in this directory is to help learn and understand Bash, specifically processes and signals.  

# General #
0. What is a PID?  
PID is an identification number assigned to each process that's created.  

1. What is a process?  
Process is an executing/running instance of a program.  It's assigned a non-negative integer as a PID.  

2. How to find a process’ PID?  
Use the ps command to find a process' PID.  

3. How to kill a process?  
Use the kill command to terminate a process without having to log out or reboot the computer.  

4. What is a signal?  
Signal is a software interruption that changes the current running process.  

5. What are the 2 signals that cannot be ignored?  
SIGKILL and SIGSTOP cannot be ignored.  

# Resources #
0. Man pages of:  
    a. ps  
	b. pgrep  
	c. pkill  
	d. kill  
	e. exit  
	f. trap  

1. PID Definition  
http://www.linfo.org/pid.html  

2. Linux Processes – Environment extern, environ, getenv, setenv  
https://www.thegeekstuff.com/2012/03/linux-processes-environment/  

3. Linux Signals Fundamentals – Part I  
https://www.thegeekstuff.com/2012/03/linux-signals-fundamentals/  

4. $BASHPID And $$ differ in some cases  
https://unix.stackexchange.com/questions/62231/bashpid-and-differ-in-some-cases  

5. Shellcheck  
https://github.com/koalaman/shellcheck/wiki/Ignore  

6. Bash check if process is running or not on Linux / Unix  
https://www.cyberciti.biz/faq/bash-check-if-process-is-running-or-notonlinuxunix/  

7. Linux Signals  
https://www.computerhope.com/unix/signals.htm  

# Contributor #
Jennifer Tang  
