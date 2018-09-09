# Open2Nord
I made this to bypass the Unity block when trying to run Unity with NordVPN connected. 

***Open2Nord*** does some light Python scripting to find the best NordVPN server for your location, and connects you to it automatically on logon through the OpenVPN GUI.

I also made sure that the code (and project itself) was short and sweet, so you can easily tell if anything fishy is going on. I'd like to say it's also easier for newbies to learn so they can do it themselves, but I can't say for certain! Let me know what to clear up so it's more understandable.


### ------------------Instructions------------------
1. `Install OpenVPN from` 

      a. https://swupdate.openvpn.org/community/releases/openvpn-install-2.4.5-I601.exe  
  
      b. https://nordvpn.com/tutorials/windows-7/openvpn/
  
2. `Download and extract the compiled Open2Nord.zip version` [here](https://github.com/Porocyonak/Open2Nord/releases) `or build your own Open2Nord`

      2a. make sure you extract it to a good place, like `C:\Programs\Open2Nord` 
      ## **DO NOT HAVE SPACES OR PARENTHESIS IN THE DIRECTORY!**

3. `Modify the data.txt folder accordingly. I reccomend` https://gps-coordinates.org/ `for grabbing location data`
4. **`[Optionally]`**`Modify the login_info.txt with your NordVPN email and password`
5. `Run RunOnStartup (Run Me!).bat (will run the Open2Nord every computer boot)`
6. **`[Optionally]`**`Run Open2Nord.exe to connect right away`

**NOTE: Make sure to run `RunOnStartup (Run Me!).bat` again if you change the project directory!**

### ------------------Build It Yourself--------------
TODO cleanup, make more newbie friendly. 
1. download source and extract source
2. pip install requests and cx_freeze
3. modify a couple lines in setup.py so they point to your python directory
4. run "python setup.py build" in terminal at the project directory (that has setup.py)
5. move all the files in `move_to_build_directory` to the newly made build directory (same path as Open2Nord.exe)
      
      5a. make sure you extract the config_files.zip so that the config_files folder appears in the same directory, and is full of .ovpn files
      
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
