#Written and managed by Mukesh Bahuguna
from subprocess import Popen, PIPE
import sys
import requests
import webbrowser

def run_prog(command):
    p = Popen([sys.executable, command], stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    return output,error
#print(run_prog("your_file_name.py"))

def stackoverflow_req(err):
    response=requests.get("https://api.stackexchange.com/"+"/2.2/search?order=desc&sort=activity&tagged=python&intitle={}&site=stackoverflow".format(err))
    return response.json()

def get_urls(js_d):
    urlist=[]
    c=0
    for i in js_d["items"]:
        if i["is_answered"]:
            urlist.append(i["link"])
        c+=1
        if c==3:
            break

    #fetch urlist and open browser
    for i in urlist:
        webbrowser.open(i)

if __name__=='__main__':
    typ,error1=run_prog("your_file_name.py")
    error1=error1.decode("utf-8")
    err_mess=error1.split("\r\n")[-2]

    if err_mess:
        err=err_mess.split(':')
        #ignore err[1:]=[':'.join(err[1:])]
        get_urls(stackoverflow_req(err[0]))
        get_urls(stackoverflow_req(err[1]))
        get_urls(stackoverflow_req(err_mess))
    else:
        print("no error found")
