# port-scanner

A simple CLI program for scanning ports on a network using ```socket```.
<br>
This was built to better understand indirectly how a port scanner like **nmap** functions behind the scenes. Only functions across TCP, for now.

---

## v3.0

Configurable, threaded TCP scanner built on ```argparse```.
<br>
Usage: ```> python main.py <target> [-p PORTS] [-w WORKERS] [-t TIMEOUT]```
<br>
Example: ```> python main.py scanme.nmap.org -p 22,80,1000-2000 -w 200 -t 0.5```

- **`-p/--ports`** — ports to scan as a comma list, a range, or both mixed (e.g. ```22,80,1000-2000```). Defaults to all 65535 ports.
- **`-w/--workers`** — thread pool size, bounds-checked to 1-1000. Since scanning is I/O-bound rather than CPU-bound, the default scales off the machine's core count (```os.cpu_count() * 50```, capped at 1000) instead of a fixed number.
- **`-t/--timeout`** — per-connection socket timeout in seconds, bounds-checked to 0-5.
- The target hostname/IP is resolved once upfront; an unresolvable target now fails fast with a clear error instead of silently reporting every port as closed.
- Output only lists open ports, with a closing note that anything unlisted is closed, filtered, or a UDP-only service (TCP connect scans can't see e.g. DNS's UDP:53).

## v2.0

Threaded TCP scanner using ```ThreadPoolExecutor```. Distributes port scans across a pool of worker threads for significantly faster scans compared to v1's sequential approach.
<br>
Usage: ```> python main.py <target>```
<br>
Example: ```> python main.py scanme.nmap.org```
<br>
Still scans all 65535 ports; no configurable range or worker count yet.

## v1.0

Sequential TCP scanner using the ```socket``` library. Scans all 65535 ports on a given target and reports which are open.
<br>
Usage: ```> python main.py <target>```
<br>
Example: ```> python main.py scanme.nmap.org```
<br>
No threading. No port range or other arguments yet.

## Roadmap

- **v4.0** — Service and version detection.
- **v5.0** — May add implementation for sending RST instead of completing ACK for stealth. Also may add UDP connections.