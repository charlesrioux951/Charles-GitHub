import os

def get_os_status():
    status = os.uname()
    return {
        "sysname": status.sysname,
        "nodename": status.nodename,
        "release": status.release,
        "version": status.version,
        "machine": status.machine
    }

if __name__ == "__main__":
    os_status = get_os_status()
    for key, value in os_status.items():
        print(f"{key}: {value}")