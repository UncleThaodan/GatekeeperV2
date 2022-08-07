# **Gatekeeper V2**

Welcome to the efforts of countless hours of learning and failed attempts at writing code that culminated into this project known as Gatekeeper! Originally this started out as a bot to bring CubeCoders AMP to Discord with support for only Minecraft, but has evolved into this encompasing project of providing support for any type of server AMP can run along with providing as many of AMPs core features inside of Discord.


Come Join my Discord **[Kat's Paradise](https://discord.gg/s5FnnsbJ)**


### **Requirements**
_________
- Python 3.1 or greater
- Pip 2.1 or greater
- Discord.py 2.0 or greater 
    - *Please visit: https://github.com/Rapptz/discord.py to install discord.py development version!*
- Cube Coders AMP License
    - *https://cubecoders.com/AMP*


## **Installation Methods**
___
### **Manual Instructions**
1. Open your command line: run `sudo apt-get install -y python3 pip && git clone https://github.com/Rapptz/discord.py && cd discord.py && python3 -m pip install -U .[voice]`
2. Create an AMP user for the Bot with `Super Admins` role.
3. Follow the instructions in `tokenstemplate.py` file -> [tokenstemplate.py](/tokenstemplate.py)
4. From Command Line run script `start.py` *(eg. `../Discord Bot/start.py`)*
    - Run the bot, it will finish installing the rest of the requirements.
5. See **Interacting with the Bot~**

### **AMP Instance Instructions**
1. Create an AMP user for the Bot with `Super Admins` role.
2. Create a new instance of GatekeeperV2 in a container. *(The container option can be found under `Configuration -> New Instance Defaults`)*
3. Configure the settings in the GatekeeperV2 Instance under the `Configuration -> Bot Settings`, click `Update`, then start the bot.
4. See **Interacting with the Bot~**
___

## **Interacting with the Bot**
*Channel ID and Channel Name are interchangable in commands*


__Setting up a NON-Adminstrator Role for the Bot__
- **TIP** - Use this if you want NON-Discord Admins to have the ability to interact with the bot*
- Use `/bot setup role_id` and the bot will add that role as the minimum required role to interact with the bot.
    - It does honor the role heirarchy set via `Discord -> Server Settings -> Roles`.


__Setting your AMP Console Channels__
- Use `/server console channel channel_id` and the bot will begin sending AMP Console messages to that channel. 
    - **TIP**: You can also send AMP Console commands through that Discord Channel to the Dedicated Server.


__Setting your AMP Chat Channels__
- Use `/server chat channel channel_id` and the bot will begin sending AMP Chat messages to that channel. 
    - **TIP**: You can also send Chat messages through that Discord Channel to the Dedicated Server.


__Setting your Whitelist Channel/Settings__
- Use `/bot whitelist channel set channel_id/channel_name`
    - *Optional*: Using the auto-whitelist feature, simply use the command `/bot whitelist auto whitelist true`
        - The Bot has a default wait time of 5 minutes. *(eg. `/bot whitelist waittime 5`)* **TIP**: You can set this value to `None` or `0`.
        - If the message was parsed successful they are added to the whitelist waitlist, after the timer is up they are whitelisted!.

___
## **Commands List**
*This documentation is subject to change and is purely temporary*

__Bot__ *( eg. `/bot settings`)*
- Settings - *Lists all Bot Settings*
- Setup - *Sets the Discord Role for Staff*
- ping - *Pong!*
- cog loader - *Loads a specific Cog (you must provide the directory name too)*
- cog unloader - *Unloads a specific Cog (by name)*
- stop - *Stops the Bot*
- restart - *Restarts the Bot*
- status - *Checks for AMP version/setup, DB version/setup and Displays Bot version information*
- sync - *Syncs Gatekeeper commands to the current guild*
- __Whitelist__ *(eg. `/bot whitelist channel`)*
    - Whitelist auto - *Allows the bot to automatically Whitelist a Users request*
    - Whitelist channel - *Sets the Whitelist channel for the bot to listen too*
    - Whitelist waittime - *Sets the Whitelist wait time after message is received*
    - Whitelist done_emoji - *Set an Emoji for to be applied to finished whitelist requests*
    - Whitelist pending_emoji - *Set an Emoji to be applied to pending/waiting whitelist request*

___

__DBServer__ *(eg. `/dbserver cleanup`)*
- !TBD(**Do Not Use**) - cleanup : Removes any DB Servers that are not in AMP instances
- !TBD(**Do Not Use**) - instance swap : Will be used for swapping instances via InstanceIDs

___
__User/Member Group__ *(eg. `/user info`)*
- Info - *Displays User information from the DB*
- Add - *Adds a User to the DB*
- Update - *Updates a user Minecraft In-Game Name, Minecraft UUID, Steam ID or Donator status*
- UUID - *Gets a users UUID! via Minecraft In-Game Name*

___
__Server__ *(eg. `/server list`)*
- list - *Lists all available servers*
- start - *Starts the specified dedicated server*
- stop - Stops the specified dedicated server 
- restart - *restarts the specified dedicated server* 
- kill - *kills the specified dedicated server* 
- console msg - *sends a message through the console for the specified dedicated server*
- backup - *creates a backup of the dedicated server*
- status - *displays a embedded message of the dedicated server with buttons for start, stop, kill and restart. (see #showcase)*
- users list - *displays a list of connected users to the dedicated server*
- display name - *sets the display name of the dedicated server in the DB (purely for display purposes)*
- description - *sets the description of the dedicated server in the DB (purely for display purposes)*
- IP- *sets the IP of the dedicated server in the DB (purely for display purposes)*
- role - *sets the role of the dedicated server in the DB*
- __Donator__ *(eg. `/server donator true`)*
    - true - *Sets Donator Only Flag for the dedicated server to True*
    - false - *Sets the Donator Only flag for the dedicated server to False*
- __Console__ *(eg. `/server console on`)*
    - on - *Turns the console on for the dedicated server (default: on)*
    - off - *Turns off the console for the dedicated server*
    - channel - *Sets the discord channel for the dedicated server to output too*
    - filter - *Enable or Disable console filtering for the dedicated server*
- __Chat__ *(eg. `/server chat channel`)*
    - channel - *Sets the discord channel for the dedicated server to output its chat messages*
- __Whitelist__ *(eg. `/server whitelist true`)*
    - true - *Sets the whitelist flag to true for the dedicated server*
    - false - *Sets the whitelist flag to false for the dedicated server*
    - add - *Adds the IGN to the dedicated server whitelist*
    - remove - *Removes the IGN from the dedicated server whitelist*

______
## **Launch Args**
- `-token` - Bypasse tokens validation check. *(Mandatory for AMP Template Installations/Operations)*
- `-command` - Enable slash command print statements for user traceback.
- `-dev` - Enable development print statments. *(used for development)*
- `-debug` - Enables *DEBUGGING* level for logging. *(used for development)*
- `-discord` - Disables Discord Intigration *(used for testing)*
- `-super` - This leaves AMP Super Admin role intact, use at your own risk.    
___
### **Credits**
"**Thank You**" to everyone at CubeCoders Discord Server, especially *IceofWrath, Mike, Greelan* and everyone else in their discord.

"**Thank You**" to everyone over at Discord.py Discord Server, especially *SolsticeShard and sgtlaggy* for all the silly questions I kept asking about embed's and Hybrid messages!