import time

# User input
seconds = int(input("⏱️ Enter time in seconds: "))

while seconds > 0:
    mins = seconds // 60
    secs = seconds % 60
    timer = f"{mins:02d}:{secs:02d}"
    print("⏳ Time Left:", timer, end="\r")
    time.sleep(1)
    seconds -= 1

print("\n⏰ Time's up!")
