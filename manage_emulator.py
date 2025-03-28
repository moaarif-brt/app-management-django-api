import subprocess
import time

AVD_NAME = "Pixel_4_API_30"  # Replace with your AVD name in my case Pixel_4_API_30
APK_PATH = "C:\Users\Aarif\Desktop\Project\sample.apk"  # Replace with your APK pathn in my case C:\Users\Aarif\Desktop\Project\sample.apk

def start_emulator():
    subprocess.Popen(["emulator", "-avd", AVD_NAME])
    print("Starting emulator...")
    subprocess.run(["adb", "wait-for-device"])
    while True:
        output = subprocess.check_output(["adb", "shell", "getprop", "sys.boot_completed"]).decode().strip()
        if output == "1":
            break
        time.sleep(1)
    print("Emulator booted.")

def install_apk():
    subprocess.run(["adb", "install", APK_PATH])
    print(f"Installed APK: {APK_PATH}")

def get_system_info():
    os_version = subprocess.check_output(["adb", "shell", "getprop", "ro.build.version.release"]).decode().strip()
    device_model = subprocess.check_output(["adb", "shell", "getprop", "ro.product.model"]).decode().strip()
    print(f"OS Version: {os_version}")
    print(f"Device Model: {device_model}")

if __name__ == "__main__":
    start_emulator()
    install_apk()
    get_system_info()