import subprocess
import time,os


def login():
    name = input("User : ")
    password = input(f"Password[{name}]: ")
    if password == "root":
        cool()
        time.sleep(.5)
        run()
    else:
        print("Unauthorised access............#############")


def run():
    i = 0
    while i<1:
        take = input("wfi: ")
        if take == "show":
            subprocess.run(['notepad', 'data.txt'])
        if take == "clear":
            os.remove("data.txt")
            print("Deleting......")
        if take == "show file":
            subprocess.run(["attrib", "-r", "-s", "-h", "data.txt"])
        if take == "q" or take=="exit":
            i+=1


def cool():
    list = ["Storage", "Drives", "os", "python", "process-algo"]
    print("Getting things ready..............")
    for i in range(5):
        print(f"Getting {list[i]} ready........")
        time.sleep(.3)
        print("Searching storage..........." + ".")
    print("finalizing..........")
    print("                                             Done                                        ")
if __name__ == '__main__':
    login()