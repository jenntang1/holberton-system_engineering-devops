# Overview #
The program codes contained in this directory is to help with learning and understanding computer networks.  

## General ##
0. OSI Model  
a. What it is?  OSI Model stands for Open Systems Interconnection and it is how applications communicate over a network.  
b. How many layers it has?  In total, there are seven layers that are organzied from lowest to highest.  
c. How it is organized?  The lowest level aka layer 1 is for transmission on physical layers with electrical impulse, light or radio signal.  Layer 2 is for handling data moving in and out of a physical link in a network and handles problems that occurred as as a result of bit transmission errors.  Layer 3 is for handling data moving in and out of other networks through packaging data with correct network addresses, selecting the correct network routs and forwarding the data.  Layer 4 is for handling data moving across a network.  Layer 5 is for coordination and termination of conversations between applications.  Layer 6 is for translating data for the applicationn and it handles encrytion and decryption for the application.  Layer 7 is for interaction between the application and the user.  

1. What is a LAN?  LAN stands for local area network.  
a. Typical usage?  LAN is a type of computer network that connects network devices to each other, sharing a command communications line.  
b. Typical geographical size?  LAN covers a short distance, usually in one dwelling such as school or home.  

2. What is a WAN?  WAN stands for wide area network.  
a. Typical usage?  WAN is a type of computer network that also connects network devices to each other.  
b. Typical geographical size?  WAN covers a longer distance than LAN.  In fact, the internet is the largest WAN!  

3. What is the Internet?  Internet is a global system of interconnected computer networks.  
a. What is an IP address?  IP address stands for Internet Protocol address and it's an unique id for every device connected to the Internet.  
b. What are the 2 types of IP address?  IPv4 uses 32-bit addresses which has a limit of 4,294,967,296 IP addresses.  IPv5 uses 128-bit addresses.  
c. What is localhost?  Localhost means "this computer" which is the local device connected to the network.  
d. What is a subnet?  Subnet is a part of a larger network and shares the same IP address.  
e. Why IPv6 was created?  IPv6 was created to handle the increasing demand of IP addresses.  

4. TCP/UDP..
a. What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)?  TCP stands for Transmission Control Protocol and UDP stands for User Datagram Protocol.  They both send bits of data in a packet over the Internet from one IP address to another.  
b. What is the main difference between TCP and UDP?  TCP sends ordered packets and error checks them by having the recipient send a response to the sender that it received the packet.  If not, the sender will try to resend the packet.  UDP sends packets quicker because it doesn't handle error checks.  
c. What is a port?  Port is a number that serves as a communication endpoint between two devices.  
d. Memorize SSH, HTTP and HTTPS port numbers?  The most used ports are 22 for SSH, 80 for HTTP and 443 for HTTPS.  
e. What tool/protocol is often used to check if a device is connected to a network?  In Linux, the netstat command displays various network information including network connections.  

## Resources ##
0. Man pages  
a. netstat  
b. ping  

1. OSI model (Open Systems Interconnection)  
https://searchnetworking.techtarget.com/definition/OSI  

2. Introduction to LANs, WANs, and Other Kinds of Area Networks  
https://www.lifewire.com/lans-wans-and-other-area-networks-817376  

3. local area network (LAN)  
https://searchnetworking.techtarget.com/definition/local-area-network-LAN  

4. WAN (Wide Area Network)  
https://searchnetworking.techtarget.com/definition/WAN-wide-area-network  

5. Internet  
https://en.wikipedia.org/wiki/Internet  

6. What is a MAC Address?  
https://whatismyipaddress.com/mac-address  

7. IP Addresses Explained  
https://www.bleepingcomputer.com/tutorials/ip-addresses-explained/  

8. What is the difference between public and private IP address?  
https://www.iplocation.net/public-vs-private-ip-address  

9. What is The Difference Between IPv6 and IPv4?  
https://www.webopedia.com/DidYouKnow/Internet/ipv6\_ipv4\_difference.html  

10. localhost  
https://en.wikipedia.org/wiki/Localhost  

11. What’s the Difference Between TCP and UDP?  
https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/  

12. List of TCP and UDP port numbers  
https://en.wikipedia.org/wiki/List\_of\_TCP\_and\_UDP\_port\_numbers  

13. ping (networking utility)  
https://en.wikipedia.org/wiki/Ping\_%28networking\_utility%29  

14. Handling positional parameters  
https://wiki.bash-hackers.org/scripting/posparams  

## Contributor ##
Jennifer Tang  
