import datetime
from importlib.resources import contents
import time

# Function to get the website input
def website():
    site = []
    n = int(input("How many wesite do you want to block/unblock\n"))
    for i in range(0,n):
        website = str(input("Please enter the website you want to block\n"))
        site.append(website)
    return site

host_path = "/etc/hosts"
redirect = "127.0.0.1"

whatToDo = int(input("What do you want to do?\n1.Block\n2.Unblock\n"))
if whatToDo == 1:
    d = int(input("Please enter the day till you want to block this wesite\n"))
    m = int(input("Please enter the month till you want to block this wesite\n"))
    y = int(input("Please enter the year till you want to block this wesite\n"))

    end_time = datetime.datetime(y,m,d)

    site_block = website()

    if datetime.datetime.now() < end_time:
        print("Start Blocking")
        with open(host_path, "r+") as host_file:
            content = host_file.read()
            for website in site_block:
                if website not in content:
                    host_file.write("\n"+redirect+" "+website+"\n")
                else:
                    pass
    else:
        pass

elif whatToDo ==2:
    site_unblock = website()

    with open(host_path, "r+") as host_file:
        file_lines = host_file.readlines()
        host_file.seek(0)
        for site in site_unblock:
            for line in file_lines:
                if redirect+" "+site not in line:
                    host_file.write(line)
            host_file.truncate()
    
