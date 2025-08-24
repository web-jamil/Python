# # import subprocess
# # import socket
# # import os

# # # Get saved Wi-Fi profiles and passwords
# # data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
# # profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

# # print("\nSaved Wi-Fi Profiles and Passwords:\n")
# # for i in profiles:
# #     try:
# #         results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
# #         results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
# #         try:
# #             print("{:<30}|  {:<}".format(i, results[0]))
# #         except IndexError:
# #             print("{:<30}|  {:<}".format(i, ""))
# #     except subprocess.CalledProcessError:
# #         print("{:<30}|  {:<}".format(i, "ENCODING ERROR"))

# # # Get default gateway (router IP)
# # print("\nRouter Login Info:\n")
# # gateway_data = subprocess.check_output("ipconfig", shell=True).decode()
# # for line in gateway_data.split('\n'):
# #     if "Default Gateway" in line:
# #         router_ip = line.split(":")[1].strip()
# #         break
# # else:
# #     router_ip = "Not found"

# # print("Router IP Address: {}".format(router_ip))
# # print("Default Login (if unchanged):")
# # print("  Username: admin")
# # print("  Password: admin")

# # input("\nPress Enter to exit...")


# import subprocess
# import re
# import ipaddress

# def get_wifi_profiles():
#     output = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True)
#     return re.findall(r"All User Profile\s*:\s*(.*)", output.stdout)

# def get_wifi_password(profile):
#     try:
#         result = subprocess.run(
#             ['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'],
#             capture_output=True, text=True
#         )
#         match = re.search(r"Key Content\s*:\s*(.*)", result.stdout)
#         return match.group(1) if match else ""
#     except subprocess.CalledProcessError:
#         return "ERROR"

# def get_default_gateway():
#     output = subprocess.run("ipconfig", shell=True, capture_output=True, text=True).stdout
#     match = re.search(r"Default Gateway\s*:\s*(\d+\.\d+\.\d+\.\d+)", output)
#     if match:
#         ip = match.group(1)
#         try:
#             return str(ipaddress.ip_address(ip))
#         except ValueError:
#             return "Invalid IP"
#     return "Not Found"

# def main():
#     print("\n📶 Saved Wi-Fi Profiles and Passwords:\n")
#     for profile in get_wifi_profiles():
#         password = get_wifi_password(profile)
#         print(f"{profile:<30} | {password}")

#     print("\n🌐 Router Login Info:\n")
#     router_ip = get_default_gateway()
#     print(f"Router IP Address: {router_ip}")
#     print("Default Login (if unchanged):")
#     print("  Username: admin")
#     print("  Password: admin")

# if __name__ == "__main__":
#     main()
#     input("\nPress Enter to exit...")


import subprocess
import re
import ipaddress

class WifiProfile:
    def __init__(self, name):
        self.name = name
        self.password = self._get_password()

    def _get_password(self):
        try:
            result = subprocess.run(
                ['netsh', 'wlan', 'show', 'profile', self.name, 'key=clear'],
                capture_output=True, text=True
            )
            match = re.search(r"Key Content\s*:\s*(.*)", result.stdout)
            return match.group(1) if match else ""
        except subprocess.CalledProcessError:
            return "ERROR"

    def display(self):
        print(f"{self.name:<30} | {self.password}")

class RouterInfo:
    def __init__(self):
        self.ip = self._get_default_gateway()

    def _get_default_gateway(self):
        output = subprocess.run("ipconfig", shell=True, capture_output=True, text=True).stdout
        match = re.search(r"Default Gateway\s*:\s*(\d+\.\d+\.\d+\.\d+)", output)
        if match:
            ip = match.group(1)
            try:
                return str(ipaddress.ip_address(ip))
            except ValueError:
                return "Invalid IP"
        return "Not Found"

    def display(self):
        print("\n🌐 Router Login Info:\n")
        print(f"Router IP Address: {self.ip}")
        print("Default Login (if unchanged):")
        print("  Username: admin")
        print("  Password: admin")

class WifiManager:
    def __init__(self):
        self.profiles = self._get_profiles()

    def _get_profiles(self):
        output = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True)
        profile_names = re.findall(r"All User Profile\s*:\s*(.*)", output.stdout)
        return [WifiProfile(name.strip()) for name in profile_names]

    def display_profiles(self):
        print("\n📶 Saved Wi-Fi Profiles and Passwords:\n")
        for profile in self.profiles:
            profile.display()

def main():
    manager = WifiManager()
    manager.display_profiles()

    router = RouterInfo()
    router.display()

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()