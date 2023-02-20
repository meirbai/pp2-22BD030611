import json
with open("data.json", "r") as read_file:
    data = json.load(read_file)
print("""Interface Status
================================================================================""")
print("""DN                                             Description          Speed                      MTU """)
i = int(0)
for i in range(3):
    for i, k in data["imdata"][i]['l1PhysIf']["attributes"].items():
        if i == 'dn':
            print(k, end="                          ")
        if i == "speed":
            print(k, end="                                         ")
        if i == "mtu":
            print(k, end="                   ")
    print("")
