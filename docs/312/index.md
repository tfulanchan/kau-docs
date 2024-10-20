---
sidebar_position: 0
title: CPIS-312
---

# [CPIS-312 Information systems strategies and policies](https://fcit.kau.edu.sa/aims/runReportAPI2.php?REP_ID=3&FL_TYPE=pdf&CLG_ID=1&PRA_STR=(PARAM1:18)%7C(PARAM2:2)%7C(PARAM3:3)%7C(PARAM4:BINDER)%7C(PARAM6:CPIS-312)%7C(PARAM5:0)%7C(PARAM7:)%7C(P_DESFORMAT:PDF)%7C(P_RDF_FILENAME:BINDER)%7C(P_OUTPUT_FILENAME:Syllabus))

application layer: handle high level API

presentation layer: ensure data in usable format, encryption, decryption, compression and data translation

session layer: manage sessions of applications, coordinate communciation and maintain connections

transport layer: provide services to presentation layer to organize dialogue and manage data exchange

network layer: routing of datagrams from source to destination, handle logic addressing and packet forwarding

data link layer: data transfer between neighboring network elements, provides physcial addressing

physical layer: physical transmission of bitstreams through physical medium

## Module 5 Network Protocols

At School

1. In a school environment, students utilize devices like laptops and tablets to access online learning resources.
2. When Student 1 connects to the school's Wi-Fi network, their device communicates with the router using the Physical and Data Link layers for wireless communication.
3. Their search query is formatted into packets at the Network layer, addressed to ensure it reaches the appropriate destination.
4. These packets are then encapsulated into frames and transmitted as radio waves, which are converted into electrical signals that traverse the school's wired network, move through the Transport layer for reliable data transmission.
5. Once the request reaches the school's Internet Service Provider (ISP), the packets are routed through the ISP's infrastructure and travel across the Internet to the search engine.
6. At the Application layer, the search engine processes the query and returns results, which are sent back through the same layers and eventually displayed on Student 1's device.

Gaming

1. Student 2 connects gaming console to the internet via a home network that includes a router and a cable modem.
2. At the Physical layer, the console communicates through a wired connection, while the Data Link layer establishes a local area network (LAN) connection.
3. When Student 2 joins an online game, the gameplay data is encapsulated into packets at the Transport layer and sent through the ISP’s network.
4. The ISP's infrastructure uses the Network layer to route these packets to the game provider’s servers, which host the game.
5. The packets carry information identify Student 2, gaming actions, and network location.
6. The game provider's servers process this data at the Application layer and send back high-speed updates, including graphics and sound, which travel back through the OSI layers to Student 2's console.

Medical Consultations

1. In the medical context, Professional 1 relies on a cloud service for consulting with specialists about patient cases.
2. When a patient undergoes an X-ray, the hospital's imaging equipment digitizes the image, prepare it for transmission over the network.
3. At the Application layer, the medical data, including the X-ray and patient information, is encrypted to ensure confidentiality.
4. The data is then segmented into packets at the Transport layer, ensure reliable delivery.
5. The hospital’s network infrastructure uses the Network layer to route the encrypted data securely to the cloud service provider’s data center.
6. This data is encapsulated into frames at the Data Link layer and transmitted across various physical mediums, such as fiber-optic cables, utilize the Physical layer.
7. Once at the cloud provider's data center, the data can be accessed and managed securely, allow authorized medical personnel to retrieve and analyze the patient’s X-ray and other relevant information as needed.


| **OSI Model**            | **TCP/IP Model**         | **Description**     |
|--------------------------|--------------------------|---------------------------------------------------------------------------------|
| 7. Application Layer      | 4. Application Layer     | Handles network processes and user applications (e.g., HTTP, FTP, SMTP).        |
| 6. Presentation Layer     | -         | Manages data format translation, encryption, and compression.    |
| 5. Session Layer          | -         | Manages sessions and controls dialogues between computers.       |
| 4. Transport Layer        | 3. Transport Layer       | Ensures end-to-end communication, reliability (e.g., TCP, UDP).  |
| 3. Network Layer          | 2. Internet Layer        | Routes data between devices across different networks (e.g., IP).|
| 2. Data Link Layer        | 1. Network Access Layer  | Handles physical addressing and error detection for data transmission.          |
| 1. Physical Layer         | 1. Network Access Layer  | Manages the physical connection, electrical signals, and hardware interaction.   |

### OSI Model

|-| **OSI Layer**            | **Function** | **Example Protocols/Technologies**             |
|-|--------------------------|-------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| 7 | Application | Provides network services directly to user applications, handle high-level APIs and application protocols. | HTTP, FTP, SMTP, DNS           |
| 6 | Presentation | Translates data between the application and network, ensures data is in a usable format, manages encryption, decryption, compression, and data translation.  | SSL/TLS, JPEG, GIF, MPEG       |
| 5 | Session | Manages sessions between applications and connections between computers, coordinate communication and maintaining connections.         | NetBIOS, RPC    |
| 4 | Transport | Trasmits data via trasmission protocols, ensures error-free transmission of data between hosts, manage flow control and error checking. | TCP, UDP        |
| 3 | Network | Route datagrams from source to destination, handle logic addressing and packet forwarding | IP, ICMP, OSPF, RIP            |
| 2 | Data Link | Transfers data between nodes on the same network segment, provides physical addressing (MAC), error detection, and frames for the network.        | Ethernet, PPP, Wi-Fi, ARP      |
| 1 | Physical | Transmits raw bit streams over the physical medium (cables, radio waves).            | Ethernet cables, Fiber optics, 802.11 (Wi-Fi) |

