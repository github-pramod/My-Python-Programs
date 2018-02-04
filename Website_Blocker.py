import time
from datetime import datetime as dt

host_path = r"C:\Windows\System32\drivers\etc\hosts"
host_temp = "hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com"]  # list of websites to be blocked

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 11) < dt.now() < dt(dt.now().year, dt.now().month,
       dt.now().day, 12):  # the time duration you want the sites to be blocked.
        print("Working hours!!")
        with open(host_path, 'r+') as file:  # opening the host_path in read and append mode.
            content = file.read()  # reading the contents of the file
            for website in website_list:  # iterating over the website_list mentioned above.
                if website in content:
                    pass  # if the website is already present in the file do nothing
                else:
                    file.write(redirect + " " + website + "\n")
    else:  # if the time is not within the above mentioned range
        with open(host_path, 'r+') as file:  # opening the host_path in read and append mode.
            content = file.readlines()  # reading lines of the file
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):  # this will exclude the websites from the file, if present.
                    file.write(line)  # write the content excluding the websites
            file.truncate()  # truncate the file.
        print("Free Time")

    time.sleep(5)
