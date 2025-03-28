import subprocess
import requests

def get_system_info():
    device_id = subprocess.check_output(["adb", "shell", "getprop", "ro.serialno"]).decode().strip()
    os_version = subprocess.check_output(["adb", "shell", "getprop", "ro.build.version.release"]).decode().strip()
    device_model = subprocess.check_output(["adb", "shell", "getprop", "ro.product.model"]).decode().strip()
    return {
        "device_id": device_id,
        "os_version": os_version,
        "device_model": device_model
    }

if __name__ == "__main__":
    system_info = get_system_info()
    payload = {
        "app_name": "TestApp",
        "version": "1.0",
        "description": "A test app from emulator",
        **system_info  # Add system info to payload
    }
    response = requests.post("http://localhost:8000/api/create-app/", json=payload)
    print(f"Response Status: {response.status_code}")
    print(f"Response Body: {response.text}")