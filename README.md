# Open2Nord
I made this to bypass a Unity3D block when trying to run Unity3D with NordVPN connected. Connecting to NordVPN servers through OpenVPN GUI fixes this 'unity block' issue, **but there are two major problems:** OpenVPN GUI can't be configured to run and connect on startup, and there isn't a way to find the 'best' server to connect to.
**Open2Nord fixes these two issues!**

***Open2Nord*** does some light Python scripting to find the best NordVPN server for your location, and connects you to it automatically on logon through the OpenVPN GUI.

I also made sure that the code (and project itself) was short and sweet, so you can easily tell if anything fishy is going on. I'd like to say it's also easier for newbies to learn so they can do it themselves, but I can't say for certain! Let me know what to clear up so it's more understandable.

(Currently only supports Windows 10, maybe Windows 7)


### ------------------Instructions------------------
1. `Install OpenVPN from` 

      a. https://swupdate.openvpn.org/community/releases/openvpn-install-2.4.5-I601.exe  
  
      b. https://nordvpn.com/tutorials/windows-7/openvpn/
  
      c. https://nordvpn.com/tutorials/windows-10/openvpn/
      
2. `Download and extract the compiled Open2Nord.zip version` [here](https://github.com/Porocyonak/Open2Nord/releases) `or build your own Open2Nord`

      a. make sure you extract it to a good place, like `C:\Programs\Open2Nord` 
      ## **DO NOT HAVE SPACES OR PARENTHESIS IN THE DIRECTORY!**

3. `Modify the data.txt folder accordingly. I recommend` https://gps-coordinates.org/ `for grabbing latitude and longitude (will eventually be automated)`
      
      a. also make sure your OpenVPN directory ends at OpenVPN e.g: C:\Program Files\OpenVPN
      [as shown](https://i.imgur.com/mi04WHC.png)
      so 'OpenVPN directory' should point to this area of the OpenVPN install
4. **`[Optionally]`**`Modify the login_info.txt with your NordVPN email and password. Keep in mind this is stored in plaintext on your device.`
5. `Run RunOnStartup (Run Me!).bat (will run Open2Nord every computer boot)`
6. **`[Optionally]`**`Run Open2Nord.exe (as admin) to connect right away`

**NOTE: Make sure to run `RunOnStartup (Run Me!).bat` again if you change the project directory!**

### ------------------Build It Yourself--------------
TODO cleanup, make more newbie friendly. 
1. install python 3.x, most versions should be compatible
2. download source and extract source
3. pip install requests and pip install cx_freeze (or look up how to install requests and cx_freeze)
4. modify a couple lines in setup.py so they point to your python directory
5. run "python setup.py build" in terminal at the project directory (that has setup.py)
6. move all the files in `move_to_build_directory` to the newly made build directory (same path as Open2Nord.exe)
      
      a. make sure you extract the config_files.zip so that the config_files folder appears in the same directory, and is full of .ovpn files
      
Final product should be something like this: ![final](https://i.imgur.com/sBimI6u.jpg)

Config folder should look like: ![config](https://i.imgur.com/UZKaa5p.png)

### -------------------How It Works------------------
* **`RunOnStartup (Run Me!).bat`** creates a windows Task Scheduler to run **Open2Nord** on every boot. It calls `XML_Stuff.bat` which does some batch modifications of `task_info.xml` so it's customized to your system, and then creates a new Task with this new XML named `newtext.xml`.

* **`StopStartup.bat`** deletes the task named **Open2Nord**. Basically stops Open2Nord from running on boot.

* **`ScheduleFixer_donotrun.bat`** is a quick fix for Task Scheduler so it runs in the proper directory

* **`data.txt`** takes user input to modify how they want **Open2Nord** to run.

* **`login_info.txt`** takes an email on the first line and password on the second; used to automatically connect to NordVPN's servers.

* **`config_files`** is a list of server config files given from NordVPN's website

* **`Open2Nord.exe`** - view Open2Nord.py for more info
### -------------------------------------------------

If you are getting config errors, replace the files inside the config_files folder with the .ovpn files from https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip (might make a quick script to do this automatically later)

And you're done! Let me know if there are any problems.

## Demonstration:
![demo](https://i.imgur.com/YafoZ3a.gif)
![hi](https://i.imgur.com/OpULrTR.png)

#### Extra Notes:
* connect through 1.1.1.1 (see https://1.1.1.1/ ) to get Amazon and other sites working, if they aren't

#### Todo:
* automatically grab latitude/longitude from current ip
* automatically refresh config files if outdated
* fix an issue when there are more than 50 config files in OpenVPN GUI config folder automatically (if you are experiencing this, just delete a bunch of them. OpenVPN GUI doesn't like more than 50 config files)
* change task to have 'onlogon for specific user' instead of all users (unsure if this affects anything. if you have this issue let me know, i'll see if I can fix it)
* make time.sleep wait longer than .3 seconds, potential inefficiency in polling so fast
