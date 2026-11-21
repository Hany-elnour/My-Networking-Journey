# Project: Integrating Network Automation with PNETLab

## 1. Project Documentation — Why Am I Doing This?

### Motivation

I discovered [netlab](https://netlab.tools/) while exploring tools that could improve my networking lab environment. Initially, I was looking at it as another way to build network topologies, but I started seeing potential beyond that.

I already have a working PNETLab environment running on Proxmox, with virtual Cisco devices that I use for CCNA and CCNP Enterprise studies. Rather than replacing that environment, I want to explore how I can integrate network automation tools into it.

The idea is to build a workflow where I can use tools like netlab, Ansible, Python, and GitHub to automate and manage devices running inside PNETLab.

### Project Goals

- Explore how netlab can complement an existing PNETLab environment.
- Establish a dedicated management path to virtual network devices without exposing their management interfaces to my physical home LAN.
- Experiment with SSH-based device management from the PNETLab server or a dedicated automation controller.
- Use Python, Ansible, and potentially Netmiko to automate network configurations.
- Integrate GitHub for version control and documentation.
- Explore GitHub Codespaces for developing and maintaining automation projects.
- Investigate GitHub Actions and self-hosted runners for automating workflows within my home lab.

### Why This Matters

This project is about moving beyond manually configuring individual network devices.

I want to develop a better understanding of how network automation, infrastructure management, and version control work together in a practical environment.

It also gives me an opportunity to build something closer to a real-world network engineering workflow while continuing to use my existing virtual lab.

---

## 2. TODO — Project Implementation

### Phase 1: Preparation and Discovery

- [ ] Create a full Proxmox backup of the PNETLab VM.
- [ ] Document the current PNETLab network architecture.
- [ ] Document existing interfaces, bridges, and IP addressing.
- [ ] Review netlab's documentation and supported providers.
- [ ] Determine whether netlab's External Provider can support the intended workflow.
- [ ] Identify which components should run on PNETLab versus a separate automation controller.

### Phase 2: Management Network

- [x] Identify PNETLab's internal `pnet_nat` network.
- [x] Connect a separate management interface to an IOSv router.
- [x] Assign a management IP address to the router.
- [x] Verify connectivity from the PNETLab server using ICMP.
- [x] Verify SSH connectivity from the PNETLab server.
- [ ] Document the management network design.
- [ ] Test SSH command execution without an interactive session.
- [ ] Test connectivity to additional virtual network devices.
- [ ] Determine an IP addressing and device naming convention.

### Phase 3: Automation Environment

- [ ] Evaluate Python and pip availability on PNETLab.
- [ ] Create an isolated Python virtual environment if using PNETLab as the initial controller.
- [ ] Install and test the required automation dependencies.
- [ ] Evaluate Ansible connectivity to IOSv devices.
- [ ] Test basic configuration retrieval.
- [ ] Test configuration deployment on a disposable lab device.
- [ ] Investigate netlab's External Provider capabilities.
- [ ] Determine how netlab-generated inventories and configurations could fit into the workflow.

### Phase 4: GitHub Integration

- [ ] Create a dedicated GitHub repository for this project.
- [ ] Document the network architecture with diagrams.
- [ ] Store automation playbooks and Python scripts in version control.
- [ ] Create an inventory for lab devices.
- [ ] Explore GitHub Codespaces for development.
- [ ] Keep credentials and secrets out of the repository.
- [ ] Investigate GitHub Actions integration.
- [ ] Evaluate a self-hosted GitHub Actions runner inside the home lab.
- [ ] Implement a controlled workflow for running automation against lab devices.

### Phase 5: Testing and Validation

- [ ] Retrieve interface information from an IOSv device using automation.
- [ ] Automate a basic configuration change.
- [ ] Verify the change on the network device.
- [ ] Test configuration backup and version tracking.
- [ ] Test repeatable deployment of configurations.
- [ ] Document failures, troubleshooting steps, and lessons learned.
- [ ] Evaluate whether the workflow is reliable enough to expand to additional devices.

### Phase 6: Final Documentation

- [ ] Create a final network architecture diagram.
- [ ] Document the complete automation workflow.
- [ ] Explain the role of each technology.
- [ ] Document security considerations and limitations.
- [ ] Include example playbooks and configuration files.
- [ ] Record test results and lessons learned.
- [ ] Write a project summary for my GitHub portfolio.

---

## 3. Technologies Involved

| Technology | Intended purpose |
|---|---|
| PNETLab | Virtual network device environment |
| Proxmox | Virtualization platform |
| netlab | Network lab modeling and automation exploration |
| Python | Automation scripting and tooling |
| Ansible | Network configuration management |
| Netmiko | SSH-based network device interaction |
| Git / GitHub | Version control and project documentation |
| GitHub Codespaces | Cloud-based development environment |
| GitHub Actions | Workflow automation |
| Cloudflare | Existing secure remote access infrastructure |

## 4. Initial Success Criteria

The project will be considered successful when I can:

1. Manage virtual Cisco devices through a dedicated management network.
2. Execute commands against those devices programmatically.
3. Automate configuration changes using Ansible or Python.
4. Track automation code and configuration changes through Git.
5. Trigger a controlled automation workflow through GitHub.
6. Document a repeatable process that can be expanded to additional lab devices.

**Long-term vision:** Build a self-hosted network automation environment that connects virtual network infrastructure, automation tooling, and Git-based workflows without unnecessarily exposing lab management interfaces to my home network.

---

## 5. Design Notes and Assumptions

- The existing PNETLab topology should remain intact while testing management connectivity.
- The `pnet_nat` management path has been verified from the PNETLab host to one IOSv router using ping and SSH.
- The current successful test proves host-to-device reachability; it does not yet prove that a separate VM or cloud-hosted Codespace can reach that network.
- Do not assume netlab's External Provider manages PNETLab's topology lifecycle. Validate exactly what it can do before choosing the final architecture.
- Prefer an isolated Python virtual environment for experiments. Avoid changing PNETLab's system Python or installing virtualization components until compatibility has been assessed.
- Treat any self-hosted GitHub Actions runner as a security boundary: restrict who can trigger workflows, avoid running untrusted pull-request code, and use least-privilege credentials.
