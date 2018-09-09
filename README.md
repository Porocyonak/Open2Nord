# Open2Nord
I made this to bypass the Unity block when trying to run Unity with NordVPN. 

***Open2Nord*** does some light Python scripting to find the best NordVPN server for your location, and connects you to it automatically on logon using the OpenVPN GUI.

I also made sure that the code was short and sweet, so you can easily tell if anything fishy is going on


### ------------------Instructions------------------
1. `Install OpenVPN from` 

      a. https://swupdate.openvpn.org/community/releases/openvpn-install-2.4.5-I601.exe  
  
      b. https://nordvpn.com/tutorials/windows-7/openvpn/
  
2. `Download the release version or build your own OpenVPN-To-NordVPN`
3. `Modify the data.txt folder accordingly`
4. **`Optionally`**`Modify the login_info.txt with your NordVPN email and password`
5. `Run RunOnStartup (Run Me!).bat (will run the .exe every computer boot)`
6. `*Optionally* Run Open2Nord.exe to connect right away`

Done!

### ------------------Build It Yourself--------------
todo. basically just pip install requests and cx_freeze, modify a couple lines in setup.py so they point to your python directory,  and do "python setup.py build" in terminal in the directory with setup.py

### -------------------How It Works------------------
**`RunOnStartup (Run Me!).bat`** creates a windows Task Scheduler to run **Open2Nord** on every boot. It calls `XML_Stuff.bat` which does some batch modifications of `task_info.xml` so its customized to your system, and then creates a new Task with this new XML named `newtext.xml`.

**`StopStartup.bat`** deletes the task named **Open2Nord**. Basically stops Open2Nord from running on boot.

**`ScheduleFixer_donotrun.bat`** is a quick fix for Task Scheduler so it runs in the proper directory

**`data.txt`** takes user input to modify how they want **Open2Nord** to run.

**`login_info.txt`** takes an email on the first line and password on the second; used to automatically connect to NordVPN's servers.

**`config_files`** is a list of server config files given from NordVPN's website

**`Open2Nord.exe`** - view Open2Nord.py for more info
### -------------------------------------------------

If you are getting config errors, replace the files inside the config_files folder with the .ovpn files from https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip

And you're done! Let me know if there are any problems.

## Demonstration:
![Alt Text](https://i.imgur.com/YafoZ3a.gif)
