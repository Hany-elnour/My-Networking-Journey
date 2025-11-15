# Python Network Emulator 🖧

## Overview

This project is a **Python-based network emulator** that simulates the behavior of a basic network devices. It is designed primarily for **learning, experimentation, and keeping coding skills fresh**.

The emulator supports:

* **MAC address learning**: Learns source MAC addresses on ingress ports.
* **Frame forwarding**: Forwards frames to the correct egress port if the destination MAC is known.
* **Broadcast handling**: Floods frames to all ports when the destination MAC is unknown or broadcast.
* **Detailed console output**: Colorful and structured logs for easy tracing of frame flow.

## Goals

* Explore **network behavior** without the need for real hardware.
* Experiment with **Python programming and network logic**.
* Future expansion:

  * Implement **Control Plane APIs** for switches.
  * Add support for **VLANs**, **multiple switches**, or **traffic logging**.


## File Structure

```
python-network-emulator/
├── network_device.py          # Main emulator logic|
|── generate_traffic.py        # Simulate traffic  
├── .gitignore       # Ignore Python caches, logs, virtual environments
└── README.md        # Project overview and instructions
```

## Example Output

```
📥 Frame received on Eth0/1 | From: 00:11:22:33:44:55 -> To: FF:FF:FF:FF:FF:FF | Size: 64 bytes
💡 Learned 00:11:22:33:44:55 on Eth0/1
🟡 Broadcast frame detected
➡️ Forwarded frame (64 bytes) to FF:FF:FF:FF:FF:FF via Eth0/2
➡️ Forwarded frame (64 bytes) to FF:FF:FF:FF:FF:FF via Eth0/3
...
```

## Future Work
* Expand to **multi-switch topologies**.
* Add **packet inspection** or **logging** for debugging and analytics.
