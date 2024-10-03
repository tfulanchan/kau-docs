---
title: Nmap
sidebar_position: 0
---

```jsx title="1- Intense scan"
nmap -T4 -A -v target
```

Should be reasonable quick, scan the most common TCP ports. It will make an effort in determining the OS type and what services and their versions are running.

```jsx title="2- Intense scan plus UDP"
nmap -sS -sU -T4 -A -v target
```

Same as the regular Intense scan, just that we will also scan UDP ports (-sU).

```jsx title="3- Intense scan, all TCP ports"
nmap -p 1-65535 -T4 -A -v target
```

Leave no TCP ports unchecked.

```jsx title="4- Intense scan, no ping"
nmap -T4 -A -v -Pn target
```

Just like the other intense scans, however this will assume the host is up.

```jsx title="5- Ping scan"
nmap -sn target
```

Do only a ping only on the target, no port scan

```jsx title="6- Quick scan"
nmap -T4 -F target
```

Scan faster than the intense scan by limiting the number of TCP ports scanned to only the top 100 most common TCP ports.

```jsx title="7- Quick scan plus"
nmap -sV -T4 -O -F –version-light target
```

Add a little bit of version and OS detection and you got the Quick scan plus.

```jsx title="8- Quick traceroute"
nmap -sn –traceroute target
```

Use this option when you need to determine hosts and routers in a network scan. It will traceroute and ping all hosts defined in the target.

```jsx title="9- Regular scan"
nmap target
```

Default everything. This means it will issue a TCP SYN scan for the most common 1000 TCP ports, using ICMP Echo request (ping) for host detection.

```jsx title="10- Slow comprehensive scan"
nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 –script
```

“default or (discovery and safe)” target

It will put a whole lot of effort into host detection, not giving up if the initial ping request fails. It uses three different protocols in order to detect the hosts; TCP, UDP and SCTP