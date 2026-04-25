import pydirectinput
import time
import keyboard
import math
import random

# --- INITIAL SETTINGS ---
intensity = 50    
frequency = 0.5   
jitter_strength = 5 
# ------------------------

enabled = False
last_toggle = 0

# Static art printed once at the start
cat_art = r"""
      .--.            .--.
     ( (`\\. "--``--".//`) )
      '-.   __   __    .-'
       /   /__\ /__\   \
      |     \ 0/ \ 0/    |
       \      `/   \`      /
        `-.  /-""" + '"' + r"""-\  .-`
          /  '.___.'  \
          \      I      /
           `;--'`'--;`
            '.___.'
"""

def toggle():
    global enabled, last_toggle
    if time.time() - last_toggle > 0.3:
        enabled = not enabled
        last_toggle = time.time()
        status = "ENABLED" if enabled else "DISABLED"
        print(f" >> SYSTEM {status}")

keyboard.add_hotkey('insert', toggle)

print(cat_art)
print("--- LAG-FREE MODE ACTIVE ---")
print("Controls: Q/E (Speed), Z/C (Width), INSERT (Toggle)")
print("Ready...")

try:
    t = 0
    while True:
        # Check for Q (Speed Up)
        if keyboard.is_pressed('q'):
            frequency += 0.05
            print(f" [+] Speed: {frequency:.2f}")
            time.sleep(0.12)
            
        # Check for E (Speed Down)
        if keyboard.is_pressed('e'):
            frequency = max(0.01, frequency - 0.05)
            print(f" [-] Speed: {frequency:.2f}")
            time.sleep(0.12)

        # Check for Z (Width Up)
        if keyboard.is_pressed('z'):
            intensity += 5
            print(f" [>] Width: {intensity}")
            time.sleep(0.12)
            
        # Check for C (Width Down)
        if keyboard.is_pressed('c'):
            intensity = max(1, intensity - 5)
            print(f" [<] Width: {intensity}")
            time.sleep(0.12)

        if enabled:
            # High-performance movement
            move_val = math.cos(t) * intensity
            jitter = random.randint(-jitter_strength, jitter_strength)
            
            # Use relative movement without extra delays
            pydirectinput.moveRel(int(move_val) + jitter, 0, relative=True)
            
            t += frequency
        else:
            # Idle state uses very little CPU
            time.sleep(0.01)
        
        # This tiny sleep is the "heartbeat" of the script
        # 0.0001 is much faster than 0.001 to prevent lag
        time.sleep(0.0001)

except KeyboardInterrupt:
    print("\nClosing...")
