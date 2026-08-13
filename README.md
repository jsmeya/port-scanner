# port-scanner

A simple CLI program for scanning ports on a network using ```socket```.
<br>
This was built to better understand indirectly how a port scanner like **nmap** functions behind the scenes.

---

## v1

Sequential TCP scanner using the ```socket``` library. Scans all 65535 ports on a given target and reports which are open.
<br>
Usage: ```> python main.py <target>```
<br>
Example: ```> python main.py scanme.nmap.org```
<br>
No threading. No port range or other arguments yet.

## Roadmap

- **v2** — Threading for faster scans.
- **v3** — Port ranges, including reading targets/ports from a file.
- **v4** — Service and version detection.