import os
import subprocess
from git import Repo

# Daftar repositori dan folder target
repos = {
    "1": "https://github.com/AinzOoalGowns/1.git",
    "2": "https://github.com/AinzOoalGowns/2.git",
    "3": "https://github.com/AinzOoalGowns/3.git",
    "4": "https://github.com/AinzOoalGowns/4.git",
    "5": "https://github.com/AinzOoalGowns/5.git",
}

def clone_repo(repo_url, target_dir):
    if not os.path.exists(target_dir):
        print(f"Mengkloning repo {repo_url} ke {target_dir}...")
        Repo.clone_from(repo_url, target_dir)
    else:
        print(f"Repo {target_dir} sudah ada, melewati kloning.")

def run_script(script_path):
    print(f"Menjalankan script: {script_path}")
    process = subprocess.Popen(["python", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        print(f"Berhasil menjalankan {script_path}:\n{stdout.decode().strip()}")
    else:
        print(f"Error menjalankan {script_path}:\n{stderr.decode().strip()}")

def main():
    base_path = os.getcwd()  # Lokasi direktori saat ini
    for folder, repo_url in repos.items():
        target_dir = os.path.join(base_path, folder)
        
        # Kloning repositori jika belum ada
        clone_repo(repo_url, target_dir)
        
        # Validasi file di dalam folder
        script_path = os.path.join(target_dir, "1.py")
        userid_path = os.path.join(target_dir, "userid.txt")
        proxy_path = os.path.join(target_dir, "proxy.txt")
        
        if not (os.path.exists(script_path) and os.path.exists(userid_path) and os.path.exists(proxy_path)):
            print(f"Folder '{folder}' tidak memiliki semua file yang diperlukan. Melewati...")
            continue
        
        # Jalankan script
        run_script(script_path)

if __name__ == "__main__":
    main()