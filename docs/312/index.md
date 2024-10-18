---
sidebar_position: 0
title: CPIS-312
---

# [CPIS-312 Information systems strategies and policies](https://fcit.kau.edu.sa/aims/runReportAPI2.php?REP_ID=3&FL_TYPE=pdf&CLG_ID=1&PRA_STR=(PARAM1:18)%7C(PARAM2:2)%7C(PARAM3:3)%7C(PARAM4:BINDER)%7C(PARAM6:CPIS-312)%7C(PARAM5:0)%7C(PARAM7:)%7C(P_DESFORMAT:PDF)%7C(P_RDF_FILENAME:BINDER)%7C(P_OUTPUT_FILENAME:Syllabus))

## Module 5 Network Protocols

| **OSI Model**            | **TCP/IP Model**         | **Description**                                                                 |
|--------------------------|--------------------------|---------------------------------------------------------------------------------|
| 7. Application Layer      | 4. Application Layer     | Handles network processes and user applications (e.g., HTTP, FTP, SMTP).        |
| 6. Presentation Layer     | -                        | Manages data format translation, encryption, and compression.                   |
| 5. Session Layer          | -                        | Manages sessions and controls dialogues between computers.                      |
| 4. Transport Layer        | 3. Transport Layer       | Ensures end-to-end communication, reliability (e.g., TCP, UDP).                 |
| 3. Network Layer          | 2. Internet Layer        | Routes data between devices across different networks (e.g., IP).               |
| 2. Data Link Layer        | 1. Network Access Layer  | Handles physical addressing and error detection for data transmission.          |
| 1. Physical Layer         | 1. Network Access Layer  | Manages the physical connection, electrical signals, and hardware interaction.   |

### OSI Model

|-| **OSI Layer**            | **Function**                                                                                          | **Example Protocols/Technologies**             |
|-|--------------------------|-------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| 7 | Application      | Provides network services directly to user applications, handling high-level APIs and application protocols. | HTTP, FTP, SMTP, DNS                          |
| 6 | Presentation     | Ensures data is in a usable format, manages encryption, decryption, compression, and data translation.  | SSL/TLS, JPEG, GIF, MPEG                      |
| 5 | Session          | Manages sessions between applications, coordinating communication and maintaining connections.         | NetBIOS, RPC                                  |
| 4 | Transport        | Provides reliable or unreliable delivery, error detection, and flow control for end-to-end communication. | TCP, UDP                                      |
| 3 | Network          | Determines the best path for data, handles logical addressing and packet forwarding.                   | IP, ICMP, OSPF, RIP                           |
| 2 | Data Link        | Provides physical addressing (MAC), error detection, and frames for the network.                       | Ethernet, PPP, Wi-Fi, ARP                     |
| 1 | Physical         | Deals with the physical transmission of raw bitstreams over a medium (cables, radio waves).            | Ethernet cables, Fiber optics, 802.11 (Wi-Fi) |


|-| OSI Model Layer | Description |
|-|-|-|
| 7 | Application | Contains protocols used for process-to-process communication |
| 6 | Presentation | Provides presentation of the data transferred between application layer services |
| 5 | Transport | Provides services to the presentation layer to organize its dialogue and manage data exchange |
| 4 | Session | Defines services to segment, transfer, and reassemble the data for individual communications between the end devices |
| 3 | Network | Provides services to exchange the individual pieces of data over the network |
| 2 | Data Link | Describe methods for exchanging data frames between devices over a common media |
| 1 | Physical | Describe the mechanical, eletrical, functional, and procedural means to activate, maintain, and deactivate physical connections for a big transmission between devices |

### TCP/IP Model

|-| **TCP/IP Layer**          | **Function**                                                                                           | **Example Protocols/Technologies**             |
|-|---------------------------|--------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| 4 | Application       | Combines the functionalities of OSI's Application, Presentation, and Session layers, handling high-level protocols for data exchange. | HTTP, FTP, SMTP, DNS, SNMP                   |
| 3 | Transport         | Manages end-to-end communication, including data segmentation, flow control, and error handling.       | TCP, UDP                                      |
| 2 | Internet          | Responsible for logical addressing, packet routing, and forwarding across multiple networks.            | IP, ICMP, ARP, OSPF, BGP                      |
| 1 | Network Access    | Encompasses OSI's Physical and Data Link layers, handling hardware addressing and physical data transmission. | Ethernet, Wi-Fi, ARP, PPP, Frame Relay        |

|-| TCP/IP Model Layer | Description |
|-|-|-|
| 4 | Application | Represents data to the user, plus encoding and dialog control |
| 3 | Transport | Supports communication between various devices across diverse networks |
| 2 | Internet | Determines best path through network |
| 1 | Network Access | Controls the hardware devices and media that make up the network |

### Encapsulation

