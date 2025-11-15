from network_device import *

incoming_frame("00:1A:2B:3C:4D:01", "FF:FF:FF:FF:FF:FF", ingress_port="Eth0/1", size=64)
incoming_frame("3C:F0:11:8A:7B:22", "A4:5E:60:9B:12:33", ingress_port="Eth0/2", size=128)
incoming_frame("A4:5E:60:9B:12:33", "3C:F0:11:8A:7B:22", ingress_port="Eth0/3", size=512)
#incoming_frame("F8:16:54:2A:99:44", "00:00:00:00:00:00", ingress_port="Eth0/4", size=60)  # ARP request
incoming_frame("D0:7E:35:CC:8D:55", "FF:FF:FF:FF:FF:FF", ingress_port="Eth0/5", size=1500)
incoming_frame("B8:27:EB:66:42:66", "4C:32:75:AE:01:77", ingress_port="Eth0/6", size=256)
incoming_frame("4C:32:75:AE:01:77", "68:5D:43:9F:21:88", ingress_port="Eth0/7", size=1024)
incoming_frame("68:5D:43:9F:21:88", "00:1A:2B:3C:4D:01", ingress_port="Eth0/8", size=150)
incoming_frame("DE:AD:BE:EF:00:01", "FF:FF:FF:FF:FF:FF", ingress_port="Eth0/3", size=70)
incoming_frame("AA:BB:CC:DD:EE:FF", "F8:16:54:2A:99:44", ingress_port="Eth0/1", size=900)
incoming_frame("40:16:7E:99:00:12", "B8:27:EB:66:42:66", ingress_port="Eth0/6", size=350)
incoming_frame("88:99:AA:BB:CC:12", "FF:FF:FF:FF:FF:FF", ingress_port="Eth0/2", size=1400)

show_mac_address_table()