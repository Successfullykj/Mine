import os
import subprocess
import threading

# ✅ Config
XMRIG_URL = "https://github.com/xmrig/xmrig/releases/download/v6.18.0/xmrig-6.18.0-linux-x64.tar.gz"
XMRIG_ARCHIVE = "xmrig-6.18.0-linux-x64.tar.gz"
XMRIG_FOLDER = "xmrig-6.18.0"
POOL = "soulcrack.duckdns.org:8080"  # 🔁 Updated pool
WALLET = "47HxtCmFXxqVzQSGjQgBnDC1LRTrokf3aMFocbWQRxYzjhjxkfLGjzwE3PJhrCtdQkXPunr8cZZBAiEmY5W46V1UV8mFMZh"
PASS = "myworker"
NUM_MINERS = 10

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
        "-u", WALLET,
        "-p", PASS,
        "-k",             # 🔐 Keepalive
        "--coin", "monero"  # 🪙 Monero mode
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
