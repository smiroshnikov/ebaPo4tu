import subprocess

server_execution = "python3.6 -m http.server 5500"
lsof_proc = subprocess.run(['lsof', '-n', '-i4TCP:5500'], stdout=subprocess.PIPE)
process_output = lsof_proc.stdout.decode().splitlines()

pid = None
for line in process_output:
    if "(LISTEN)" in line:
        pid = [v for v in line.split() if v.isdigit()][0]
        print(f"FOUND PID {pid}")
try:
    kill_command = subprocess.run(['kill', '-9', pid], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if kill_command.returncode == 0:
        print(f"killed {pid}!")
except TypeError as e:
    print(f"NO SUCH PROCESS !!! ")

# proc = subprocess.run(["ls", "-la"], stdout=subprocess.PIPE)
# r = (str(proc.stdout.decode()))
# print(r.upper())
# print(str(proc.stdout))  # raw byte information
# print(str(proc.stdout.decode()))  # raw byte information
#
# try:
#     new_proc = subprocess.run(['cat', 'fake.txt'], check=True)
# except subprocess.CalledProcessError as e:
#     print(f"ERROR {e}")

# print([int(v) for v in line.split() if v.isdigit()])

# if re.findall(r'\d+',v):
#     print(v)

# r = (lsof_proc.stdout.splitlines())
# print(r[1].split()[1])
#
# s = 'Java\n Python Android Kotlin ' \
#     'PHP \n ' \
#     'another line'
#
# r1 = s.splitlines()
# print(r1)