|-|-|
|-|-|
| segmentation | data broken into a series of smaller pieces and sent over the network. |
| multiplexing | increased speed is gained because many data conversations can happen at the same time on the network. |
| encapsulation | as data is passed down the protocol stack to be sent, different information is added by each layer. |
| protocol data unit | the form that data takes at different layer |
| de-encapsulation | the process used by a receiving device to remove one or more of the protocol headers. |

=====================

## Module 13 Attackers and Their Tools

Indicators of Attack are signs of potential malicious activity or tactics that may indicate an ongoing or future attack, emphasizing behavior and intent, such as unusual network activity or suspicious access patterns.

Indicators of Compromise are evidence that an attack has already occurred, such as malware signatures, compromised files, or logs of unauthorized access.

While Indicators of Attack help in detecting and preventing attacks in real-time, Indicators of Compromise are used for forensic analysis and post-incident investigation.

### Categories of common network penetration testing tools

| Categories of Tools | Description |-|
|-|-|-|
| Password crackers | crack or recover the password. | John the Ripper, Ophcrack |
| Wireless hacking tools | intentionally hack into a wireless network to detect security vulnerabilities. | Aircrack-ng, Kismet |
| Network scanning and hacking tools | probe network devices, servers, and hosts for open TCP or UDP ports.  | Nmap, SuperScan |
| Packet crafting tools | probe and test a firewall’s robustness.  | Hping, Scapy
| Packet sniffers | capture and analyze packets within traditional Ethernet LANs or WLANs.  | Wireshark, Tcpdump |
| Rootkit detectors | a directory and file integrity checker used by white hats to detect installed root kits.  | AIDE, Netfilter |
| Fuzzers to search vulnerabilities | discover computer systems’ security vulnerabilities.  | Skipfish, Wapiti |
| Forensic tools | sniff out any trace of evidence existing in a particular computer system.  | Sleuth Kit, Helix |
| Debuggers | reverse engineer binary files when writing exploits and used by white hats when analyzing malware. | GDB, WinDbg |
| Hacking operating systems | preloaded with tools and technologies optimized for hacking.  | Kali Linux, SELinux |
| Encryption tools | use algorithm schemes to encode the data to prevent unauthorized access to the data.  | VeraCrypt, CipherShed |
| Vulnerability exploitation tools | identify whether a remote host is vulnerable to a security attack.  | Metasploit, Core Impact |
| Vulnerability scanners | scan a network or system to identify open ports. They can also be used to scan for known vulnerabilities and scan VMs, BYOD devices, and client databases. | Nipper, Securia PSI |

### Attacks

| Category of Attack | Description |
|-|-|
| Eavesdropping attack | An eavesdropping attack is when a threat actor captures and listens to network traffic. This is also called as sniffing or snooping. |
| Data modification attack | Data modification attacks occur when a threat actor has captured enterprise traffic and has altered the data in the packets without the knowledge of the sender or receiver. |
| IP address spoofing attack | An IP address spoofing attack is when a threat actor constructs an IP packet that appears to originate from a valid address inside the corporate intranet. |
| Password-based attacks | Password-based attacks occur when a threat actor obtains the credentials for a valid user account. |
| Denial-of-service attack | A Denial-of-service attack prevents normal use of a computer or network by valid users. This attack can block traffic, which results in a loss of access to network resources. |
| Man-in-the-middle attack | A Man-in-the-middle attack attack occurs when threat actors have positioned themselves between a source and destination. |
| Compromised key attack | A compromised-key attack occurs when a threat actor obtains a secret key. A compromised key can be used to gain access to a secured communication without the sender or receiver. |
| Sniffer attack | A sniffer is an application or device that can read, monitor, and capture network data exchanges and read network packets. If the packets are not encrypted, a sniffer provides a full view of the data inside the packet. |

====================================

### Trojan Horse

| Type of Trojan Horse | Description |
|-|-|
| Remote-access | Enables unauthorized remote access. |
| Data-sending | Provides the threat actor with sensitive data, such as passwords. |
| Destructive | Corrupts or deletes files. |
| Proxy | Uses the victim's computer as the source device to launch attacks and perform other illegal activities. |
| FTP | Enables unauthorized file transfer services on end devices. |
| Security software disabler | Stops antivirus programs or firewalls from functioning. |
| Denial of Service | Slows or halts network activity. |
| Keylogger | Actively attempts to steal confidential information, such as credit card numbers, by recording keystrokes entered into a web form. |

### Malware

| Type of Malware | Description |
|-|-|
| Scareware | Includes scam software which uses social engineering to shock or induce anxiety by creating the perception of a threat. It is generally directed at an unsuspecting user and attempts to persuade the user to infect a computer by taking action to address the bogus threat. |
| Phishing | Attempts to convince people to divulge sensitive information. Examples include receiving an email from their bank asking users to divulge their account and PIN numbers. |
| Rootkits | Installed on a compromised system. After it is installed, it continues to hide its intrusion and provide privileged access to the threat actor. |
| Spyware | gather information about a user and send the information to another entity without the user’s consent. Spyware can be a system monitor, Trojan horse, Adware, tracking cookies, and key loggers. |
| Adware | Displays annoying pop-ups to generate revenue for its author. The malware may analyze user interests by tracking the websites visited. It can then send pop-up advertising pertinent to those sites. |

