# MultiThreadPortScan

A fast and efficient **multithreaded port scanner** built with Python. Designed to quickly identify open TCP ports on a target host using concurrent threading and socket programming.

---

## Features

- Scans specified range of ports on a target IP address or domain.
- Uses multithreading to speed up scanning and reduce total scan time.
- Thread-safe handling of shared data for accurate results.
- Configurable thread count for balancing speed and resource use.
- Provides a clear list of open ports at the end of the scan.
- Includes timeout handling for unresponsive ports.

---

## Technologies Used

- Python 3
- `socket` library for TCP connection attempts
- `threading` library for concurrent execution
- `queue.Queue` for thread-safe task management
