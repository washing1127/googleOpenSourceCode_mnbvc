import os
import glob
import json
import shutil
import subprocess


fs = glob.glob("*.json")

err = 0

for f in fs:
    with open(f) as r: j = json.loads(r.read())
    for value in j.values():
        clone_url = value['clone_url']
        out_path = clone_url.replace('.googlesource.com', '')[7:].strip('/')

        if os.path.exists(out_path):
            print(out_path, 'exist.')
            continue

        # 创建目标目录
        shutil.os.makedirs(out_path, exist_ok=True)

        try:
            subprocess.run(['git', 'clone', clone_url, out_path])
            print(f"==== Repository {clone_url} cloned successfully ====")
        except subprocess.CalledProcessError as e:
            print(f"**** Cloning repository {clone_url} failed with reason: {e}")
            # 删除已下载部分
            shutil.rmtree(out_path)
            err += 1

print(f"{err} Errors.")
