import os  
import sys  
import datetime  
import calendar  
import glob  
import time  
import platform  
  
def display_current_working_directory():  
    cwd = os.getcwd()  
    print(f"Current Working Directory: {cwd}")  
  
def display_login_name():  
    try:  
        login_name = os.getlogin()  
    except Exception:  
        # Fallback for environments where os.getlogin() may fail  
        login_name = os.environ.get('USERNAME') or os.environ.get('USER')  
    print(f"Login Name: {login_name}")  
  
def display_all_environment_variables():  
    print("\nAll Environment Variables:")  
    for key, value in os.environ.items():  
        print(f"{key}: {value}")  
  
def display_todays_date():  
    today = datetime.datetime.now()  
    print(f"\nToday's Date (Timestamp): {today}")  
  
def display_september_calendar(year=None):  
    if not year:  
        year = datetime.datetime.now().year  
    print(f"\nSeptember Calendar for {year}:\n")  
    sept_calendar = calendar.month(year, 9)  
    print(sept_calendar)  
  
def display_py_files_and_sizes(directory='.'):  
    print("\nAll .py Files and Their Sizes in Bytes:")  
    py_files = glob.glob(os.path.join(directory, '*.py'))  
    if not py_files:  
        print("No .py files found.")  
    for file in py_files:  
        size = os.path.getsize(file)  
        print(f"{file}: {size} bytes")  
  
def display_modified_time(file_path='employees.csv'):  
    if os.path.exists(file_path):  
        modified_time = time.ctime(os.path.getmtime(file_path))  
        print(f"\nModified Time of '{file_path}': {modified_time}")  
    else:  
        print(f"\nFile '{file_path}' does not exist.")  
  
def display_current_process_id():  
    pid = os.getpid()  
    print(f"\nCurrent Process ID: {pid}")  
  
def set_environment_variable(key='TEST_PATH', value='C:/Users/Admin/'):  
    os.environ[key] = value  
    print(f"\nEnvironment Variable Set: {key} = {os.environ[key]}")  
  
def lock_and_unlock_file(file_path='sample.lock'):  
    # Note: File locking differs between operating systems  
    # This example uses a simple lock mechanism using os.open and os.close  
    print(f"\nLocking file: {file_path}")  
    fd = os.open(file_path, os.O_CREAT | os.O_RDWR)  
    print(f"File '{file_path}' locked with file descriptor {fd}")  
      
    # Simulate some operation while the file is locked  
    time.sleep(2)  
      
    os.close(fd)  
    print(f"File '{file_path}' unlocked.")  
  
def retrieve_load_average():  
    if hasattr(os, 'getloadavg'):  
        load1, load5, load15 = os.getloadavg()  
        print(f"\nSystem Load Average: 1min={load1}, 5min={load5}, 15min={load15}")  
    else:  
        print("\nLoad average not supported on this operating system.")  
  
def display_python_version():  
    version = sys.version  
    print(f"\nPython Version:\n{version}")  
  
def main():  
    print("### Python Standard Library Operations ###\n")  
    display_current_working_directory() #     cwd = os.getcwd()   
    display_login_name()  #         login_name = os.getlogin()  
    display_all_environment_variables()  #     for key, value in os.environ.items():  
    display_todays_date()      # today = datetime.datetime.now()  
    display_september_calendar()  #     sept_calendar = calendar.month(year, 9)  
    display_py_files_and_sizes()  
    display_modified_time()  
    display_current_process_id()  
    set_environment_variable()  
    lock_and_unlock_file()  
    retrieve_load_average()  
    display_python_version()  
  
if __name__ == "__main__":  
    main()  