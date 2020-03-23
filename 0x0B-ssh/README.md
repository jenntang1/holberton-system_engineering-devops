# Overview #
The program codes contained in this directory is to help with learning and understanding SSH.  

## General ##
0. What is a server?  
A server could be a physical computer, virtual machine or container that provides data or services to clients through a network.  

1. Where servers usually live?  
Physical servers live in a datacenter that could physically reside anywhere in the world.  Virtual server/machine is a computer file that resides on an actual computer.  

2. What is SSH?  
SSH stands for Secure Shell Protocol and is a secure protocol used to connect remotely to Linux servers.  

3. How to create an SSH RSA key pair?  
In order to create a SSH RSA key pair, run the following command.  
```bash
ssh-keygen -t rsa
```

4. How to connect to a remote host using an SSH RSA key pair?  
In order to connect to a remote host after public SSH key is copied to the server, run the following commands.

```bash
ssh remotehost
```

OR

```bash
ssh username@remotehost
```

5. The advantage of using #!/usr/bin/env bash instead of /bin/bash?  
Both specifies the interpreter to use. The former uses env to find bash in PATH which is a security risk because malware would have access to the user's PATH. The latter assumes bash is always in bin but that's not always the case.  

## Resources ##
0. Man Pages  
a. ssh  
b. ssh-keygen  
c. env  

1. Server (computing)  
https://en.wikipedia.org/wiki/Server\_%28computing%29#Hardware\_requirement  

2. What is a Server.  
https://www.youtube.com/watch?v=B1ANfsDyjeA  

3. SSH Essentials: Working with SSH Servers, Clients, and Keys  
https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys  

4. SSH Config File  
https://www.ssh.com/ssh/config  

5. Public Key authentication for SSH  
https://www.ssh.com/ssh/public-key-authentication  

6. How Secure Shell Works (SSH) - Computerphile  
https://www.youtube.com/watch?v=ORcvSkgdA58  

7. SSH Crash Course | With Some DevOps  
https://www.youtube.com/watch?v=hQWRp-FdTpc  

## Contributor ##
Jennifer Tang  
