import time
from datetime import datetime as dt
import pandas
hosts_path  =   r"C:\Windows\System32\drivers\etc\hosts"
hosts_temp  =   r"hosts"
redirect="127.0.0.1"
df      =   pandas.read_csv("websites.txt")
year    =   dt.now().year
month   =   dt.now().month
day     =   dt.now().day
st_time =   8
en_time =   20
while True:
    if(dt(year,month,day,st_time) < dt.now() < dt(year,month,day,en_time)):
        with open(hosts_path, "r+") as file:
            content =   file.read()
            for website in df["WEBSITES"]:
                if(website in content):
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, "r+") as file:
            content =   file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in df["WEBSITES"]):
                    file.write(line)
            file.truncate()
    time.sleep(5)
