from pathlib import Path
import filecmp

p = Path('.').resolve()
# print(f'{[x for x in p.iterdir() if x.is_dir()]}')

for v in p.iterdir():
    if v.is_dir():
        print(str(v))

if filecmp.cmp('iterating_ovet_path.py', 'working_with_path.py',shallow=False):
    print("same")
else:
    print("diff")
