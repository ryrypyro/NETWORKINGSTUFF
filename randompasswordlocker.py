# PASSWORD LOCKER PROJECT 


# PW.PY  -- insecure pw locker program! 


# 1 - program design / data structure. store values of the objects within PASSWORDS. 
#! python3 
PASSWORDS = {
    'email': '5t0iwt8ihwthwet87hqwrwtjerhttyhujiry',
    'blog': 'teghib8y7gf43t48yby8g32t4yb',
    'luggage': '5647'
}

# 2 - handle command line arguments 
#! python3 
import sys 
if len(sys.argv) < 2: 
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # 1st cmd line arg is the account name 

# 3 - copy the right password 
#! python3 
# now that account name is stored in account, check if it ecists in PASSWORDS.. 

account = sys.argv[1]
import pyperclip
if account in PASSWORDS: 
    pyperclip.copy(PASSWORDS[account])
    print('PASSWORD FOR ' + account + ' copied to clipboard!')
else: 
        print('sorry, we cannot find an account named ' + account)