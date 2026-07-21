# vlan-config-generator
# Takes a list of VLANs and generates ready-to-paste Cisco IOS commands
# Combines CCNA knowledge with Python automation

def generate_vlan_config(vlans):
    print("=== VLAN Configuration ===\n")
    
    config = []
    
    for vlan in vlans:
        vlan_id = vlan["id"]
        vlan_name = vlan["name"]
        
        # generate Cisco IOS commands
        config.append(f"vlan {vlan_id}")
        config.append(f" name {vlan_name}")
        config.append("!")
    
    # print config
    for line in config:
        print(line)
    
    return config

# define VLANs
vlans = [
    {"id": 10, "name": "Management"},
    {"id": 20, "name": "Finance"},
    {"id": 30, "name": "HR"},
    {"id": 40, "name": "IT"},
    {"id": 50, "name": "Guest"},
]

generate_vlan_config(vlans)