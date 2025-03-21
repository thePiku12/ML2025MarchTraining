import os  
import sys  
import platform  
import socket  
import uuid  
import psutil  
import time  
from datetime import timedelta  
import threading  
  
def display_os_name():  
    os_name = platform.system()  
    print(f"OS Name: {os_name}")  
  
def display_python_version():  
    python_version = sys.version  
    print(f"Python Version:\n{python_version}")  
  
def display_processor_details():  
    processor = platform.processor()  
    if not processor:  
        # Fallback for some operating systems  
        processor = platform.machine()  
    print(f"Processor Details: {processor}")  
  
def display_system_architecture():  
    architecture = platform.architecture()[0]  
    print(f"System Architecture: {architecture}")  
  
def display_system_hostname():  
    hostname = socket.gethostname()  
    print(f"System Hostname: {hostname}")  
  
def detect_operating_system():  
    os_system = platform.system()  
    if os_system == "Windows":  
        print("Operating System: Windows")  
    elif os_system == "Linux":  
        print("Operating System: Linux")  
    elif os_system == "Darwin":  
        print("Operating System: macOS")  
    else:  
        print(f"Operating System: {os_system}")  
  
def display_python_build_info():  
    build_info = platform.python_build()  
    compiler = platform.python_compiler()  
    print(f"Python Build Information: {build_info}")  
    print(f"Python Compiler: {compiler}")  
  
def fetch_mac_address():  
    mac_num = hex(uuid.getnode()).replace('0x', '').upper()  
    mac = ':'.join(mac_num[i:i+2] for i in range(0, 11, 2))  
    print(f"MAC Address: {mac}")  
  
def display_network_details():  
    hostname = socket.gethostname()  
    try:  
        ip_address = socket.gethostbyname(hostname)  
    except socket.gaierror:  
        ip_address = "Unable to get IP Address"  
    print(f"IP Address: {ip_address}")  
    print(f"Hostname: {hostname}")  
  
def monitor_system_uptime():  
    boot_time = psutil.boot_time()  
    current_time = time.time()  
    uptime_seconds = current_time - boot_time  
    uptime = timedelta(seconds=uptime_seconds)  
    print(f"System Uptime: {uptime}")  
  
def get_size(bytes, suffix="B"):  
    """  
    Scale bytes to its proper format  
    e.g.:  
        1253656 => '1.20MB'  
        1253656678 => '1.17GB'  
    """  
    factor = 1024  
    for unit in ["", "K", "M", "G", "T", "P"]:  
        if bytes < factor:  
            return f"{bytes:.2f}{unit}{suffix}"  
        bytes /= factor  
    return f"{bytes:.2f}P{suffix}"  
  
def display_real_time_usage(interval=1):  
    print("\nReal-Time System Monitoring (Press Ctrl+C to exit):")  
    try:  
        while True:  
            # CPU Usage  
            cpu_percent = psutil.cpu_percent(interval=interval)  
              
            # Memory Usage  
            memory = psutil.virtual_memory()  
            memory_used = get_size(memory.used)  
            memory_percent = memory.percent  
              
            # Disk Usage  
            disk = psutil.disk_usage('/')  
            disk_used = get_size(disk.used)  
            disk_percent = disk.percent  
              
            # Clear the previous output (optional, works on Unix)  
            # os.system('clear')  # For Linux/Mac  
            # os.system('cls')    # For Windows  
                  
            # Display the stats  
            print(f"CPU Usage: {cpu_percent}% | Memory Usage: {memory_used} ({memory_percent}%) | Disk Usage: {disk_used} ({disk_percent}%)")  
              
            # Sleep for the interval duration  
            time.sleep(interval)  
    except KeyboardInterrupt:  
        print("\nExiting Real-Time Monitoring.")  
  
def main():  
    print("### Comprehensive System Information ###\n")  
    display_os_name()  
    detect_operating_system()  
    display_python_version()  
    display_processor_details()  
    display_system_architecture()  
    display_system_hostname()  
    display_python_build_info()  
    fetch_mac_address()  
    display_network_details()  
    monitor_system_uptime()  
      
    # Start real-time monitoring in a separate thread (optional)  
    # For demonstration, we'll run real-time monitoring for 10 seconds  
    print("\n### Starting Real-Time Monitoring for 10 Seconds ###")  
    real_time_thread = threading.Thread(target=display_real_time_usage, args=(1,), daemon=True)  
    real_time_thread.start()  
    time.sleep(10)  
    print("\n### Real-Time Monitoring Ended ###")  
  
if __name__ == "__main__":  
    main()  