### TCP/IP Model

|-| **Layer** | **Function**   | **Example Protocols/Technologies**             |
|-|-------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| 4 | Application Layer | Handles high-level protocols for data exchange and user services, ensures communication between applications. | HTTP, FTP, SMTP, DNS, SNMP                    |
| 3 | Transport Layer | Manages end-to-end communication, provides data segmentation, error correction, and flow control.         | TCP, UDP                                      |
| 2 | Internet Layer | Packet routing, logical addressing, and forwarding between networks.                      | IP, ICMP, ARP, OSPF, BGP                      |
| 1 | Network Access Layer | Handles hardware addressing, data link control, and physical data transmission across the network medium.  | Ethernet, Wi-Fi, PPP, Frame Relay             |

### Encapsulation

| **Concept** | **Definition** |
|----------------------------|--------------------------------------------------------------------------------------------------|
| Segmentation            | The process of breaking down large data packets into smaller ones for easier transmission.       |
| Multiplexing            | A technique that combines multiple signals or data streams into one for more efficient processing.|
| Encapsulation           | Wrapping data with protocol information (like headers) before transmission across a network.     |
| De-encapsulation        | The process of removing protocol headers from data as it reaches its destination.                |
| Denial-of-Service (DoS) | An attack that overwhelms a network or service with traffic, causing it to become unavailable.   |
| Man-in-the-Middle Attack| A cyberattack where an attacker intercepts and potentially alters communications between two parties.|
| Sniffer Attack          | A network attack where an attacker captures data packets to steal sensitive information.         |
| IP Address Spoofing Attack| A technique where an attacker disguises their device’s IP address to impersonate another system. |
| Eavesdropping Attack    | A passive attack where an attacker listens in on private communications to steal information.    |

=====================

## Module 13 Attackers and Their Tools

Indicators of Attack are signs of potential malicious activity or tactics that may indicate an ongoing or future attack, such as unusual network activity or suspicious access patterns.

Indicators of Compromise are evidence that an attack has already occurred, such as malware signatures, compromised files, or logs of unauthorized access.

While Indicators of Attack help in detecting and preventing attacks in real-time, Indicators of Compromise are used for forensic analysis and post-incident investigation.

### Categories of common network penetration testing tools

| Categories of Tools | Description |-|
|-|-|-|
| Password crackers | crack or recover the password. | John the Ripper, Ophcrack |
| Wireless hacking | intentionally hack into a wireless network to detect security vulnerabilities. | Aircrack-ng, Kismet |
| Network scanning and hacking | probe network devices, servers, and hosts for open TCP or UDP ports.  | Nmap, SuperScan |
| Packet crafting | probe and test a firewall’s robustness.  | Hping, Scapy
| Packet sniffers | capture and analyze packets within traditional Ethernet LANs or WLANs.  | Wireshark, Tcpdump |
| Rootkit detectors | a directory and file integrity checker used by white hats to detect installed root kits.  | AIDE, Netfilter |
| Fuzzers to search vulnerabilities | discover computer systems’ security vulnerabilities.  | Skipfish, Wapiti |
| Forensic | sniff out any trace of evidence existing in a particular computer system.  | Sleuth Kit, Helix |
| Debuggers | reverse engineer binary files when writing exploits and used by white hats when analyzing malware. | GDB, WinDbg |
| Hacking operating systems | preloaded with tools and technologies optimized for hacking.  | Kali Linux, SELinux |
| Encryption | use algorithm schemes to encode the data to prevent unauthorized access to the data.  | VeraCrypt, CipherShed |
| Vulnerability exploitation | identify whether a remote host is vulnerable to a security attack.  | Metasploit, Core Impact |
| Vulnerability scanners | scan a network or system to identify open ports. They can also be used to scan for known vulnerabilities and scan VMs, BYOD devices, and client databases. | Nipper, Securia PSI |

### Attacks

| Category of Attack | Description |
|-|-|
| Eavesdropping attack         | intercepts network communications to secretly listen in on data transfers, often referred to as snooping or packet sniffing |
| Data modification attack     | intercepts and alters the contents of data packets during transmission, modifying information without the sender or receiver noticing |
| IP address spoofing attack   | forges IP packet headers to make it appear as though the traffic originates from a trusted, legitimate source within the network |
| Password-based attacks       | gains access to a user’s credentials, allowing unauthorized access to a network or system using valid login information |
| Denial-of-service attack     | floods a target system or network with excessive requests or traffic, overwhelming resources and prevent legitimate users from accessing services |
| Man-in-the-middle attack     | intercepts the data being exchanged without their knowledge |
| Compromised key attack       | gains unauthorized access to a cryptographic key, enabling them to decrypt and read secure communications without detection |
| Sniffer attack               | captures and monitors network traffic to view unencrypted data transmitted over the network |

