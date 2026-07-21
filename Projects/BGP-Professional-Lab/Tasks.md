```markdown
# 📋 govNet Core Engineering Requirements & Tasks

Your government has asked you to help design its vision of govNet, a large private network that will be used to interconnect all of the region’s public sector services. Schools, hospitals, universities, museums, government offices, and various other types of public buildings and services will be connected to this network. govNet will essentially function as the ISP for these public sector institutions. The network will provide Internet connectivity, telephony, and various other network services required for the public sector to operate.

govNet will be separated into several geographically defined administrative areas, each served by a BGP Autonomous System (AS). The whole network will connect to the Internet via a Tier 1 ISP.

Your job is to set up and configure all of the main BGP routers to fulfill the needs of the network. Your work will include:

Basic BGP configuration of routers including eBGP peerings and iBGP peerings as shown in the topology diagram.
Manipulation of various BGP attributes to achieve the required advertising of particular networks.
The implementation of BGP communities to implement traffic engineering and dynamic routing policies.
Additional advanced BGP configurations including confederations, route filtering, peer groups, and multipath among others, to achieve the required network behavior and capabilities.

In preparation for migration to IPv6, you will introduce some IPv6 routes to be advertised by the BGP topology.
Your expertise will play a key role in advancing govNet to become one of the most sophisticated government networks in the world. This is your chance to demonstrate your potential and contribute to building a network that is not only scalable and reliable but also instrumental in achieving the regional government’s ambitious goals.

---

## 1. IGP Foundation & Overlay Transport

* **OSPF Preparation**:
  * Configure OSPF within **AS 23** and **AS 4567** to establish underlying L3 reachability for loopback-based iBGP sessions.
* **Non-BGP Transit Tunneling**:
  * **R8** does not run BGP, but **R5** and **R9** must form a direct eBGP neighbor adjacency using their loopback interfaces.
  * *Constraint*: You are only permitted to configure two static routes on **R8**, and two static routes each on **R5** and **R9**. Build a tunnel solution to bridge R5 and R9.

---

## 2. BGP Fundamentals & IPv6 Dual-Stack

* **IPv4 Peering Matrix**:
  * Establish iBGP sessions using loopback interfaces (do not use physical interfaces).
  * Establish eBGP sessions using physical interfaces (except for multihop/tunnel exceptions).
  * Configure eBGP between **R1 ↔ ISP**, **R1 ↔ R2**, **R1 ↔ R3**, **R1 ↔ R4**, **R2 ↔ R4**, and **R3 ↔ R5**.
  * Configure iBGP between **R2 ↔ R3**.
  * Configure intra-confederation eBGP/iBGP peerings across **AS 4567** sub-autonomous systems.
  * Configure eBGP multihop between **R5 ↔ R9** over loopbacks, ensuring 4-byte AS numbers are properly interpreted.
* **IPv6 eBGP Integration**:
  * Establish an IPv6 eBGP session between **ISP** and **R1** using physical interface addresses.
* **Route Advertisements & Next-Hop Self**:
  * Redistribute directly connected IPv4 networks on the ISP router into BGP.
  * Advertise `Loopback 0` on the ISP router via the BGP `network` command.
  * Advertise IPv6 prefixes on ISP loopbacks 0–19 over the IPv6 BGP session.
  * Configure **AS 23** to receive IPv6 routes over the IPv4 eBGP peerings with **R1**.
  * Restrict IPv6 route propagation so prefixes are contained within **AS 1** and **AS 23** and do not leak further.
  * Advertise loopback addresses for all BGP routers into BGP.
  * Configure `next-hop-self` on all required routers for proper egress routing.

---

## 3. Advanced BGP & Path Manipulation

* **BGP Auto-Summary**: Enable auto-summary on **R9** for efficient aggregation of future `9.0.0.0/8` subnets.
* **BGP Route Summarization**: Aggregate loopbacks 10, 11, and 12 on the ISP router using the most specific summary address, suppressing more specific routes.
* **Weight Attribute**: Force **R4** to route `12.34.0.0/16` via **AS 23** instead of directly via **AS 1** using a route-map.
* **Local Preference**: Ensure outbound traffic from **AS 23** destined for `23.45.0.0/16` always exits via **R2**.
* **AS-Path Prepending**: Prepend the AS path on **R4** (3x length) so traffic from **R1** destined to **R9's** loopback prefers the **AS 23** path over **AS 4567**.
* **Origin Code Normalization**: Modify `66.77.0.0/17` on the ISP router so downstream peers view it with an `IGP` origin code.
* **MED Attribute Tuning**: Configure MED on **R3** so that incoming traffic from **AS 1** to **R9** prefers **R2** over **R3**.
* **Best Path Analysis**: Evaluate the `91.200.0.0/18` prefix on **R3** and determine the winning BGP path selection criteria across multiple entries.

---

## 4. Community-Based Policy Control

* **`no-advertise`**: Apply policy on **R1** using communities to prevent `102.64.0.0/18` from being advertised downstream by **R2**, **R3**, and **R4**.
* **`no-export`**: Advertise `123.45.0.0/17` from **R1** to **AS 23** and **AS 4567** tagged such that eBGP peers will not readvertise it externally.
* **`local-AS`**: Restrain `130.25.0.0/18` propagation within **Sub-AS 45** so it is not advertised into **Sub-AS 67** or beyond.

---

## 5. Route Filtering & Security Policies

* **Prefix-List Filtering**: Filter out all `/18` prefixes on **R5** so they do not enter **R9's** BGP table.
* **Extended ACL Filtering**: Configure extended access-list filtering on **R9** to drop prefixes between `/22` and `/32`.
* **Transit AS Protection**: Ensure **AS 23** never acts as a transit autonomous system for the `175.45.200.0/21` prefix using access list distribute-lists.
* **AS-Path Filtering**:
  * Filter any routes passing through **AS 23** on **R6**.
  * Filter routes on **R3** that have traversed **AS 4567**, while permitting routes originated within **AS 4567**.

---

## 6. Stability, Optimization & Convergence

* **BGP Route Dampening**: Enable route dampening on **R2** for ISP loopback networks 13, 14, and 15 (Half-life: 15, Reuse: 750, Suppress: 2000, Max-suppress: 60).
* **BGP Peer Groups**: Configure peer groups on **R1** for scalable peer expansion into **AS 23**.
* **Soft Reconfiguration**: Enable inbound soft reconfiguration on **R6** and **R7** for inter-sub-AS links.
* **BGP Multipath**: Enable dual-path BGP multipath (`maximum-paths 2`) on **R1** for subnet `192.168.23.0/24` via both **R2** and **R3**.
* **Next-Hop Tracking**: Configure BGP next-hop tracking on **R1** for **R2** and **R3** with a 10-second trigger delay for IPv4.