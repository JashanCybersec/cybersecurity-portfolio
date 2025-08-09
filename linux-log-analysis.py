import re

def parse_auth_log(filename):
    failed_logins = {}
    with open(filename, 'r') as file:
        for line in file:
            if 'Failed password' in line:
                ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
                if ip_match:
                    ip = ip_match.group(1)
                    failed_logins[ip] = failed_logins.get(ip, 0) + 1
    return failed_logins

if __name__ == "__main__":
    log_file = 'auth.log'
    failed = parse_auth_log(log_file)
    print("Failed SSH login attempts:")
    for ip, count in failed.items():
        print(f"{ip}: {count} times")
