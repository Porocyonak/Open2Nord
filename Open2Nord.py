import json
import requests
import shutil
import subprocess
import os
import ctypes
import time


# Define some global variables. This info is taken from data.txt
lat = 0
long = 0
configDirectory = ""
savePasswords = False
maxLoad = 30
timeout = 150
country = 'US'
endWait = 1


# Wait for a connection every .3 seconds
def wait_for_internet_connection():
    while True:
        try:
            print("Attempting connection to NordVPN api...")
            time.sleep(.3) # fix 10-11-19 for polling spam bug. not reflected in github release (yet?)
            nordServers = requests.get('https://api.nordvpn.com/server')
            print("Success!")
            return nordServers
        except requests.exceptions.ConnectionError:
            pass


# Called to take data from data.txt and apply them to our global variables
def setVals():
    global lat
    global long
    global configDirectory
    global savePasswords
    global maxLoad
    global timeout
    global country
    global laptopOrPc

    file = open("data.txt", 'r+')
    lines = file.readlines()
    lat = float(lines[4])
    long = float(lines[5])
    configDirectory = str(lines[1]).strip()
    s = str(lines[8])
    if s.strip() in ['Yes', 'yes', 'y', 'true', 'True']:
        savePasswords = True
    else:
        savePasswords = False
    maxLoad = float(lines[11])
    timeout = float(lines[14])
    country = str(lines[17]).strip() # just in case
    endWait = float(lines[20])

    file.close()


# Called to sort a list of servers by location distance 
def getKey(each):
    latDifference = abs(each['location']['lat'] - lat)
    longDifference = abs(each['location']['long'] - long)
    total = latDifference + longDifference
    return total


def run():


    # Poll for the NordVPN API
    nordServers = wait_for_internet_connection()
    nordServersJson = nordServers.json()


    # Read data in the location txt file
    print("Reading given data...")
    setVals()


    # List of servers with < maxLoad
    print("Calculating best server...")
    usableServers = [] 
    bestPing = 9999
    bestServer = "null"
    numbersOnly = str.maketrans(dict.fromkeys('ms')) # Removes the ms from the ping results
    

    # Get every US server thats usable
    # For every server we find in the API, we only take the ones from val country, filter for below given server load, and add them to an array.
    for each in nordServersJson:
        if(each['flag'] == country):
            if(each['load'] <= maxLoad):
                if(each['load'] > 5): # low load usually has problems
                    usableServers.append(each)


    # Use getKey to properly sort servers by their location (closest to you)
    nearbyServers = sorted(usableServers, key=getKey)


    # Take this new sorted list, and ping each one, starting from the closest servers. Stop once we take the closest 15.
    usableServers.clear()
    print("We have a list of " + str(len(nearbyServers)) + " US servers! We will take the top 15 closest, and take the one with the highest ping.")
    index = 0

    for tempEach in nearbyServers: # Start iterating through the list

        # Increment index, check if max index reached, and ping each server (closest->farthest)
        index +=1
        if(index == 16):
            break
        ip1 = os.popen('ping ' + tempEach['domain'] + ' -n 1 -w ' + str(timeout)) # Ping the server with a timeout of 150ms
        result = ip1.readlines()

        # Check if ping went through
        try:                                                          # Strip out the resulting ping number
            msLine = float(result[-1].strip().split()[8].translate(numbersOnly))
        except:                                                       # Exception when the ping fails
            print("Connection timed out, ignoring...")
            continue # Skip this current loop so we don't add broken servers to our usableServers list

        # Checks and stores the server with the lowest ping
        if(msLine < bestPing):                                        
            bestPing = msLine
            bestServer = tempEach['domain']
            print("Server " + tempEach['domain'] + " has a faster ping of " + str(bestPing) + ". Setting as best server.")
        else:
            print("Server " + tempEach['domain'] + " is not faster, ignoring. Has a ping of " + str(msLine))

        # Add each server (that doesn't fail to return a ping) to a list of viable server choices
        usableServers.append(tempEach)
    

    # All done!
    if(bestServer=="null"):
        input("Critical Error! Server ping was never higher than 9999. This shouldn't ever happen! Check your internet.")
        return
    else:
        print("Congratulations! We have found the best server " + bestServer + " with a ping of " + str(bestPing))


    # Now we must copy the proper config to the OpenVPN folder
    # We open a file to read a directory and copy our needed file over to that directory.
    print("Copying config file over to OpenVPN...")
    # Flip it around so we can treat this list as a stack
    usableServers.reverse()
    while(os.path.isfile('config_files\\' + bestServer + '.udp.ovpn') == False):

        print("Server doesn't exist inside config_files, taking a different viable one.")
        if(len(usableServers)>0):
            bestServer = usableServers.pop()['domain']
            print("Next best server is: " + bestServer)
            # do the loop with a new bestserver
        else:
            input("Couldn't find any servers based on your given parameters. Edit data.txt and try again.")
            return
    

    # If you want automatic logins with your password saved locally
    if(savePasswords == True): 

        temp = open('temp.txt', 'w')
        with open('config_files\\' + bestServer + '.udp.ovpn', 'r') as f:
            for line in f:
                if line.startswith('auth-user-pass'):
                    line = 'auth-user-pass login_info.txt\n'
                temp.write(line)

        temp.close()
        # Copy over new config file and the login info txt
        shutil.move('temp.txt', configDirectory + '\\config\\' + bestServer + '.udp.ovpn')
        shutil.copyfile('login_info.txt', configDirectory + '\\config\\' + 'login_info.txt')
    else:
        # Since you no longer want to save login data, we delete the one we stored in the OpenVPN folder.
        if(os.path.isfile(configDirectory + '\\config\\' + 'login_info.txt') == True):
            os.remove(configDirectory + '\\config\\' + 'login_info.txt')
        shutil.copyfile('config_files\\' + bestServer + '.udp.ovpn', configDirectory + '\\config\\' + bestServer + '.udp.ovpn')


    print("Successfully copied file over to directory " + configDirectory)
    print("Attempting to run OpenVPN...")
    if(savePasswords == False):
        print("Use your NordVPN email and password when asked for credentials.")


    # Finally, lets run OpenVPN and connect to our server.
    FNULL = open(os.devnull, 'w')
    args = configDirectory + "\\bin\\openvpn-gui.exe --connect " + bestServer + '.udp.ovpn' # Find the OpenVPN .exe and ask it to connect
    b = subprocess.Popen(args, stdout=FNULL, stderr=FNULL, shell=False)

    # And we're done!
    print("Done! Closing...")
    time.sleep(endWait)


# Simple check for Admin rights (UAC), as we cannot move around files without it.
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    try:
        run()
    except Exception as e:
        print("-------------------------")
        print("Critical Error! Shutting down program.")
        print("Problem description:")
        print(e)
        input()
else:
    # Re-run the program with admin rights
    # ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1) # Causes problems when compiled into an EXE
    input("Please restart and run as admin! (only matters for manual execution)")
