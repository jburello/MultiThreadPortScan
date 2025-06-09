# MultiThreadPortScan

A simple, multithreaded TCP port scanner written in Python.  
It efficiently scans a range of ports on a target IP address or hostname using concurrent threads to speed up the process.

---

## Features

- Supports scanning user-defined port ranges (e.g., 1-1024)
- Resolves hostnames to IP addresses automatically
- Uses multithreading (default 100 threads) for faster scanning
- Thread-safe collection and display of open ports
- Validates user input for IP addresses and port ranges
- Prints real-time results of open ports during scanning
- Clean and user-friendly command-line interface

---

## Requirements

- Python 3.x
- No external dependencies (uses built-in `socket`, `threading`, `queue` modules)

---
