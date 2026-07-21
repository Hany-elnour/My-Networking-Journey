# 🌐 govNet: High-Availability Public Sector BGP Core Architecture

[![Network Architecture](https://img.shields.io/badge/Network-BGP%20%7C%20MP--BGP-blue.svg)](#)
[![IGP](https://img.shields.io/badge/IGP-OSPFv2-green.svg)](#)
[![IPv6 Ready](https://img.shields.io/badge/IPv6-Dual--Stack-purple.svg)](#)
[![Emulation](https://img.shields.io/badge/Platform-EVE--NG%20%2F%20PNETLab-orange.svg)](#)

## 📌 Overview

**govNet** is an enterprise-grade multi-AS regional network core designed to serve as a dedicated public sector Internet Service Provider (ISP). The network interconnects essential regional public infrastructure, including schools, universities, healthcare systems, municipal buildings, and civil administration centers.

This repository contains the complete architectural specifications, topology designs, path manipulation policies, traffic engineering rules, and router configuration files for the **govNet** BGP core backbone.

---

## 📐 Network Topology & Autonomous System Hierarchy

![Network Topology Diagram] (Topology.png)

### Autonomous System Allocation Matrix

| Autonomous System | Entity / Role | Nodes | Key Protocols & Technologies |
| :--- | :--- | :--- | :--- |
| **AS 999** | Tier-1 Upstream ISP | ISP | eBGP, IPv4 (`203.0.113.0/30`), IPv6 (`2001:DB8::/64`) |
| **AS 1** | Regional Core Gateway | R1 | Dual-Stack eBGP, Peer-Groups, Multipath, Next-Hop Tracking |
| **AS 23** | Transit Backbone | R2, R3 | iBGP Full Mesh, OSPF Area 0, Local Preference, Route Dampening |
| **AS 4567** | Regional Confederation Core | R4, R5, R6, R7 | **Sub-AS 45** (R4, R5), **Sub-AS 67** (R6, R7), eBGP Intra-Confed |
| **AS 65505.9** | Remote Enterprise Branch | R8, R9 | 4-Byte ASDOT Notation, GRE Overlay (bypassing non-BGP R8) |

---

## 🛠️ Technical Highlights & Feature Matrix

### 1. Underlying IGP & Overlay Transport
* **OSPF Area 0**: Established within AS 23 (R2, R3) and AS 4567 (Sub-AS 45 and Sub-AS 67) to ensure iBGP loopback reachability.
* **GRE Tunneling over Non-BGP Transit**: Provisioned point-to-point GRE tunnel between R5 and R9 across non-BGP intermediate router R8 to support multihop eBGP neighbor adjacency.

### 2. Multi-Protocol BGP (MP-BGP) & IPv6 Integration
* **Dual-Stack Peering**: Configured IPv4 and IPv6 BGP address families on the ISP-to-R1 edge link.
* **IPv6 Propagation Boundary**: IPv6 prefixes are advertised into AS 1 and propagated into AS 23 over IPv4 peerings, with explicit route-map filtering preventing IPv6 route leakage beyond AS 23.
* **4-Byte ASN Support**: Configured 32-bit ASDOT format (`AS 65505.9`) across all network nodes.

### 3. Path Manipulation & Traffic Engineering
* **Weight Attribute**: Applied via inbound route-maps on R4 to force `12.34.0.0/16` traffic through AS 23 rather than directly via AS 1.
* **Local Preference**: Inbound policy on R2 enforces AS 23 exit paths via R2 for `23.45.0.0/16`.
* **AS-Path Prepending**: R4 prepends its AS path 3x for R9 loopback reachability to make the AS 23 path preferred by R1.
* **MED Adjustments**: Inflated MED on R3 for R9 prefixes to prioritize R2 over R3 for incoming traffic from AS 1.
* **Origin Code Normalization**: Route-maps on the ISP rewrite redistributed prefixes (`66.77.0.0/17`) to `IGP` origin.

### 4. Dynamic Community Policy Controls
* **`no-advertise`**: R1 tags `102.64.0.0/18` to prevent downstream propagation past peer routers.
* **`no-export`**: R1 tags `123.45.0.0/17` so external eBGP peers in AS 23 and AS 4567 do not re-advertise the prefix.
* **`local-AS`**: Applied inside Confederation 4567 to constrain `130.25.0.0/18` to Sub-AS 45.

### 5. Advanced Route Filtering & Convergence
* **Prefix-List & Extended ACL Filtering**: Blocked `/18` prefixes and `/22` through `/32` ranges on R5 and R9 respectively.
* **AS-Path ACL Filtering**: R6 blocks all routes traversing AS 23; R3 strips transit paths through AS 4567 while retaining locally originated routes.
* **Route Dampening**: Enforced flap dampening on R2 for ISP loopback networks (`13.0.0.0/8`, `14.0.0.0/8`, `15.0.0.0/8`).
* **BGP Multipath & Next-Hop Tracking**: Enabled load balancing across dual paths on R1 (`maximum-paths 2`) with 10-second next-hop trigger delays.

---

## 📂 Repository Structure

```
├── README.md                      # Repository overview and architectural summary
├── Tasks.md    # Complete end-to-end configuration & lab manual
└── configs/                       # Cisco IOS configuration files per router
    ├── ISP.cfg
    ├── R1.cfg
    ├── R2.cfg
    ├── R3.cfg
    ├── R4.cfg
    ├── R5.cfg
    ├── R6.cfg
    ├── R7.cfg
    ├── R8.cfg
    └── R9.cfg
```

---

## 🚀 Quick Start & Verification Guide

1. **Verify BGP Neighbor Summary**:
   ```text
   show ip bgp summary
   show ipv6 bgp summary
   ```
2. **Inspect BGP Decision Tree & Best Path**:
   ```text
   show ip bgp 9.9.9.9
   show ip bgp 91.200.0.0/18
   ```
3. **Verify Active Community Tags**:
   ```text
   show ip bgp community no-advertise
   show ip bgp community no-export
   show ip bgp community local-AS
   ```

---

## 📜 License & Acknowledgments

This lab project is developed for enterprise network architecture demonstration, lab research, and certification preparation using Cisco vIOS / EVE-NG.