### Exploitation

| Technique | Description |-|
|-|-|-|
| Perform an information query of a target | The threat actor is looking for initial information about a target. | Google search, organizations website, whois |
| Initiate a ping sweep of the target network | The information query usually reveals the target’s network address. The threat actor can now initiate a ping sweep to determine which IP addresses are active. |-|
| Port scanner initiate a port scan of active IP addresses | This is used to determine which ports or services are available. | Nmap, SuperScan, Angry IP Scanner, NetScanTools. |
| Vulnerability scanners | This is to query the identified ports to determine the type and version of the application and operating system that is running on the host. | Nipper, Secuna PSI, Core Impact, Nessus v6, SAINT, Open VAS. |
| Exploitation tools | The threat actor now attempts to discover vulnerable services that can be exploited | Metasploit, Core Impact, Sqlmap, Social Engineer Toolkit, Netsparker. |

### Attacks

|-|-|
|-|-|
| Access attacks | exploit known vulnerabilities in authentication services, FTP services, and web services to gain entry into web accounts, confidential databases, and other sensitive information. |
| Password Attacks | The threat actor attempts to discover critical system passwords using a variety of password cracking tools. |
| Spoofing Attacks | The threat actor device attempts to pose as another device by falsifying data. |

### Social engineering

| Social Engineering Attack | Description |
|-|-|
| Pretexting | A threat actor pretends to need personal or financial data to confirm the identity of the recipient. |
| Phishing | A threat actor sends fraudulent email which is disguised as being from a legitimate, trusted source to trick the recipient into installing malware on their device, or to share personal or financial information. |
| Spear phishing |A threat actor creates a targeted phishing attack tailored for a specific individual or organization. |
| Spam | Also known as junk mail, this is unsolicited email which often contains harmful links, malware, or deceptive content. |
| Something for Something | Sometimes called “Quid pro quo”, this is when a threat actor requests personal information from a party in exchange for something such as a gift. |
| Baiting | A threat actor leaves a malware infected flash drive in a public location. A victim finds the drive and unsuspectingly inserts it into their laptop, unintentionally installing malware. |
| Impersonation | In this type of attack, a threat actor pretends to be someone else to gain the trust of a victim. |
| Tailgating | This is where a threat actor quickly follows an authorized person into a secure location to gain access to a secure area. |
| Shoulder surfing | This is where a threat actor inconspicuously looks over someone’s shoulder to steal their passwords or other information. |
| Dumpster diving | This is where a threat actor rummages through trash bins to discover confidential documents. |

### Evasion

| Evasion Method | Description |
|-|-|
| Encryption and tunneling | This evasion technique uses tunneling to hide, or encryption to scramble, malware files. This makes it difficult for many security detection techniques to detect and identify the malware. Tunneling can mean hiding stolen data inside of legitimate packets. |
| Resource exhaustion | This evasion technique makes the target host too busy to properly use security detection techniques. |
| Traffic fragmentation | This evasion technique splits a malicious payload into smaller packets to bypass network security detection. After the fragmented packets bypass the security detection system, the malware is reassembled and may begin sending sensitive data out of the network. |
| Protocol-level misinterpretation | This evasion technique occurs when network defenses do not properly handle features of a PDU like a checksum or TTL value. This can trick a firewall into ignoring packets that it should check. |
| Traffic substitution | In this evasion technique, the threat actor attempts to trick an IPS by obfuscating the data in the payload. This is done by encoding it in a different format. For example, the threat actor could use encoded traffic in Unicode instead of ASCII. The IPS does not recognize the true meaning of the data, but the target end system can read the data. |
| Traffic insertion | Similar to traffic substitution, but the threat actor inserts extra bytes of data in a malicious sequence of data. The IPS rules miss the malicious data, accepting the full sequence of data. |
| Pivoting | This technique assumes the threat actor has compromised an inside host and wants to expand their access further into the compromised network. An example is a threat actor who has gained access to the administrator password on a compromised host and is attempting to login to another host using the same credentials. |
| Rootkits | A rootkit is a complex attacker tool used by experienced threat actors. It integrates with the lowest levels of the operating system. When a program attempts to list files, processes, or network connections, the rootkit presents a sanitized version of the output, eliminating any incriminating output. The goal of the rootkit is to completely hide the activities of the attacker on the local system. |
| Proxies | Network traffic can be redirected through intermediate systems in order to hide the ultimate destination for stolen data. In this way, known command-and-control not be blocked by an enterprise because the proxy destination appears benign. Additionally, if data is being stolen, the destination for the stolen data can be distributed among many proxies, thus not drawing attention to the fact that a single unknown destination is serving as the destination for large amounts of network traffic. |