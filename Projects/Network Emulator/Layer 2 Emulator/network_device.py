interface_names = ["Eth0/1" , "Eth0/2" , "Eth0/3" , "Eth0/4" , "Eth0/5" , "Eth0/6" , "Eth0/7" , "Eth0/8"]
print(interface_names)

for port in interface_names:
    print(port)

mac_table = {
    "00:1A:2B:3C:4D:01": "Eth0/1",
    "3C:F0:11:8A:7B:22": "Eth0/2",
    "A4:5E:60:9B:12:33": "Eth0/3",
    "F8:16:54:2A:99:44": "Eth0/4",
    "D0:7E:35:CC:8D:55": "Eth0/5",
    "B8:27:EB:66:42:66": "Eth0/6",
    "4C:32:75:AE:01:77": "Eth0/7",
    "68:5D:43:9F:21:88": "Eth0/8"
}

print(mac_table)