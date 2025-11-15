interface_names = ["Eth0/1", "Eth0/2", "Eth0/3", "Eth0/4", "Eth0/5", "Eth0/6", "Eth0/7", "Eth0/8"]
mac_table = {}

def forward_frame(dest_mac, egress_port, size):
    print(f"➡️  Forwarded frame ({size} bytes) to {dest_mac} via {egress_port}")

def flood_frame(dest_mac, ingress_port, size):
    print(f"🌊 Flooding frame ({size} bytes) from {ingress_port} to all other ports")
    for egress_port in interface_names:
        if egress_port != ingress_port:
            forward_frame(dest_mac, egress_port, size)

def incoming_frame(src_mac, dest_mac, ingress_port, size):
    print(f"\n📥 Frame received on {ingress_port} | From: {src_mac} -> To: {dest_mac} | Size: {size} bytes")

    # Learning MAC address
    if src_mac not in mac_table:
        print(f"💡 Learned {src_mac} is on {ingress_port}")
        mac_table[src_mac] = ingress_port
    else:
        print(f"🔁 Already know {src_mac} is on {mac_table[src_mac]}")

    # Forwarding logic
    if dest_mac in mac_table:
        egress_port = mac_table[dest_mac]
        print(f"🟢 Destination {dest_mac} found on {egress_port}, forwarding...")
        forward_frame(dest_mac, egress_port, size)
    elif dest_mac == "FF:FF:FF:FF:FF:FF":
        print(f"🟡 Broadcast frame detected -> To: FF:FF:FF:FF:FF:FF ")
        flood_frame(dest_mac, ingress_port, size)
    else:
        print(f"🔴 Destination {dest_mac} unknown, flooding...")
        flood_frame(dest_mac, ingress_port, size)
