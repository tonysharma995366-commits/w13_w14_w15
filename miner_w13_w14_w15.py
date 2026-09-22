#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Miner Automation - W13, W14, W15 (Terminals 361-450 Only)
W13: 361-390 | W14: 391-420 | W15: 421-450
"""

import os
import sys
import subprocess
import time
import argparse
import psutil
from datetime import datetime
from typing import Optional

def auto_install_dependencies():
    required = ['requests', 'psutil', 'pillow']
    for package in required:
        try:
            if package == 'pillow':
                __import__('PIL')
            else:
                __import__(package)
            print(f"[OK] {package} already installed")
        except ImportError:
            print(f"[*] Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
            print(f"[OK] {package} installed")

auto_install_dependencies()

import requests
from PIL import ImageGrab

# ==================== TELEGRAM ====================
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "8670890083:AAFdQaEiC67jmk6l8jxxdG01NTEN4JxvPUc")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "6955911349")

class TelegramLogger:
    def __init__(self):
        self.base_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"
    def send_message(self, message: str):
        try:
            requests.post(f"{self.base_url}/sendMessage", json={"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "HTML"}, timeout=10)
        except:
            pass
    def send_photo(self, image_path: str, caption: str):
        try:
            with open(image_path, 'rb') as f:
                requests.post(f"{self.base_url}/sendPhoto", files={'photo': f}, data={'chat_id': TELEGRAM_CHAT_ID, 'caption': caption, 'parse_mode': 'HTML'}, timeout=30)
            os.remove(image_path)
        except:
            pass

telegram = TelegramLogger()

# ==================== CONFIG ====================
FIREFOX_PATH = r"C:\Program Files\Mozilla Firefox\firefox.exe"
API_BASE = "https://api.unmineable.com/v5"
WALLET_ADDRESS = "nano_1g97x3h6wxd4h577p6dricapigs78ccc7tcowjfm67hewsmg7qob4xwc8jak"
COIN = "NANO"
BATCH_SIZE = 3
GAP_BETWEEN_BATCHES = 60
CHECK_INTERVAL = 360

# ==================== W13: TERMINALS 361-390 ====================
W13_TERMINALS = [
    [361, "Terminal 361", "ugviq3vaogk5cjrjh2njvu", "https://ais-pre-ugviq3vaogk5cjrjh2njvu-835267516178.asia-southeast1.run.app"],
    [362, "Terminal 362", "pan3eygcye354fuowtcm4p", "https://ais-pre-pan3eygcye354fuowtcm4p-835267516178.asia-southeast1.run.app"],
    [363, "Terminal 363", "u5zgzitckdtc2dqwrcxqmg", "https://ais-pre-u5zgzitckdtc2dqwrcxqmg-835267516178.asia-southeast1.run.app"],
    [364, "Terminal 364", "lh43kfxsmzzc6ex3mmg4z5", "https://ais-pre-lh43kfxsmzzc6ex3mmg4z5-835267516178.asia-southeast1.run.app"],
    [365, "Terminal 365", "64yapvcxgoucball7ydlnq", "https://ais-pre-64yapvcxgoucball7ydlnq-835267516178.asia-southeast1.run.app"],
    [366, "Terminal 366", "nuhedif7gbpvzib7tqukfm", "https://ais-pre-nuhedif7gbpvzib7tqukfm-835267516178.asia-southeast1.run.app"],
    [367, "Terminal 367", "2u6kupvewers3l4jrw6o5b", "https://ais-pre-2u6kupvewers3l4jrw6o5b-835267516178.asia-southeast1.run.app"],
    [368, "Terminal 368", "5xb5sznynsuhqmy4xux7fz", "https://ais-pre-5xb5sznynsuhqmy4xux7fz-835267516178.asia-southeast1.run.app"],
    [369, "Terminal 369", "dz5nfkzu2becu3wzsyp7fg", "https://ais-pre-dz5nfkzu2becu3wzsyp7fg-835267516178.asia-southeast1.run.app"],
    [370, "Terminal 370", "a6caldqf6fibtgkbwlzz4b", "https://ais-pre-a6caldqf6fibtgkbwlzz4b-835267516178.asia-southeast1.run.app"],
    [371, "Terminal 371", "mhnhav6maycupzpokwnmi2", "https://ais-pre-mhnhav6maycupzpokwnmi2-835267516178.asia-southeast1.run.app"],
    [372, "Terminal 372", "rykujqobn52s3jhqyb3a4b", "https://ais-pre-rykujqobn52s3jhqyb3a4b-835267516178.asia-southeast1.run.app"],
    [373, "Terminal 373", "5hhgpmnivny2bnb3v27tqf", "https://ais-pre-5hhgpmnivny2bnb3v27tqf-835267516178.asia-southeast1.run.app"],
    [374, "Terminal 374", "m6rwtgks7pyss3ykc7qkgr", "https://ais-pre-m6rwtgks7pyss3ykc7qkgr-835267516178.asia-southeast1.run.app"],
    [375, "Terminal 375", "mpr626sg2zhfouudazw4l2", "https://ais-pre-mpr626sg2zhfouudazw4l2-835267516178.asia-southeast1.run.app"],
    [376, "Terminal 376", "wirkpco7taropjzmzvdxf6", "https://ais-pre-wirkpco7taropjzmzvdxf6-835267516178.asia-southeast1.run.app"],
    [377, "Terminal 377", "f5dtijs3yzeu6xbmjwgefi", "https://ais-pre-f5dtijs3yzeu6xbmjwgefi-835267516178.asia-southeast1.run.app"],
    [378, "Terminal 378", "42gui6777iwrypmrplyizd", "https://ais-pre-42gui6777iwrypmrplyizd-835267516178.asia-southeast1.run.app"],
    [379, "Terminal 379", "w6xztbgd66v7vmcg5yt2i7", "https://ais-pre-w6xztbgd66v7vmcg5yt2i7-835267516178.asia-southeast1.run.app"],
    [380, "Terminal 380", "uipfytwsd2xp5esfkwrneq", "https://ais-pre-uipfytwsd2xp5esfkwrneq-835267516178.asia-southeast1.run.app"],
    [381, "Terminal 381", "oghjwnecpu44gkg36363eo", "https://ais-pre-oghjwnecpu44gkg36363eo-835267516178.asia-southeast1.run.app"],
    [382, "Terminal 382", "s23ns6vwocw6h4ht6foxfm", "https://ais-pre-s23ns6vwocw6h4ht6foxfm-835267516178.asia-southeast1.run.app"],
    [383, "Terminal 383", "rttm7hviybxjzwt5y7gu5n", "https://ais-pre-rttm7hviybxjzwt5y7gu5n-835267516178.asia-southeast1.run.app"],
    [384, "Terminal 384", "rkcchhd33hiivsdp3xneat", "https://ais-pre-rkcchhd33hiivsdp3xneat-835267516178.asia-southeast1.run.app"],
    [385, "Terminal 385", "zypukt7rv5iazx7vbykol7", "https://ais-pre-zypukt7rv5iazx7vbykol7-835267516178.asia-southeast1.run.app"],
    [386, "Terminal 386", "2mcrrasmd6gpclsvv6wr2p", "https://ais-pre-2mcrrasmd6gpclsvv6wr2p-835267516178.asia-southeast1.run.app"],
    [387, "Terminal 387", "5fam3kybbnz2txyb3qypkq", "https://ais-pre-5fam3kybbnz2txyb3qypkq-835267516178.asia-southeast1.run.app"],
    [388, "Terminal 388", "bmsj2nkuh7xvd7nhxsm5zl", "https://ais-pre-bmsj2nkuh7xvd7nhxsm5zl-835267516178.asia-southeast1.run.app"],
    [389, "Terminal 389", "niisfzl25znbsskitpwwge", "https://ais-pre-niisfzl25znbsskitpwwge-835267516178.asia-southeast1.run.app"],
    [390, "Terminal 390", "n7zldlnyyppwf2vdvanxm5", "https://ais-pre-n7zldlnyyppwf2vdvanxm5-835267516178.asia-southeast1.run.app"],
]

# ==================== W14: TERMINALS 391-420 ====================
W14_TERMINALS = [
    [391, "Terminal 391", "4yhj4pf4wudtpeaqpz4v25", "https://ais-pre-4yhj4pf4wudtpeaqpz4v25-877252276767.asia-southeast1.run.app"],
    [392, "Terminal 392", "vngbim3xorq2sw2fl5rf44", "https://ais-pre-vngbim3xorq2sw2fl5rf44-877252276767.asia-southeast1.run.app"],
    [393, "Terminal 393", "cwpip3ryfjsnvwvruqpq6a", "https://ais-pre-cwpip3ryfjsnvwvruqpq6a-877252276767.asia-southeast1.run.app"],
    [394, "Terminal 394", "c3afizulsycdhclyznycca", "https://ais-pre-c3afizulsycdhclyznycca-877252276767.asia-southeast1.run.app"],
    [395, "Terminal 395", "qcldv4om2aaj6rpjcqvqjd", "https://ais-pre-qcldv4om2aaj6rpjcqvqjd-877252276767.asia-southeast1.run.app"],
    [396, "Terminal 396", "ky66z7ikwh724ld3wmnnpz", "https://ais-pre-ky66z7ikwh724ld3wmnnpz-877252276767.asia-southeast1.run.app"],
    [397, "Terminal 397", "bfqpepuzqyq6qunmrwadtt", "https://ais-pre-bfqpepuzqyq6qunmrwadtt-877252276767.asia-southeast1.run.app"],
    [398, "Terminal 398", "bruntdwhhlglcmnuee3nqh", "https://ais-pre-bruntdwhhlglcmnuee3nqh-877252276767.asia-southeast1.run.app"],
    [399, "Terminal 399", "4uje4hmr35eja3ium2yhwd", "https://ais-pre-4uje4hmr35eja3ium2yhwd-877252276767.asia-southeast1.run.app"],
    [400, "Terminal 400", "tbfz7ksk2wujfjt2gdzoxz", "https://ais-pre-tbfz7ksk2wujfjt2gdzoxz-877252276767.asia-southeast1.run.app"],
    [401, "Terminal 401", "srbubxy7zcb6ki2jviriwq", "https://ais-pre-srbubxy7zcb6ki2jviriwq-877252276767.asia-southeast1.run.app"],
    [402, "Terminal 402", "5bifwab3al7reqtiypaloo", "https://ais-pre-5bifwab3al7reqtiypaloo-877252276767.asia-southeast1.run.app"],
    [403, "Terminal 403", "ylkljbqenmfk4vrhiclqqp", "https://ais-pre-ylkljbqenmfk4vrhiclqqp-877252276767.asia-southeast1.run.app"],
    [404, "Terminal 404", "s5lmyrza47alwhz2ryhuje", "https://ais-pre-s5lmyrza47alwhz2ryhuje-877252276767.asia-southeast1.run.app"],
    [405, "Terminal 405", "7thh23gecimg52got3mycv", "https://ais-pre-7thh23gecimg52got3mycv-877252276767.asia-southeast1.run.app"],
    [406, "Terminal 406", "l3ell6bqkhyrd36r67a25e", "https://ais-pre-l3ell6bqkhyrd36r67a25e-877252276767.asia-southeast1.run.app"],
    [407, "Terminal 407", "griw3lwh4sn2aoptihkilp", "https://ais-pre-griw3lwh4sn2aoptihkilp-877252276767.asia-southeast1.run.app"],
    [408, "Terminal 408", "uram4ptgrix3553uggndlf", "https://ais-pre-uram4ptgrix3553uggndlf-877252276767.asia-southeast1.run.app"],
    [409, "Terminal 409", "pgjsiuxlihpo2uqd223hrg", "https://ais-pre-pgjsiuxlihpo2uqd223hrg-877252276767.asia-southeast1.run.app"],
    [410, "Terminal 410", "mqwgyvdund6kuy2yb7ni35", "https://ais-pre-mqwgyvdund6kuy2yb7ni35-877252276767.asia-southeast1.run.app"],
    [411, "Terminal 411", "6ndx7ftsrnqaj7tjhglxpa", "https://ais-pre-6ndx7ftsrnqaj7tjhglxpa-877252276767.asia-southeast1.run.app"],
    [412, "Terminal 412", "okeqchbp53ccu2yfysyqpl", "https://ais-pre-okeqchbp53ccu2yfysyqpl-877252276767.asia-southeast1.run.app"],
    [413, "Terminal 413", "wzuubl7ky44et46s3eq44w", "https://ais-pre-wzuubl7ky44et46s3eq44w-877252276767.asia-southeast1.run.app"],
    [414, "Terminal 414", "ly5i3dia37ioqk2g3unv6h", "https://ais-pre-ly5i3dia37ioqk2g3unv6h-877252276767.asia-southeast1.run.app"],
    [415, "Terminal 415", "efpjkyz3sdjlcq4jhdremh", "https://ais-pre-efpjkyz3sdjlcq4jhdremh-877252276767.asia-southeast1.run.app"],
    [416, "Terminal 416", "mlneqdjkaudm3yn4wakk4g", "https://ais-pre-mlneqdjkaudm3yn4wakk4g-877252276767.asia-southeast1.run.app"],
    [417, "Terminal 417", "acukqhyaozux44cnp65lhf", "https://ais-pre-acukqhyaozux44cnp65lhf-877252276767.asia-southeast1.run.app"],
    [418, "Terminal 418", "j4kwvlrqiurr24wqi42ain", "https://ais-pre-j4kwvlrqiurr24wqi42ain-877252276767.asia-southeast1.run.app"],
    [419, "Terminal 419", "qbsydzzxgdmebwelpzxjj3", "https://ais-pre-qbsydzzxgdmebwelpzxjj3-877252276767.asia-southeast1.run.app"],
    [420, "Terminal 420", "gv7gqtnctyazhhm77ru2y2", "https://ais-pre-gv7gqtnctyazhhm77ru2y2-877252276767.asia-southeast1.run.app"],
]

# ==================== W15: TERMINALS 421-450 ====================
W15_TERMINALS = [
    [421, "Terminal 421", "3bycrrearrf77brqign5wm", "https://ais-pre-3bycrrearrf77brqign5wm-81633053786.asia-southeast1.run.app"],
    [422, "Terminal 422", "4cebz7inuuriuggeajgpjq", "https://ais-pre-4cebz7inuuriuggeajgpjq-81633053786.asia-southeast1.run.app"],
    [423, "Terminal 423", "5xx4hw7y2aota7phfinz3e", "https://ais-pre-5xx4hw7y2aota7phfinz3e-81633053786.asia-southeast1.run.app"],
    [424, "Terminal 424", "2nedcltowyfkmgm5gyjoj3", "https://ais-pre-2nedcltowyfkmgm5gyjoj3-81633053786.asia-southeast1.run.app"],
    [425, "Terminal 425", "vn54uzbdxgziipoukcudvj", "https://ais-pre-vn54uzbdxgziipoukcudvj-81633053786.asia-southeast1.run.app"],
    [426, "Terminal 426", "wrak72scktiu6npqhif7zr", "https://ais-pre-wrak72scktiu6npqhif7zr-81633053786.asia-southeast1.run.app"],
    [427, "Terminal 427", "nojd4odygycponibanovvb", "https://ais-pre-nojd4odygycponibanovvb-81633053786.asia-southeast1.run.app"],
    [428, "Terminal 428", "dku3wak2m365gbusfp6z27", "https://ais-pre-dku3wak2m365gbusfp6z27-81633053786.asia-southeast1.run.app"],
    [429, "Terminal 429", "7vsvsmgmfsqm3qkert7q4o", "https://ais-pre-7vsvsmgmfsqm3qkert7q4o-81633053786.asia-southeast1.run.app"],
    [430, "Terminal 430", "u4xehnjingwavsdaj5vnpx", "https://ais-pre-u4xehnjingwavsdaj5vnpx-81633053786.asia-southeast1.run.app"],
    [431, "Terminal 431", "pq67672bf7iihfcklqoopr", "https://ais-pre-pq67672bf7iihfcklqoopr-81633053786.asia-southeast1.run.app"],
    [432, "Terminal 432", "3g757y2jhthl7yvqoapj2k", "https://ais-pre-3g757y2jhthl7yvqoapj2k-81633053786.asia-southeast1.run.app"],
    [433, "Terminal 433", "i26ue7optybau3jeg3wa2h", "https://ais-pre-i26ue7optybau3jeg3wa2h-81633053786.asia-southeast1.run.app"],
    [434, "Terminal 434", "25fwvmdja3uoqjx4krjiio", "https://ais-pre-25fwvmdja3uoqjx4krjiio-81633053786.asia-southeast1.run.app"],
    [435, "Terminal 435", "636p6boz6vg3nvseehtvc4", "https://ais-pre-636p6boz6vg3nvseehtvc4-81633053786.asia-southeast1.run.app"],
    [436, "Terminal 436", "4fgwb5hancb3k24aifhtd6", "https://ais-pre-4fgwb5hancb3k24aifhtd6-81633053786.asia-southeast1.run.app"],
    [437, "Terminal 437", "alzmw6u6734p5fuz32fwqh", "https://ais-pre-alzmw6u6734p5fuz32fwqh-81633053786.asia-southeast1.run.app"],
    [438, "Terminal 438", "zxazevtgjsld7fwqkehvzk", "https://ais-pre-zxazevtgjsld7fwqkehvzk-81633053786.asia-southeast1.run.app"],
    [439, "Terminal 439", "quywomyd6jbzzl7sexoeke", "https://ais-pre-quywomyd6jbzzl7sexoeke-81633053786.asia-southeast1.run.app"],
    [440, "Terminal 440", "4l7zaasyoz4brsq3di3ygo", "https://ais-pre-4l7zaasyoz4brsq3di3ygo-81633053786.asia-southeast1.run.app"],
    [441, "Terminal 441", "vkppx7vycpulbp72wp6axr", "https://ais-pre-vkppx7vycpulbp72wp6axr-81633053786.asia-southeast1.run.app"],
    [442, "Terminal 442", "vhiimgmukyllnrus2etzv7", "https://ais-pre-vhiimgmukyllnrus2etzv7-81633053786.asia-southeast1.run.app"],
    [443, "Terminal 443", "7fns4fr3fg5e5ytdnrfyya", "https://ais-pre-7fns4fr3fg5e5ytdnrfyya-81633053786.asia-southeast1.run.app"],
    [444, "Terminal 444", "xkjrbnuuhed5zl6dibruon", "https://ais-pre-xkjrbnuuhed5zl6dibruon-81633053786.asia-southeast1.run.app"],
    [445, "Terminal 445", "vtw2hfhr33r5ws56lpv2zo", "https://ais-pre-vtw2hfhr33r5ws56lpv2zo-81633053786.asia-southeast1.run.app"],
    [446, "Terminal 446", "vwupeosw3x65hvdnwrtydi", "https://ais-pre-vwupeosw3x65hvdnwrtydi-81633053786.asia-southeast1.run.app"],
    [447, "Terminal 447", "5xbahwvghys7j2bq3rwaxp", "https://ais-pre-5xbahwvghys7j2bq3rwaxp-81633053786.asia-southeast1.run.app"],
    [448, "Terminal 448", "nhh77relz2ipopebylmnkm", "https://ais-pre-nhh77relz2ipopebylmnkm-81633053786.asia-southeast1.run.app"],
    [449, "Terminal 449", "sgnvsm2e6o4ms2xjauxgct", "https://ais-pre-sgnvsm2e6o4ms2xjauxgct-81633053786.asia-southeast1.run.app"],
    [450, "Terminal 450", "yfb7576xfjcf6kflnw2a6v", "https://ais-pre-yfb7576xfjcf6kflnw2a6v-81633053786.asia-southeast1.run.app"],
]

# ==================== FUNCTIONS ====================
def log(msg): print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")
def send_tg(title, msg, emoji="📘"): telegram.send_message(f"{emoji} <b>{title}</b>\n{msg}")
def get_system_info():
    try:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        return f"CPU: {cpu}% | RAM: {ram.used/(1024**3):.1f}/{ram.total/(1024**3):.1f}GB ({ram.percent}%)"
    except:
        return "N/A"

def take_screenshot(filename="screenshot.png"):
    try:
        screenshot = ImageGrab.grab()
        screenshot.save(filename)
        return filename
    except:
        return None

def get_uuid():
    try:
        r = requests.get(f"{API_BASE}/address/{WALLET_ADDRESS}?coin={COIN}", headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
        return r.json().get('data', {}).get('uuid')
    except:
        return None

def check_status(miner_name, uuid):
    try:
        r = requests.get(f"{API_BASE}/account/{uuid}/workers", headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
        workers = r.json().get('data', {}).get('randomx', {}).get('workers', [])
        for w in workers:
            if w.get('name') == miner_name:
                return w.get('online', False)
        return False
    except:
        return False

def open_window(url, name):
    try:
        subprocess.Popen([FIREFOX_PATH, "-new-window", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except:
        return False

def close_window(miner_name):
    try:
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            if proc.info['name'] == 'firefox.exe' and miner_name in str(proc.info['cmdline']):
                proc.terminate()
                return True
    except:
        pass
    return False

def run_workflow(terminals, workflow_name):
    if not os.path.exists(FIREFOX_PATH):
        send_tg("ERROR", "Firefox not found!", "❌")
        return
    
    total = len(terminals)
    batches = (total + BATCH_SIZE - 1) // BATCH_SIZE
    
    log(f"{workflow_name} Started | Total: {total}")
    send_tg("WORKFLOW STARTED", f"{workflow_name}\nTotal: {total}\n{get_system_info()}", "🚀")
    
    uuid = get_uuid()
    if not uuid:
        send_tg("ERROR", "Failed to get UUID!", "❌")
        return
    
    # Open first batch (for screenshot)
    log("Opening BATCH 1...")
    first_batch = terminals[0:BATCH_SIZE]
    for m in first_batch:
        open_window(m[3], m[1])
        time.sleep(2)
    
    time.sleep(30)
    ss = take_screenshot(f"screenshot_{workflow_name.replace(' ', '_')}.png")
    if ss:
        caption = f"📸 BATCH 1 SCREENSHOT\n{workflow_name}\n{get_system_info()}"
        telegram.send_photo(ss, caption)
    
    time.sleep(GAP_BETWEEN_BATCHES)
    
    # Open remaining batches
    for b in range(1, batches):
        start = b * BATCH_SIZE
        end = min(start + BATCH_SIZE, total)
        for m in terminals[start:end]:
            open_window(m[3], m[1])
            time.sleep(2)
        if end < total:
            time.sleep(GAP_BETWEEN_BATCHES)
    
    log("All terminals opened!")
    send_tg("ALL OPENED", f"All {total} terminals opened!\n{get_system_info()}", "✅")
    
    # Monitoring loop
    while True:
        time.sleep(CHECK_INTERVAL)
        offline, online = [], 0
        for m in terminals:
            if check_status(m[2], uuid):
                online += 1
            else:
                offline.append(m)
        
        if offline:
            send_tg(f"STATUS - {len(offline)} OFFLINE", f"{workflow_name}: {online}/{total} ONLINE\n{get_system_info()}", "⚠️")
            for m in offline:
                close_window(m[2])
                time.sleep(2)
                open_window(m[3], m[1])
                time.sleep(3)
            send_tg("RESTART COMPLETE", f"Restarted {len(offline)} miners", "✅")
        else:
            send_tg("STATUS - ALL ONLINE", f"{workflow_name}: {online}/{total} ONLINE (100%)\n{get_system_info()}", "✅")

# ==================== MAIN ====================
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--workflow', type=str, default='W13')
    args = parser.parse_args()
    
    if args.workflow == 'W13':
        run_workflow(W13_TERMINALS, "W13 (361-390)")
    elif args.workflow == 'W14':
        run_workflow(W14_TERMINALS, "W14 (391-420)")
    elif args.workflow == 'W15':
        run_workflow(W15_TERMINALS, "W15 (421-450)")
    else:
        print("Use --workflow W13, W14, or W15")
