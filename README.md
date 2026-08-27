# port-scanner

A simple CLI program for scanning ports on a network using ```socket```.
<br>
This was built to better understand indirectly how a port scanner like **nmap** functions behind the scenes.

---

## v1.0

Sequential TCP scanner using the ```socket``` library. Scans all 65535 ports on a given target and reports which are open.
<br>
Usage: ```> python main.py <target>```
<br>
Example: ```> python main.py scanme.nmap.org```
<br>
No threading. No port range or other arguments yet.

## v2.0

Threaded TCP scanner using ```ThreadPoolExecutor```. Distributes port scans across a pool of worker threads for significantly faster scans compared to v1's sequential approach.
<br>
Usage: ```> python main.py <target>```
<br>
Example: ```> python main.py scanme.nmap.org```
<br>
Still scans all 65535 ports; no configurable range or worker count yet.

## Roadmap

- **v3.0** — Port ranges, worker count, and timeout as CLI arguments; reading targets/ports from a file.
- **v4.0** — Service and version detection.
- **v5.0** — May add implementation for sending RST instead of completing ACK for stealth.