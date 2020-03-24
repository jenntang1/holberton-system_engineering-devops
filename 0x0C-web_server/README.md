# Overview #
The program codes contained in this directory are used to set up a web server.  

## Overview ##
0. What is the main role of a web server?  
The main role of a web servier is to serve static content.  

1. What is a child process?  
A child process is a process created from another process called a parent process.  In terms of web infrastructure, programs such as Apache, creates a child process if the number of web requests exceeds the maximum allowed.  Then, if the maximum allowed children processes is exceeded, another child process will be created.  The following command shows all the current running processes in tree format.  

```bash
ps axf
```

2. Why web servers usually have a parent process and child processes?  
Web servers usually have a parent process and child processesto dynamically change the number of child process to accommodate the volume of requests to be processed.  

3. What are the main HTTP requests?  
The main HTTP requests are 

4. What DNS stands for?  
DNA stands for Domain Name System.  

5. What is DNS main role?  
The main role of DNS to translate domain name into IP address.  

6. DNS Record Types: A, CNAME, TXT, MX?  
A stands for Address and only takes an IP address as its value.  
CNAME stands for Canonical Name and maps an alias to another alias, therefore, translates itself to a domain.  
TXT stands for text record and doesn't impact domain but tells other domains about your domain.  
MX stands for Mail eXchange and it helps route emails.  

## Resources ##
0. Man Pages  
a. scp  
b. curl  

1. Web server  
https://www.youtube.com/watch?v=AZg4uJkEa-4&feature=youtu.be&hd=1  

2. How the Web works  
https://developer.mozilla.org/en-US/docs/Learn/Getting\_started\_with\_the\_web/How\_the\_Web\_works  

3. Nginx  
https://en.wikipedia.org/wiki/Nginx  

4. How To Set Up Nginx Server Blocks (Virtual Hosts) on Ubuntu 16.04  
https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04  

5. Root domain and subdomain – the differences  
https://landingi.com/knowledge-base/root-domain-subdomain-differences  

6. HTTP - Methods  
https://www.tutorialspoint.com/http/http\_methods.htm  

7. Redirects  
https://moz.com/learn/seo/redirection  

8. HTTP 404  
https://en.wikipedia.org/wiki/HTTP\_404  

9. View log files in Ubuntu Linux  
https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/  

10. Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content  
https://tools.ietf.org/html/rfc7231  

11. Hypertext Transfer Protocol Version 2 (HTTP/2)  
https://tools.ietf.org/html/rfc7540  

## Contributor ##
Jennifer Tang  