====================================

## Module 14 Common Threats and Attacks

A virus is a malicious code that attaches itself to a legitimate program or file and spreads when that file is executed by the user, requires human action to propagate.

A worm is self-replicating and does not need a host file or human intervention to spread. It exploits vulnerabilities in network systems to move across devices. It is autonomous and faster in infecting systems.

A Trojan horse disguises itself as legitimate software but contains malicious code. A Trojan does not replicate but relies on users to be tricked into downloading and running it, often to give attackers remote control or to steal sensitive information.

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
| Exploitation | The threat actor now attempts to discover vulnerable services that can be exploited | Metasploit, Core Impact, Sqlmap, Social Engineer Toolkit, Netsparker. |

### Attacks

|-|-|
|-|-|
| Access attacks | exploit known vulnerabilities in authentication services, FTP services, and web services to gain entry into web accounts, confidential databases, and other sensitive information. |
| Password Attacks | The threat actor attempts to discover critical system passwords using a variety of password cracking tools. |
| Spoofing Attacks | The threat actor device attempts to pose as another device by falsifying data. |

### Social engineering

| **Social Engineering Attack** | **Description**                                                                                                                                                                        |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Pretexting | The attacker fabricates a scenario to trick the victim into divulging sensitive information by posing as a trusted individual or authority, often under the guise of a legitimate request. |
| Phishing | A mass attack where an attacker sends fraudulent communications, typically emails, designed to appear as if they come from legitimate sources, with the intent of stealing credentials or installing malware. |
| Spear Phishing | A highly targeted form of phishing directed at a specific individual or organization, often using personalized information to increase the likelihood of success. |
| Spam | Unsolicited bulk messages, often sent via email, that may include deceptive offers, malicious links, or attachments, with the intent to deceive or compromise the recipient's system. |
| Quid Pro Quo (Something for Something) | The attacker offers a benefit or service in exchange for personal information or access, tricking the victim into thinking they will receive something of value. |
| Baiting | The attacker lures victims by placing enticing physical objects, such as malware-infected USB drives, in public spaces, counting on human curiosity to lead to their use in computers. |
| Impersonation | The attacker poses as a trusted individual, such as an IT administrator or colleague, to manipulate the victim into providing sensitive information or access. |
| Tailgating  | The attacker physically follows an authorized person into a restricted area, exploiting the person's trust or lack of attention to bypass security measures. |
| Shoulder Surfing | The attacker covertly observes a victim's private information, such as passwords or PINs, by looking over their shoulder, often in public places like ATMs or workstations. |
| Dumpster Diving | The attacker searches through discarded items, such as old documents, hard drives, or other media, to recover sensitive information that can be used for further exploitation. |

### Evasion

| Evasion Method | Description |
|--------------------|-----------------|
| Encryption and Tunneling  | This method involves encrypting malware files or utilizing tunneling to conceal malicious activity. Encryption scrambles the data, making it difficult for security tools to detect the malware. Tunneling hides malicious data within legitimate traffic, allowing it to bypass detection mechanisms.       |
| Resource Exhaustion       | Attackers deliberately overload the target system, consuming its resources such as CPU, memory, or bandwidth. This prevents the system from effectively running security checks, thus evading detection. |
| Traffic Fragmentation     | The attacker splits a malicious payload into smaller fragments to bypass security systems. These fragments, which might appear benign, are reassembled on the receiving end, where the malware can then begin its attack.    |
| Protocol-Level Misinterpretation | Attackers exploit weaknesses in how network security devices interpret certain protocol data units (PDUs), such as incorrect handling of checksums or Time-to-Live (TTL) values. This misinterpretation can cause firewalls or intrusion detection systems to incorrectly allow malicious traffic through. |
| Traffic Substitution      | The attacker obfuscates the malicious data by encoding it in an unfamiliar format (e.g., using Unicode instead of ASCII). The security system fails to recognize the threat, while the target system correctly interprets the payload.            |
| Traffic Insertion | Attackers insert additional benign data into a malicious sequence to evade detection by intrusion prevention systems (IPS). The IPS misses the hidden malicious code, as it is masked by seemingly innocuous extra bytes.        |
| Pivoting          | This technique involves expanding access after compromising a host within a network. For instance, a threat actor who gains access to an administrator’s credentials might use these to compromise additional hosts on the network, pivoting through the compromised system to escalate the attack.|
| Rootkits          | Rootkits are sophisticated malware that deeply integrate into the operating system, hiding the attacker's activity. They manipulate system functions to present sanitized results, hiding malicious processes, files, and connections from detection tools. This allows attackers to maintain long-term access without being discovered. |
| Proxies           | Attackers route malicious network traffic through intermediary proxy systems to obscure the final destination. This technique prevents security systems from identifying the true destination of stolen data or malicious communications, making it harder to detect and block command-and-control communications.|