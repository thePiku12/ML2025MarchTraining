import psutil  
import socket  
  
def display_cpu_usage():  
    cpu_percent = psutil.cpu_percent(interval=1)  
    print(f"CPU Usage: {cpu_percent}%")  
  
def display_memory_info():  
    mem = psutil.virtual_memory()  
    print(f"\nMemory Info:")  
    print(f"  Total: {get_size(mem.total)}")  
    print(f"  Available: {get_size(mem.available)}")  
    print(f"  Used: {get_size(mem.used)}")  
    print(f"  Percentage: {mem.percent}%")  
  
def display_process_info():  
    print("\nTop 5 Processes by CPU Usage:")  
    processes = []  
    for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent']):  
        try:  
            processes.append(proc.info)  
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):  
            pass  
    # Sort processes by CPU percent in descending order  
    processes = sorted(processes, key=lambda procObj: procObj['cpu_percent'] or 0, reverse=True)  
    for proc in processes[:5]:  
        print(f"PID: {proc['pid']}, Name: {proc['name']}, User: {proc['username']}, CPU Usage: {proc['cpu_percent']}%")  
  
def display_disk_partitions():  
    print("\nDisk Partitions and Usage:")  
    partitions = psutil.disk_partitions()  
    for partition in partitions:  
        print(f"  Device: {partition.device}")  
        print(f"    Mountpoint: {partition.mountpoint}")  
        print(f"    File system type: {partition.fstype}")  
        try:  
            partition_usage = psutil.disk_usage(partition.mountpoint)  
            print(f"    Total Size: {get_size(partition_usage.total)}")  
            print(f"    Used: {get_size(partition_usage.used)}")  
            print(f"    Free: {get_size(partition_usage.free)}")  
            print(f"    Percentage: {partition_usage.percent}%")  
        except PermissionError:  
            print("    No permission to access this partition.")  
  
def display_network_statistics():  
    print("\nNetwork Statistics:")  
    net_io = psutil.net_io_counters()  
    print(f"  Total Bytes Sent: {get_size(net_io.bytes_sent)}")  
    print(f"  Total Bytes Received: {get_size(net_io.bytes_recv)}")  
    print(f"  Packets Sent: {net_io.packets_sent}")  
    print(f"  Packets Received: {net_io.packets_recv}")  
  
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
  
def main():  
    print("### psutil Library Operations ###\n")  
    display_cpu_usage()  
    display_memory_info()  
    display_process_info()  
    display_disk_partitions()  
    display_network_statistics()  
  
if __name__ == "__main__":  
    main()  