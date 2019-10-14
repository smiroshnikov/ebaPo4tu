import os

blacklist = ["slow_drive.json"]
file_list = []

for f in os.listdir("E:\Development\ebaPo4tu\playground\GM_task_3\json_scenarios"):
    # print(f.endswith(".json"))
    if f.endswith(".xml"):
        pass
    # print(f"XMLs files found---> {f}")

    elif f.endswith(".json"):
        # print(f"JSON files found ####> {f}], added to list")
        file_list.append(f)

print(file_list)
# print(blacklist)
# r = set(file_list) - set(blacklist)
r = " ".join(str(v) for v in set(file_list) - set(blacklist))
print(r)
